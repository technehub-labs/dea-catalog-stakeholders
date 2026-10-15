# Change Requests

This directory tracks formal change requests (CRs) for `dea-catalog-stakeholders`.

| CR | Title | Status | Summary |
|---|---|---|---|
| [CR-CATALOG-STRUCT-07](CR-CATALOG-STRUCT-07-entity-system-stakeholders.md) | Entity System Stage 5-6 (Stakeholders Slice) | **Proposed (this PR)** | Stakeholders slice of the General Entity System institutionalisation (cross-repo cascade T7). New `reconciliation/entity-system-registry.yaml` (per-repo; generic; no profiles; canonical pattern matches the repo namespace). New `scripts/check_entity_system.py` (5-rule umbrella gate; copied verbatim from `dea-catalog-processes`). New `tests/test_check_entity_system.py` (32 tests; 4 pilot-specific tests made generic; all pass). New `.github/workflows/validate-entity-system.yml` (CI). Live: gate vacuously CONFORMANT. D-004 clean. 118a/b/c authorship gates remain CONFORMANT. Follow-on: T8 legacy ID reconciliation. |
| [CR-CATALOG-STRUCT-05](CR-CATALOG-STRUCT-05.md) | Stakeholders Catalog Adoption | Proposed | First adoption CR for Stakeholders. Scaffold repo with no entities yet. Adoption = pre-wire the standard before any entity is added: vendored regenerator + gate + schema; new `catalog-conformance.yml` workflow; `CATALOG.yaml` + `TEMPLATE_VERSION` committed. Phase 2 content population follows the standard's per-entity subtree layout automatically. |
