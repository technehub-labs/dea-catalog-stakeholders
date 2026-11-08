# CR-CATALOG-STRUCT-12: Foundation Modernization (OpenDEAM v0.9.0 Pin, Metamodel v1.0.0 Schema, Regenerator Re-Vendor, Record Gates)

**Status**: Merged (PR #15)
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-08
**Trigger**: Owner directive 2026-11-08 to advance the catalog to an active, well-enriched state. The foundation layer had drifted a full OpenDEAM generation behind the org: pointer and allocation validator pinned OpenDEAM v0.2.1 (root model now at v0.9.0; the two newer catalog stand-ups — information-assets, information-models — pin v0.8.0/v0.9.0), the repo-local record schema had drifted from the metamodel v1.0.0 Stakeholder schema (carried a metamodel-nonexistent `relationship_direction` field and an object-form `external_identifiers` where the metamodel defines array-form `external_references`; carried no `lifecycle_status`), and the vendored regenerator carried the infer_state hyphen-form defect (fixed upstream in dea-metaframework PR #58 but untagged — v2.6.0 predates it), which would have misclassified every future canonical record as a candidate. This CR is the Phase 2 precondition: the first admission lands into current, honest gates. Authored agent-side on eaojnr's behalf; agency recorded here per the CR-BP-118 cardinal rule.
**Carrier**: this file
**Lands against**: `main` @ `ab9fa70`
**Depends on**: none

## 1. Problem

Four foundation-layer defects, all invisible while the catalog is empty, all load-bearing the day the first record lands:

1. **Stale allocation pin.** `metamodel-pointer.yaml` was generated from OpenDEAM v0.2.1 (ADR-0002 era) and `validate-allocation.yml` pinned `@v0.2.1`. The org's root model has moved to v0.9.0 (OpenDEAM v0.9.0, tagged 2026-11-01); the Stakeholder allocation is unchanged (same `entity_id` / `SH` / `L1` / `L1-external-parties` at v0.9.0), so the pin moves without any allocation change. The pointer also carried scaffolding-era shape: nested `catalog.status: scaffold`, top-level `conformance_status: draft`, and `metamodel_version: "^0.2.1"` — `CATALOG.yaml` accordingly rendered `status: draft`, `version: 0.0.0`, `metamodel_version: ^0.2.1`.
2. **Schema drift from the metamodel.** `schemas/entity.schema.json` was a Phase-1 sketch: it allowed `relationship_direction` (a field the metamodel Stakeholder schema does not define) and `external_identifiers` as an object map, omitted the metamodel's `lifecycle_status` and array-form `external_references`, left the record id pattern at the generic metamodel form, and validated records against a *remote* metamodel relationship schema (offline-unvalidatable). Its `$ref` target also could not resolve offline.
3. **Vendored regenerator defect (bug family).** `scripts/regenerate_catalog.py` (and `check_catalog_index.py`'s stale entropy-alphabet regex) predated two upstream fixes: CR-ECF-011's explicit 31-symbol alphabet (`[abcdefghjkmnpqrstuvwxyz23456789]`) and PR #58's infer_state dual-form canonical-filename lookup. With this repo's IDM-005 layout, the canonical file is the *hyphen-form* name (`stakeholders-stakeholder-<slug>-<hash6>.yaml`); the colon-only lookup would have marked every future canonical subtree as `candidate` — the same defect that misreported 29 capabilities records (CR-DEA-BC-61).
4. **No record-validation gate wired locally.** `ci.yml` deferred record validation to an unproven third-party action and `catalog-conformance.yml` never validated the schema projection; neither asserted that the local schema stays a faithful projection of the metamodel schema. The dea-catalog-information-models stand-up established the house pattern (projection-constant check + fixture behavior + per-record validation, offline via a vendored relationship schema).

## 2. Changes

| Area | Change |
|---|---|
| `metamodel-pointer.yaml` | Rewritten to the information-models pointer form: top-level identity keys (`id`, `name`, `abbreviation: SH`, `version: 0.1.0`, `status: active`, `metamodel_version: 1.0.0`, `owner`, `description`), the `metamodel:` allocation block pinned `v0.9.0` (allocation values unchanged, now with the Actors-boundary sentence in the description), and `links:`. Drops the scaffolding-era `license`/`repository`/`homepage`/`conformance_status` keys and the nested `catalog:` block (the current regenerator derives `repository` from the git origin). |
| `.github/workflows/validate-allocation.yml` | `model_ref` and reusable-workflow pin `v0.2.1` → `v0.9.0`. |
| `schemas/entity.schema.json` | Rewritten as a metamodel-faithful projection (metamodel_version 1.0.0): metamodel's exact required set (`id`, `name`, `type`, `version`, `stakeholder_type`); `lifecycle_status` and array-form `external_references` added; repo-only `relationship_direction` and object-form `external_identifiers` removed; record id narrowed to the org-wide form `^stakeholders:stakeholder-[a-z0-9-]+-[a-z2-9]{6}$`; `additionalProperties: false`; relationships `$ref` the locally vendored schema. |
| `schemas/relationship-instance.schema.json` | New: vendored byte-copy of dea-metamodel v1.0.0 `schemas/relationships/relationship-instance.json` (120-type normative enum; required `source_id`/`target_id`/`relationship_type`), so record validation is offline-reproducible. |
| `schemas/fixtures/example-valid.yaml`, `example-invalid.yaml` | New: fixture pair proving the validator accepts the normative shape and rejects enum/pattern violations (the invalid fixture violates both `stakeholder_type` and the id form). |
| `scripts/regenerate_catalog.py` | Re-vendored from `dea-metaframework` `origin/main` (carries CR-ECF-011 + the #58 infer_state dual-form fix). Vendored-path adaptations: usage strings and `DEFAULT_SCHEMA_PATH` point at this repo's layout (`scripts/`, `catalog-index-schema/catalog-index-schema.json`). |
| `scripts/check_catalog_index.py` | Re-vendored from `origin/main` (entropy-alphabet regex sync; the only drift was that regex). |
| `scripts/check_pointer.py` | New: local pointer-consistency gate (identity fields, allocation constants for this repo: `dea:entity-stakeholder` / `SH` / `L1`, pin `v0.9.0`, links triple). Adapted from the information-models gate. |
| `scripts/check_schema.py` | New: projection gate — asserts the local schema mirrors the metamodel constants (type const, required set, id pattern, both normative enums, relationships `$ref`), exercises the fixture pair, and validates every record under `entities/v1-alpha/**` offline. Adapted from the information-models gate. |
| `.github/workflows/catalog-conformance.yml` | Two new steps after the index gate: `check_pointer.py` and `check_schema.py`. Header comment updated to v0.9.0. |
| `.github/workflows/ci.yml` | The deferred `dsanders11/json-schema-validate-action` step is replaced by the house gate (`scripts/check_schema.py`) under the same early-exit skip; gains `setup-python@v5` + pinned `pyyaml`/`jsonschema` installs (the action was self-contained; the script needs the interpreter — the action never proved it parses YAML records). |
| `tests/test_regenerate_catalog.py` | New: 4 regression tests pinning the re-vendor — `DEFAULT_SCHEMA_PATH` at the vendored location, `entity_id_from_subtree` reading the id from the hyphen-named file, `infer_state` returning `canonical` (and `retired` for a retired lifecycle) with the hyphen-form `canonical_path`, with the colon-form filename asserted absent. |
| `change-requests/CR-CATALOG-STRUCT-11-ci-hygiene-pinning-and-timeouts.md` | Status closes to `Merged (PR #13)` per the standing landing discipline. |
| `CATALOG.yaml` | Regenerated as the final commit action: `status` draft → `active`, `version` 0.0.0 → `0.1.0`, `metamodel_version` `^0.2.1` → `1.0.0`. `open_change_requests` stays 1 at this PR's regen: STRUCT-11 closes to `Merged (PR #13)` in the same change, but this carrier's own `Proposed` status takes over the open count (the standing discipline closes a CR in a later landing); it reaches 0 at the next landing. |

## 3. NOT-List

- **No entity records.** Population is CR-CATALOG-STRUCT-13 (plan) and -14 (first tranche); this CR only modernizes the foundation.
- **No allocation change.** The Stakeholder allocation is identical at v0.2.1 and v0.9.0; only the pin moves. Allocation changes go through the root model (ADR process), not this repo.
- **No metamodel schema edits.** The metamodel's Stakeholder schema is normative; this repo only mirrors (and closes) it locally.
- **No widening of normative enums.** `stakeholder_type` stays the metamodel's 7-value set; new types go through the metamodel first.
- **No registry (ES-003) relationship types registered here.** The tranche CR registers the types it actually uses.
- **Actions SHA-pinning still deferred** (BC-39 §8 precedent, unchanged by this CR).

## 4. Acceptance criteria

- AC-01 `python scripts/check_pointer.py` exits 0 (`OK: pointer present and internally consistent`).
- AC-02 `python scripts/check_schema.py` exits 0 (projection faithful; fixtures behave; N records validate).
- AC-03 `python scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json` exits 0 (committed `CATALOG.yaml` matches regenerator output).
- AC-04 `python scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json` exits 0; `CATALOG.yaml` shows `status: active`, `version: 0.1.0`, `metamodel_version: 1.0.0`.
- AC-05 `python scripts/check_id_system.py --strict` and `check_authorship.py --strict` and `check_entity_system.py --strict` all exit 0; `pytest tests/ -q` passes (58 prior + 4 new = 62).
- AC-06 The infer_state regression: a subtree containing only `stakeholders-stakeholder-<slug>-<hash6>.yaml` is classified `canonical` by the vendored `infer_state` (covered by `tests/test_regenerate_catalog.py`).
- AC-07 `validate-allocation.yml` references `@v0.9.0` / `model_ref: v0.9.0` and the check passes in CI against the root model at that ref.
- AC-08 `grep -Rn "v0.2.1" .github/workflows/ metamodel-pointer.yaml` returns no allocation-pin hits (historical prose in CRs is out of scope).
- AC-09 CHANGELOG `[Unreleased]` entry; CR index row added; STRUCT-11 status closed to `Merged (PR #13)`.

## 5. Follow-ons (named, not in this CR)

- CR-CATALOG-STRUCT-13: population plan (evidence channels, candidate register, id-minting convention, Actors-boundary statement, FOUNDATIONS/RECORD-STANDARD docs, ES-003 canonical relationship types).
- CR-CATALOG-STRUCT-14: first canonical tranche (~10 evidence-gated records).
- Root-model lifecycle flip (Stakeholder `scaffold` → `existing`) in dea-architecture-framework, mirroring the CR-MET-017 precedent, once records are canonical.
- Governance catalog-portfolio register refresh (stakeholders row: counts + steward-note resolution).
