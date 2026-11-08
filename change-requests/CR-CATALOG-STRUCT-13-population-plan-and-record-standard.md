# CR-CATALOG-STRUCT-13: Population Plan, Record Standard, and Relationship-Type Registration

**Status**: Proposed
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-08
**Trigger**: Owner directive 2026-11-08 to advance the catalog to an active, well-enriched state (continuation of CR-CATALOG-STRUCT-12's Phase 2 precondition). The catalog had no population contract: no evidence standard, no id-minting convention beyond the id-system spec, no stated Actors boundary, no registered relationship types (ES-003's empty `canonical_types` would fail every first record that asserts an edge), and no candidate register recording what is honestly *not* admissible yet. Authored agent-side on eaojnr's behalf; agency recorded here per the CR-BP-118 cardinal rule.
**Carrier**: this file
**Lands against**: `main` @ `2518c6b` (post CR-CATALOG-STRUCT-12, PR #15)
**Depends on**: CR-CATALOG-STRUCT-12

## 1. Problem

The first admission would have landed into an uncontracted catalog:

1. **No evidence standard** — nothing defined what org-verifiable evidence admits a Stakeholder record, so admission would have been ad-hoc per record.
2. **No registered relationship types** — ES-003 `canonical_types: []` rejects every typed edge; the metamodel enum has no stakeholders-specific registration anywhere.
3. **No Actors boundary statement** — the metamodel description says internal performers are Actors, not Stakeholders, but nothing in this repo operationalized the boundary (including the dual-capacity case: the owner as performer vs the owner as governing board).
4. **No candidate register** — parties that cannot be evidence-matched today (customers, partners) would be either silently absent or invented; the honest-zero discipline used by the capabilities candidate closure (CR-DEA-BC-68) needs a home here.
5. **Entities README drift** — the structural README contradicted the id-system spec on hash assignment ("content-addressed … changes its hash" vs §2.5's assign-once-at-admission, never-recomputed contract), claimed the CST suite checks hash correctness (it does not), documented a stale YAML shape (`definition`/`related_records` fields the schema does not define), instructed contributors to "drop the early-exit" (the count check self-adjusts), and carried a rot-prone hardcoded snapshot table.

## 2. Changes

| Area | Change |
|---|---|
| `docs/FOUNDATIONS.md` | New: the population contract — scope and Actors boundary (incl. the dual-capacity rule), the three evidence channels (in-repo primary / sibling-record anchor / public record) in authority order, the id-minting convention (hash6 assigned once at admission per id-system §2.5; storage per IDM-005/007), the relationship policy (registered types only, `direction: source-to-target`, rationale required, no instance ids — any `stakeholders:`-prefixed string is an IDM-003 reference), the lifecycle/admission workflow, and the docs/gates map. |
| `docs/RECORD-STANDARD.md` | New: per-record obligations (name/description honesty, `stakeholder_type` never widened locally, `lifecycle_status: active` + `version: 1.0.0` at admission, resolvable `external_references`, typed-edge requirements incl. the `Deferred:` note rule), YAML conventions, and the per-record README template. |
| `catalog-research/CANDIDATE-REGISTER.md` | New: the honest candidate register — C-001 the missing enterprise anchor node (blocks supplier-side outward edges), C-002 customers (honest zero), C-003 partners (honest zero), C-004 non-owner investors (honest zero); closure discipline per the CR-DEA-BC-68 precedent. |
| `reconciliation/entity-system-registry.yaml` | ES-003 `canonical_types` registered ahead of the tranche: `enforces` and `publishes` (both from the metamodel relationship-instance enum, targets `dea:regulation-*`), each with a `source_types: [Stakeholder]` constraint. |
| `entities/v1-alpha/README.md` | Truth sweep: layout tree corrected to the IDM-005 forms (`<slug>-<hash6>/` subtree, hyphen-form file name, per-record README); hash paragraph aligned to id-system §2.5 (assign-once, never recomputed; IDM-004 and the CST suite do not recompute); YAML shape replaced with the real schema projection; gate list gains `check_pointer.py`/`check_schema.py` and moves the allocation row to v0.9.0; contributor workflow de-rotted (evidence-first step, IDM-008 step, no "drop the early-exit"); hardcoded snapshot table removed in favor of the CATALOG.yaml pointer. |

## 3. NOT-List

- **No entity records.** The first tranche is CR-CATALOG-STRUCT-14; this CR contracts its admission, it does not admit.
- **No new relationship types invented.** `enforces`/`publishes` are metamodel enum members; the vocabulary authority is the metamodel schema.
- **No schema changes.** The STRUCT-12 projection is frozen by `check_schema.py`'s constants; this CR adds no fields.
- **No registry widening beyond the two types actually used by the tranche.** Types are registered when asserted, not speculatively.
- **No stakeholder_type enum changes.** The 7-value metamodel set stands.

## 4. Acceptance criteria

- AC-01 `docs/FOUNDATIONS.md`, `docs/RECORD-STANDARD.md`, and `catalog-research/CANDIDATE-REGISTER.md` exist and cross-link; the candidate register carries C-001..C-004 with verdicts.
- AC-02 `reconciliation/entity-system-registry.yaml` ES-003 `canonical_types` == `[enforces, publishes]` with `source_types: [Stakeholder]` constraints; `check_entity_system.py --strict` exits 0.
- AC-03 `grep -n "content-addressed\|changes its hash" entities/v1-alpha/README.md` returns no live-contract contradictions; the hash paragraph states assign-once-at-admission and cites id-system §2.5.
- AC-04 `grep -n "v0.2.1" entities/v1-alpha/README.md` returns nothing; the allocation row cites v0.9.0.
- AC-05 All local gates pass: regenerator `--check`, `check_catalog_index --strict`, `check_pointer`, `check_schema`, `check_id_system --strict`, `check_authorship --strict`, `check_entity_system --strict`, `pytest tests/ -q` (62).
- AC-06 CHANGELOG `[Unreleased]` entry; CR index row added; `CATALOG.yaml` regenerated as the final commit action (`open_change_requests` arithmetic unchanged at 1: STRUCT-12 closes at the next landing's discipline pass, this carrier stays `Proposed` until then).

## 5. Follow-ons (named, not in this CR)

- CR-CATALOG-STRUCT-14: first canonical tranche (11 records: platform supplier, OSS community, governing-board capacity, eight regulators one-to-one with the regulations catalog's eight active records — the EU trade-secrets directive gets its own member-state-authorities record rather than overloading the EU DPAs).
- Enterprise-anchor decision (candidate C-001): where the enterprise-as-party node lives (Actors vs a dedicated record), unblocking the deferred supplier/community edges.
- Root-model lifecycle flip and governance-register refresh, after the tranche lands.
