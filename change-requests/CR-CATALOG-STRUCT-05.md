# CR-CATALOG-STRUCT-05: Stakeholders Catalog Adoption

**Status**: Merged (PR #3)
**Layer**: L1 (Stakeholder Catalog)
**Owner**: TechNeHub Labs
**Depends on**: CR-CATALOG-STRUCT-01, CR-CATALOG-STRUCT-06a+06b
**Adoption pattern**: STRUCT-05 (scaffold adoption; pre-wire the standard before any entity is added)

## What this CR is

Adopt the catalog repository standard (CR-CATALOG-STRUCT-01) in `dea-catalog-stakeholders`. The Stakeholders catalog is the fourth and final L1 catalog to adopt; it is the only one in scaffold state (no entities yet, content population planned for Phase 2).

The migration follows STRUCT-04's pattern (per-entity subtrees + vendored regenerator + `catalog-conformance.yml` workflow + `CATALOG.yaml` + `TEMPLATE_VERSION`) but is the smallest of the four adoption CRs because there are no entities to move. Adoption here is "pre-wire the standard before any entity is added": the scaffolding is now in place so that the first entity addition lands directly into a conformant subtree.

## Decisions locked during planning

- **Q1 (scaffold adoption)**: pre-wire the standard. Adopt the full standard now; first entity addition follows the per-entity subtree layout automatically.
- **Q2 (cross-cutting dirs)**: create `change-requests/`, `classifications/`, `contributions/` with `.gitkeep` placeholders so the gate's `cross_cutting.*` paths pass under `--strict`.

## What changes

### Files added

- `scripts/regenerate_catalog.py` (vendored).
- `scripts/check_catalog_index.py` (vendored).
- `catalog-index-schema/catalog-index-schema.json` (vendored).
- `CATALOG.yaml` (generated; 0 entities).
- `TEMPLATE_VERSION` (`0.1.0`).
- `change-requests/`, `classifications/`, `contributions/` (each with `.gitkeep`).
- `.github/workflows/catalog-conformance.yml` (regenerator + gate + conformance suite).
- `change-requests/CR-CATALOG-STRUCT-05.md` (this file).
- `01_plan/pr-struct-05.md` (PR body, untracked).

### Files kept

- `entities/v1-alpha/README.md` (placeholder; Phase 2 content population begins here).
- `schemas/entity.schema.json` (Stakeholder entry schema; Phase 2 validates against this).
- `.github/workflows/ci.yml` (entry validator; fires when Phase 2 adds entities).
- `.github/workflows/validate-allocation.yml` (OpenDEAM allocation pin; orthogonal).
- `metamodel-pointer.yaml` (augmented with top-level metadata; nested blocks unchanged).
- `README.md`, `LICENSE`, `NOTICE`.

### `metamodel-pointer.yaml` changes

Same additive-plus-relocate pattern as STRUCT-02 (process), STRUCT-03 (BC), and STRUCT-04 (DBSF):

- New top-level metadata block (`id`, `name`, `abbreviation`, `owner`, `license`, `repository`, `homepage`, `metamodel_version`, `conformance_status`).
- Existing root-level `description:` rewritten from the entity-class description to the catalog-level description.
- Entity-class description moved to `metamodel.description:` where the OpenDEAM allocation validator already reads it.

The nested `metamodel:`, `catalog:`, `links:` blocks are unchanged.

### Phase 2 path (out of scope, documented for the next contributor)

When Phase 2 begins (first Stakeholder entity addition), the standard's per-entity subtree layout applies directly: each new entity lands at `entities/v1-alpha/<id>/<id>.yaml` with optional `research/`, `candidates/`, `retired/` state directories. The schema at `schemas/entity.schema.json` validates against the canonical metamodel schema at `technehub-labs/dea-metamodel/schemas/entities/stakeholder.json`.

Two known Phase 2 readiness items in `.github/workflows/ci.yml`:

1. The `dsanders11/json-schema-validate-action@v2.1.0` step uses `entities/**/*.yaml` as a multiline glob. When entities land, that glob will also pick up files under `research/`, `candidates/`, `retired/` state directories, which would fail validation (these are research artifacts, not entries). The BC catalog hit the same issue in STRUCT-03b and swapped the action for an inline Python validator (build explicit canonical-files list, then `pip install jsonschema pyyaml` + Python `Draft7Validator`). Stakeholders will need the same swap in the PR that adds the first entity.
2. The validation early-exit (skip when no entities exist) is fine while the catalog is empty; remove the early-exit once Phase 2 begins.

These are noted in the CR for future readers; they do not block STRUCT-05.

## Verification

Local run, all green:

- `python scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json` returns `OK: CATALOG.yaml is current`.
- `python scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json` returns `OK: CATALOG.yaml validates (0 entities)`.
- `python .metaframework/tools/conformance_test_catalog_structure.py --catalog-root . --template-root .metaframework/tools/catalog-repo-template --strict` returns `OK: 16 CST(s) passed (0 warning(s))`.
- Dash sweep on new prose: clean.
- Secret scan: 0.
- `git diff --check`: clean.

## Conformance after this PR

- 0 entities in per-entity subtrees (scaffold state; Phase 2 begins content population).
- 0 per-entity research files, 0 candidates, 0 retired.
- CATALOG.yaml: 0 entities, Stakeholders catalog, Apache-2.0, owner TechNeHub Labs.
- 16/16 CSTs pass under `--strict` (vacuously on entity-bearing CSTs; structurally on infrastructure CSTs).
- Cross-repo adoption tracker flips Stakeholders row from `not-started` to `conforming`.

## Sequencing

After this merges:

| Slice | Status |
|---|---|
| STRUCT-01 | Merged |
| STRUCT-06a | Merged |
| STRUCT-06b | Merged |
| STRUCT-02 (process catalog) | Merged (PR #21) |
| STRUCT-03 (BC catalog) | Merged (PR #44 + #45) |
| STRUCT-04 (DBSF catalog) | Merged (PR #6) |
| STRUCT-05 (stakeholders catalog) | This PR |
| STRUCT-07 (cross-repo consumer) | unblocked (four conformant adopters) |
