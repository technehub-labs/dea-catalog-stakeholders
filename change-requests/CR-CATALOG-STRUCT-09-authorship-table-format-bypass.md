# CR-CATALOG-STRUCT-09: Authorship Gate Table-Format Bypass (AUT-001 Coverage Hole)

**Status**: Proposed
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Review 2026-10-27 (`review-report-dea-catalog-stakeholders.md`, concern 2; bypass reproduced empirically against `main` @ `de4a581`). The review was performed agent-side on eaojnr's behalf; agency is recorded here rather than in the authorship field, per the cardinal rule this CR enforces.
**Carrier**: this file
**Lands against**: `main` @ `de4a581`
**Depends on**: none (landing after STRUCT-08 keeps index arithmetic single-step)

## 1. Problem (proven, not inferred)

`scripts/check_authorship.py` `_extract_value` (`:166-187`) only recognizes line-format fields — a line must literally start with `**Owner**:` or `**Author**:`. CRs written in the table metadata shape (`| **Author** | <value> |`) expose no visible field to the gate.

Reproduction against the live tree (2026-10-27): a CR file carrying

```
\| **Author** \| Coder (for eaojnr) |
\| **Owner** \| Hermes |
```

(the leading pipes are escaped here exactly because the fixed gate scans this carrier too; unescaped, those two rows are the probe) passes the pre-fix `python3 scripts/check_authorship.py --strict` with **0 findings, exit 0** — both denylisted values invisible. On `main` today, 2 of 3 CRs (STRUCT-06, STRUCT-07) use the table shape, so their authorship fields are entirely unchecked, and AUT-002 cannot fire for a CR that carries no authorship field at all (STRUCT-06's table has no Owner row; nothing requires one to exist). The CHANGELOG's "authorship gates remain CONFORMANT" claims are true of the gate's output but overstate what is actually being checked. This is the same format-blindness class as the regenerator's Status parsing (STRUCT-08 §1) — the house CR format has drifted to tables while the copied validators parse one shape.

## 2. Design

### 2.1 Parser fix (`scripts/check_authorship.py`)

`_extract_value` gains a table-row shape for markdown field paths (design verified locally — all six probe cases pass; see §3):

```python
_TABLE_ROW_RE_CACHE: dict[str, re.Pattern] = {}

def _extract_value(line: str, field_path: str) -> str | None:
    """Extract a registered field's value from a single line.

    Field shapes:
      - ``**Owner**: <value>``        -> line-format markdown CR metadata
      - ``| **Owner** | <value> |``   -> table-format markdown CR metadata
      - ``audit.author: <value>``    -> YAML (any leading whitespace)
    """
    stripped = line.strip()
    if field_path.startswith("**") and field_path.endswith("**"):
        prefix = f"{field_path}:"
        if stripped.startswith(prefix):
            return stripped[len(prefix):].strip()
        pat = _TABLE_ROW_RE_CACHE.get(field_path)
        if pat is None:
            pat = re.compile(
                r"^\|\s*" + re.escape(field_path) + r"\s*\|\s*(.+?)\s*\|$"
            )
            _TABLE_ROW_RE_CACHE[field_path] = pat
        m = pat.match(stripped)
        if m:
            return m.group(1)
        return None
    # YAML shape unchanged
    ...
```

The row regex is anchored end-to-end and keys on the exact field path, so adjacent table keys (`| **CR** |`, `| **Companion to** | ...`) cannot match. Registry-driven as before: any `**...**` path gains both shapes; YAML paths are unchanged.

### 2.2 Presence rule (AUT-002 extension)

Today AUT-002 fires only when a line-format field is present but empty. Add the missing half: **a file matching a registered field's `file_glob` that exposes no instance of any registered field for that glob fires AUT-002** (blocking; the CR header block is the "parent block" and it is by definition present in a CR doc). Exempt `_is_preserved` files. Concretely, in `evaluate()`: track per-file whether any registered path yielded a value; emit one AUT-002 finding per field-silent file after the scan.

Live-tree check (no false positives): STRUCT-05 exposes `**Owner**: TechNeHub Labs`; STRUCT-06 and STRUCT-07 each expose `| **Author** | Emmanuel A. Otchere |` under the fixed parser — all three files satisfy the presence rule, so the gate stays CONFORMANT on this repo's tree.

### 2.3 Regression tests (`tests/test_check_authorship.py`)

Add tests mirroring the reproduction and the design probes:

1. Table-format denylist: a CR with `| **Author** | Coder (for eaojnr) |` fires AUT-001 (the exact bypass probe; must exit 1).
2. Table-format allowlist: `| **Owner** | TechNeHub Labs |` and `| **Author** | Emmanuel A. Otchere |` produce no findings.
3. Adjacent-key negative: `| **CR** | ... |` and `| **Companion to** | ... |` rows alone yield no extracted value.
4. Presence rule: a CR-*.md with no Owner/Author field in either shape fires AUT-002.
5. Line-format behavior unchanged (existing 21 tests keep passing unmodified).

### 2.4 CI

No workflow change needed: `validate-authorship.yml` already runs the gate `--strict` plus this test module; the new tests land inside the existing step.

## 3. Design verification (2026-10-27, local)

The extraction logic of §2.1 was exercised against: the two live table-format CRs (values `Emmanuel A. Otchere` — extracted, allowlisted), the bypass probe values (`Coder (for eaojnr)` — extracted, would fire AUT-001), adjacent-key negatives (no match), and line-format positives (unchanged). Full-visibility result on the live tree: STRUCT-05 -> `[('**Owner**', 'TechNeHub Labs')]`, STRUCT-06 -> `[('**Author**', 'Emmanuel A. Otchere')]`, STRUCT-07 -> `[('**Author**', 'Emmanuel A. Otchere')]`. After this CR lands, the gate's CONFORMANT verdict covers all CR files, not 1 of 3.

## 4. Acceptance criteria

- AC-01 New unit tests 1-5 (§2.3) pass; suite total is 21 + 5 = 26 in `tests/test_check_authorship.py`.
- AC-02 Bypass probe: a tree containing a table-format `Coder`/`Hermes` CR makes `python3 scripts/check_authorship.py --strict` exit 1 with AUT-001 findings naming the file and line.
- AC-03 Live tree: `python3 scripts/check_authorship.py --strict` exits 0 (all three prior CRs now visible with allowlisted values; carriers 08/09/10 line-format `**Owner**` visible).
- AC-04 Presence rule: removing every authorship field from a CR matching the glob fires AUT-002 (covered by unit test 4).
- AC-05 `CHANGELOG.md` gains an `[Unreleased]` entry noting the coverage hole and its closure (the STRUCT-06/07 CHANGELOG claims of "gates remain CONFORMANT" predate the discovery; no history rewrite).
- AC-06 `change-requests/README.md` gains the STRUCT-09 row; prior carriers' statuses updated per the STRUCT-08 standing discipline; `CATALOG.yaml` regenerated in the same PR.

## 5. NOT-List

- No registry change (`reconciliation/authorship-fields.yaml` paths, allowlist, denylist untouched — the parser handles the second shape for already-registered `**...**` paths).
- No entity-record authorship fields: none exist; registering `audit.author` for `entities/v1-alpha/**/stakeholders-stakeholder-*.yaml` happens with the first admission CR, as the registry header already prescribes.
- No prose-content sweep of `Coder`/`Agent` in narrative fields (the CR-BP-118c class) — this repo's narrative fields are already clean.
- No regenerator Status parsing (STRUCT-08), no CI wiring changes (STRUCT-10).
