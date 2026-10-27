# CR-CATALOG-STRUCT-08: Main-Green Remediation (Counter Fix, CR Statuses, Index Row, Metaframework Ref Pin)

**Status**: Merged (PR #8)
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Review 2026-10-27 (`review-report-dea-catalog-stakeholders.md` in the OpenDEA workspace, concerns 1, 3, 6; verified against `main` @ `de4a581`). The review was performed agent-side on eaojnr's behalf; agency is recorded here rather than in the authorship field, per the CR-BP-118 cardinal rule as propagated by CR-CATALOG-STRUCT-06.
**Carrier**: this file
**Lands against**: `main` @ `de4a581`
**Depends on**: none (STRUCT-09 and STRUCT-10 are independent follow-ons)

## 1. Problem (verified on `main` @ `de4a581`)

`main` is red on `catalog-conformance` and has been since 2026-10-14 (every run after PR #4's era; both October merges landed red). Two independent causes; fixing either alone leaves `main` red:

1. **Stale `CATALOG.yaml`.** `python scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json` exits 3: the committed index says `open_change_requests: 1`, the regenerator computes 3. PRs #6 (STRUCT-06) and #7 (STRUCT-07) added carrier CRs without regenerating the index. This is the step CI fails on (confirmed against the run's job steps).
2. **CST-013/014.** The cross-repo suite exits 2: the `dea-metaframework` checkout in `.github/workflows/catalog-conformance.yml` carries no `ref:` pin. Masked in CI today only because the workflow stops at the earlier regenerator failure — this CR fixes both layers in one PR so `main` goes green once, not twice.

Underlying the staleness, the vendored counter in `scripts/regenerate_catalog.py:499-529` (`count_open_change_requests`) is wrong in three stacked ways (same family as processes `:466` and capabilities `:518`):

- `:518` — duplicated condition `if "Status**: Merged" in head or "Status**: Merged" in head:`; the second operand was meant to be a different closed status.
- The closed set is `Merged`-only (line format), while this repo's CR statuses are `Proposed` / `Accepted` / `Proposed (this PR)` — no CR will ever say `Merged` until this CR updates them, and even then table-format CRs stay invisible.
- Table-format metadata rows (`| **Status** | ... |`, used by STRUCT-06 and STRUCT-07) are not parsed at all; those files fall through to "conservative open".

Bookkeeping that rode along: the CR index (`change-requests/README.md`) has no row for STRUCT-06 at all, and the rows/files for merged CRs still say `Proposed`.

## 2. Design

### 2.1 Counter fix (`scripts/regenerate_catalog.py`)

Replace the string-probe body of `count_open_change_requests` with a status-token parser (design verified locally against all three live CR files):

```python
# Terminal CR statuses: the org-consistent closed set, as landed in
# dea-catalog-business-capabilities PR #91 / CR-DEA-BC-38 (itself a superset
# of the CR-BP-114 set ratified in dea-catalog-processes; covers this repo's
# Accepted and the Merged introduced by this CR).
CLOSED_CR_STATUSES = frozenset(
    {"Merged", "Landed", "Applied", "Accepted", "Rejected", "Superseded", "Withdrawn"}
)

_STATUS_LINE_RE = re.compile(r"^\*\*Status\*\*:\s*(.+)$")
_STATUS_TABLE_RE = re.compile(r"^\|\s*\*\*Status\*\*\s*\|\s*(.+?)\s*\|$")

def _cr_status_token(head: str) -> str | None:
    """First Status value in the CR head, as a bare token.

    Accepts both house metadata shapes (line `**Status**: X` and table
    `| **Status** | X |`), stripping trailing context such as
    `(PR #6)` or `(per user directive ...)`.
    """
    for line in head.splitlines():
        s = line.strip()
        m = _STATUS_LINE_RE.match(s) or _STATUS_TABLE_RE.match(s)
        if m:
            return re.split(r"[;(,]", m.group(1))[0].strip()
    return None
```

Loop body: derive `head` as today (first 30 lines); `token = _cr_status_token(head)`; `if token is not None and token in CLOSED_CR_STATUSES: continue`; otherwise (Proposed, Draft, unknown token, or no status line) count open — the existing conservative semantics are preserved.

Verified arithmetic on the live tree:
- Fixed parser, statuses as committed today: count = 2 (STRUCT-06 `Accepted` closes; the two `Proposed` stay open).
- After this CR's status updates (§2.2): count = 0.
- This CR's own carrier lands as `Proposed`: rendered count in the landing PR = 1.

Self-reference note (verified): §1 of this carrier quotes the buggy `:518` line, and the quoted text `if "Status**: Merged" in head ...` falls inside the carrier's first 30 lines — the **old** substring heuristic therefore miscounts this very file as closed (observed: proposal tree computes 5 open for 6 CR files). The fixed parser is immune: it returns the first status line's token, which is `Proposed` at line 3, before the quotation at line 21.

### 2.2 CR status truth (three files, factual corrections recorded here, not silent rewrites)

All three CRs are merged; their Status fields now say so, with PR links:

- `change-requests/CR-CATALOG-STRUCT-05.md`: `**Status**: Proposed` -> `**Status**: Merged (PR #3)`
- `change-requests/CR-CATALOG-STRUCT-06-authorship-cardinal-rule.md`: `| **Status** | Accepted (per user directive 2026-10-13) |` -> `| **Status** | Merged (PR #6; accepted per user directive 2026-10-13) |`
- `change-requests/CR-CATALOG-STRUCT-07-entity-system-stakeholders.md`: `| **Status** | Proposed (this PR) |` -> `| **Status** | Merged (PR #7) |`

Standing discipline introduced with this CR (recorded in `change-requests/README.md`): **every landing PR updates the Status of CRs merged by earlier PRs and regenerates `CATALOG.yaml` in the same PR.** Steady-state open count is then 1 (the current carrier), and the index never rots again.

### 2.3 CR index (`change-requests/README.md`)

- Add the missing STRUCT-06 row (title, `Merged (PR #6)`, one-line summary).
- STRUCT-07 row status -> `Merged (PR #7)`; drop "(this PR)".
- STRUCT-05 row status -> `Merged (PR #3)`.
- Add the discipline note from §2.2 as a one-line convention under the table.
- Add the STRUCT-08 row (this CR, `Proposed`).

### 2.4 Metaframework ref pin (`.github/workflows/catalog-conformance.yml`)

The `dea-metaframework` checkout step gains `ref: v2.6.0` (latest release tag as of 2026-10-27). Verified locally: with the checkout pinned to a tag, the CST suite's CST-013/014 findings clear and the suite exits 0 against this tree (16 CSTs).

### 2.5 Regenerate `CATALOG.yaml`

Run `python scripts/regenerate_catalog.py --schema catalog-index-schema/catalog-index-schema.json` with origin set to the canonical HTTPS URL (CI sets `https://github.com/technehub-labs/dea-catalog-stakeholders.git`); commit the result. Rendered count at this PR = number of `Proposed` carriers it carries (with only this carrier: 3 prior CRs closed by §2.2 + this one open = 1 — the committed value happens to already be 1, in which case the regenerated file is byte-identical and `--check` passes without a visible delta; regenerate and commit regardless). If the PR rides all three STRUCT-08/09/10 carriers, the rendered count is 3 and steps 3 -> 2 -> 1 as the later PRs close prior carriers per §2.2.

## 3. Acceptance criteria (all verifiable locally and in CI)

- AC-01 `python scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json` exits 0 on the landing PR's tree.
- AC-02 `_cr_status_token` parses both metadata shapes: unit-level spot checks on all three prior CR files return `Merged` after §2.2 (verified in design; re-verify after edit).
- AC-03 `python .metaframework/tools/conformance_test_catalog_structure.py --catalog-root . --template-root .metaframework/tools/catalog-repo-template --strict` (with the checkout at `ref: v2.6.0`) exits 0: 16 CSTs, 0 warnings.
- AC-04 The `catalog-conformance` workflow is green on `main` after this PR merges (first green run since 2026-09-21).
- AC-05 `change-requests/README.md` carries rows for STRUCT-05, 06, 07 (statuses `Merged (PR #N)`) and 08 (`Proposed`), plus the standing-discipline note.
- AC-06 `python3 scripts/check_authorship.py --strict` still exits 0 (status-row edits do not touch authorship fields).
- AC-07 `CHANGELOG.md` gains an `[Unreleased]` entry for STRUCT-08.

## 4. NOT-List

- No change to `check_authorship.py` parsing (table-format authorship bypass is STRUCT-09's carrier).
- No removal of `continue-on-error: true` from `validate-entity-system.yml`, no pytest wiring into `catalog-conformance.yml` (STRUCT-10).
- No fix to `dea-metaframework` upstream: the counting bug exists there too (`tools/regenerate_catalog.py:519` at master, 2026-10-27). This CR patches the vendored copy; the upstream fix and re-vendor is a separate metaframework CR. Until then the vendored copy intentionally diverges from upstream by this fix.
- No re-vendor of the entropy-alphabet tightening (`[a-z2-9]` vs upstream's explicit 31-symbol class): benign for the 0-record catalog; re-vendor with the upstream fix.
- No Phase 2 changes to `ci.yml` (early-exit, action swap) — tracked by STRUCT-05 §"Phase 2 path".
- No doc-truth sweep beyond the CR index (CONTRIBUTING/cardinal-rules/entities README/README/pointer are STRUCT-10).

## 5. Sequencing

STRUCT-08 -> STRUCT-09 -> STRUCT-10 (independent in content; the order keeps each PR's `CATALOG.yaml` arithmetic a single-step delta: 1 -> 1 -> 1, with each PR closing the prior carrier's status per §2.2).
