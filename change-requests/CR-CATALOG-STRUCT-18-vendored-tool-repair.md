# CR-CATALOG-STRUCT-18: Vendored-Tool Repair (Clean Re-Vendor from v2.8.0)

**Status**: Open
**Layer**: L1 (Stakeholders Catalog; tooling repair)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-11
**Trigger**: `catalog-conformance` red on main since PR #23 (2026-11-10), compound: (1) the workflow pins `ref: v2.8.0` which did not exist yet (404 checkout; the upstream release was cut 2026-11-11 at the PR #63 merge commit, resolving this half), and (2) behind it, CR-CATALOG-STRUCT-17's re-vendor landed a **mangled** `scripts/regenerate_catalog.py`: every blank line stripped (823 vs the source's 857), one comment's `# ` prefix lost (line 55, leaving `catalog repos already use).` as bare code -> `SyntaxError: unmatched ')'`), and comments re-wrapped. `scripts/check_catalog_index.py` carried the same blank-line stripping but compiled and stayed semantically identical. The vendored copy could never have executed; the 404 masked it. Found while resolving the owner-reported 404.
**Carrier**: Single PR on feature branch `fix/regenerator-revendor-v2.8.0`. PR review, not direct push.
**Lands against**: `main` @ `1c23417` (post STRUCT-17, PR #23)
**Depends on**: CR-CATALOG-STRUCT-17; upstream `dea-metaframework` release v2.8.0 (tagged 2026-11-11 at the CR-CATALOG-STRUCT-12 merge commit `607eef6`)

## 1. What lands

| Site | Change |
|---|---|
| `scripts/regenerate_catalog.py` | wholesale clean re-vendor from `dea-metaframework` v2.8.0 (`tools/regenerate_catalog.py` @ `607eef6`); zero stakeholders-specific logic existed in the copy, so this is byte-exact to the source the CR-STRUCT-17 entry already specified |
| `scripts/check_catalog_index.py` | same clean re-vendor (its only defect was cosmetic blank-line stripping; re-vendored for byte-truth) |

## 2. Verification

- `python -m py_compile scripts/regenerate_catalog.py scripts/check_catalog_index.py`: clean.
- `regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json`: CATALOG.yaml is current (byte-idempotent against the PR #23 committed index, which the grouped-shape machinery produces identically).
- `check_catalog_index.py --strict`: OK, 23 entities.
- `check_pointer.py`, `check_schema.py`: Findings 0.
- `check_entity_system.py`: CONFORMANT; `check_id_system.py --strict`: 23 records, 0 findings; `check_authorship.py --strict`: 0 hits.
- Conformance suite (v2.8.0): 17/17 CSTs, 0 warnings (`--strict`).

## 3. NOT-List

- **No behavior change**: the clean files are exactly what CR-CATALOG-STRUCT-17's "tooling re-vendors from v2.8.0" already specified; this repairs the copy operation, not the design.
- **No record, schema, or CATALOG.yaml change** beyond the standing-discipline regeneration after the CR-status flip below.
- **No workflow change**: the `ref: v2.8.0` pin was correct and is now resolvable; the install-if-missing staging stays.

## 4. Standing discipline

CR-CATALOG-STRUCT-17's status updates to `Merged (PR #23)` in this PR; `CATALOG.yaml` regenerates after the status flip (open_change_requests count), in the same PR.

## 5. Acceptance criteria

1. CI green on this PR, including `catalog-conformance` end-to-end (checkout at v2.8.0, regen freshness, index gate, CST suite, entity-system/IDM/authorship gates).
2. `open_change_requests: 0` in the regenerated index.
3. Vendored tools byte-identical to the v2.8.0 source (`cmp`).
