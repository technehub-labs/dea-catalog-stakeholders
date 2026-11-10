# v1-alpha Catalog Entries

This directory will hold authoritative `v1-alpha` Stakeholder catalog entries for the TechNeHub Labs Digital Enterprise Architecture (DEA) ecosystem.

Stakeholders are stored in a **flat layout** under this directory (one subtree per record), per the org-wide entity-storage-layout spec ratified in `dea-metaframework/docs/entity-storage-layout.md`, §3. Each record is a `<slug>-<hash6>` subtree containing the record YAML and a per-record README. The catalog is not ECF-coordinated: Stakeholder entries do not decompose into a 7x7 ECF matrix.

> **Phase 2 population.** The population contract is `docs/FOUNDATIONS.md` (evidence channels, id minting, relationship policy) and `docs/RECORD-STANDARD.md` (per-record obligations); candidates live in `catalog-research/CANDIDATE-REGISTER.md`. The CI early-exit in `ci.yml` self-adjusts: it validates records as soon as any exist.

---

## 📁 Directory Topology & Naming Conventions

```
v1-alpha/
├── <slug>-<hash6>/                                        # record subtree
│   ├── stakeholders-stakeholder-<slug>-<hash6>.yaml       # the record (id with ':' -> '-')
│   ├── README.md                                          # per-record documentation (IDM-007)
│   └── research/                                          # evidence-chain dossier (CR-CATALOG-STRUCT-15)
│       ├── README.md                                      # dossier index + provenance (CST-009)
│       ├── evidence-chain.md                              # every evidence row (E-#### ids, channels, URLs)
│       ├── stakeholder-profile.md                         # definition, goals, activities, engagement
│       └── correlations.md                                # related entities across the catalog fleet
├── retired/                                               # top-level state grouping (CR-CATALOG-STRUCT-17)
│   ├── README.md                                          # the grouping's index
│   └── <slug>-<hash6>/                                    # fully-retired record subtrees, same shape
└── README.md
```
The `research/` dossier is the exhaustive-evidence layer: its contract is
`docs/EVIDENCE-STANDARD.md` (CR-CATALOG-STRUCT-15), and the role classes its
rows typify live in `classifications/stakeholder-role-taxonomy.md`. Dossier
files are documentation-grade Markdown — the record YAML remains the only
normative artifact, and the dossier never widens a record or an edge. Since CR-CATALOG-STRUCT-16 the
canonical records are role classes — the reusable, jurisdiction-free capacities
of the role taxonomy; the named parties of the first tranche are retired
(`lifecycle_status: retired`), grouped under `retired/` per
CR-CATALOG-STRUCT-17, and their dossiers remain as the
engaged-instance history.

Subdirectory names are the id's `<slug>-<hash6>` body (IDM-005: dir = id minus the `stakeholders:stakeholder-` prefix; file = the full id with `:` normalized to `-`, lowercased). The 6-character hash is assigned **once at admission** per `dea-metaframework/docs/id-system.md` §2.5 (first 4 bytes of the record file's SHA-256, big-endian, 6 base-31 digits over `abcdefghjkmnpqrstuvwxyz23456789`) and is **never recomputed** against live content afterwards — IDM-004 checks well-formedness and uniqueness only, and the CST suite does not recompute hashes either.

---

## 📄 Entity Anatomy: Stakeholders

Per the DEA Metamodel (v1.0.0), `Stakeholder` is the entity class this catalog instantiates; records validate against the closed-world projection in `schemas/entity.schema.json`.

### Canonical id forms

| Level | id form |
| :--- | :--- |
| L1: Stakeholder | `stakeholders:stakeholder-<slug>-<hash6>` |

### Canonical YAML Shape (metamodel v1.0.0 projection; see `schemas/fixtures/example-valid.yaml`)

```yaml
# id pattern: stakeholders:stakeholder-<slug>-<hash6>
id: stakeholders:stakeholder-example-slug-a2b4c6
type: Stakeholder
name: Example Stakeholder
description: 'What the party is and the capacity in which it engages the enterprise.'
version: '1.0.0'
lifecycle_status: active
stakeholder_type: supplier      # customer|partner|supplier|regulator|investor|community|board
external_references:
  - system: <verifiable-system>
    identifier: <resolvable-id>
relationships:                   # optional; registered types only (ES-003)
  - source_id: stakeholders:stakeholder-example-slug-a2b4c6
    target_id: dea:regulation-example            # cross-catalog target
    relationship_type: enforces
    direction: source-to-target
    rationale: 'Why this edge is justified.'
```

Cross-catalog references use the referencing catalog's own id form (e.g. the regulations catalog's `dea:regulation-*` ids).

---

## 📈 Population Snapshot

Live counts are owned by the generated `CATALOG.yaml` (`catalog.counts` and the per-entity `entities[]` entries) — hardcoded numbers here rot, so this section deliberately carries none. The candidate-side truth (what is *not* yet admissible) lives in `catalog-research/CANDIDATE-REGISTER.md`.

---

## 🛡 Governance & Conformance Gates

This catalog is protected by an automated CI pipeline with the following gates. All gates run on every PR via `.github/workflows/catalog-conformance.yml` (and adjacent workflows):

1. **`validate`** (workflow `ci.yml`, job `validate-stakeholder-entries`)
   Runs `scripts/check_schema.py` on every PR once records exist: asserts the schema stays a faithful projection of the metamodel Stakeholder schema, exercises the fixture pair, and validates every record file against `schemas/entity.schema.json` (offline, via the vendored relationship schema).
   *Why it matters:* Catches malformed records and schema drift before they reach the catalog. Self-skipping while the tree is empty.

2. **Catalog Conformance Suite** (CST, layout-agnostic, from `dea-metaframework/tools/conformance_test_catalog_structure.py`, checkout pinned `v2.6.0`)
   Runs the 16-test CST suite that checks id-pattern conformance and the flat-layout invariants (it does **not** recompute content hashes — see §2.5 of the id-system spec).
   *Why it matters:* Enforces the org-wide id-system contract across the catalog fleet.

3. **ID System Gate** (`scripts/check_id_system.py`)
   Runs IDM-001..007 (catalog-wide) plus IDM-008 (PR-scoped coherence via `id-system-coherence-report.md` artifact).
   *Why it matters:* Catches id drift between branches and the canonical baseline before merge.

4. **Authorship Cardinal Rule gate** (`scripts/check_authorship.py`, `validate-authorship.yml`)
   Enforces AUT-001..003 over the registered authorship-bearing fields (both CR metadata shapes).
   *Why it matters:* Keeps agent/tool names out of authorship fields (CR-BP-118 as propagated by CR-CATALOG-STRUCT-06).

5. **Entity System gate** (`scripts/check_entity_system.py`, `validate-entity-system.yml`)
   Runs the 5-rule umbrella gate (ES-001..005) under `--strict`, data-driven from `reconciliation/entity-system-registry.yaml`.
   *Why it matters:* Keeps the id/relationship/lifecycle contract honest once records exist. Vacuously CONFORMANT while the tree is empty.

6. **Allocation pin** (`validate-allocation.yml`) + **pointer gate** (`scripts/check_pointer.py`)
   Validates `metamodel-pointer.yaml` against the OpenDEAM root model (`dea-architecture-framework@v0.9.0`), and asserts pointer/allocation consistency locally.
   *Why it matters:* Detects entity-mapping drift between this catalog and the root model.

6b. **Record schema projection gate** (`scripts/check_schema.py`, also in `catalog-conformance.yml`)
   Projection-constant check (metamodel v1.0.0 faithfulness) + fixture behavior + per-record validation.
   *Why it matters:* The catalogue schema must never become a second source of truth.

7. **Catalog index + test suite** (`scripts/regenerate_catalog.py --check`, `scripts/check_catalog_index.py`, `pytest tests/`)
   Keeps `CATALOG.yaml` truthful (counts, states, paths) and runs the gate unit tests on every PR.

Not yet adopted in this repo (tracked for Phase 2 with the first admissions, do not assume they exist): a register-audit gate (`check_register_audit.py`), a CR-metadata gate (`check_cr_metadata.py`), an allocation-matrix CI job, `reconciliation/inventory.yaml`, and baseline snapshots. This catalog is not ECF-coordinated; no ECF conformance consumer applies (unlike the capabilities/processes catalogs).

---

## 🔄 Lifecycle, Reconciliation, and Baselines

This directory is the source of truth for the repository's reconciliation artifacts under `reconciliation/`:

* **`CATALOG.yaml`** (repo root): Automatically refreshed to reflect the current state of all entities in this tree. The CI gate runs `scripts/regenerate_catalog.py --check` and fails on any drift. Currently emits an empty (zero-entity) catalog.
* **`reconciliation/authorship-fields.yaml`**: The authorship-field registry the AUT gate reads (CR-level to extend).
* **`reconciliation/entity-system-registry.yaml`**: The entity-system registry the ES gate reads (canonical id form, relationships, lifecycle, per-type gates, exceptions).
* **`reconciliation/migration-id-map.yaml`**: Declared by the entity-system registry for the legacy `dea:*` sweep; created when the first admission or the T8 follow-on needs it.

When modifying this directory, contributors must run `scripts/regenerate_catalog.py` and re-run the gates (`check_id_system.py --strict`, the CST suite, `pytest tests/`) so the committed tree stays consistent. CI enforces this.

---

## 🔗 Cross-Repo References

This catalog is one of seven in the DEA ecosystem. Records reference other catalogs using the org-wide id form `<namespace>:<level>-...-<hash6>`:

| Namespace | Catalog | Status |
| --- | --- | --- |
| `actors:` | `technehub-labs/dea-catalog-actors` | This catalog's sibling |
| `orgunits:` | `technehub-labs/dea-catalog-organizational-units` | Wave 3 scaffold |
| `objects:` | `technehub-labs/dea-catalog-business-objects` | Wave 3 scaffold |
| `stakeholders:` | `technehub-labs/dea-catalog-stakeholders` | Wave 3 scaffold (this catalog) |
| `capabilities:` | `technehub-labs/dea-catalog-business-capabilities` | Populated (see its `CATALOG.yaml`) |
| `services:` | `technehub-labs/dea-catalog-business-services` | Populated (see its `CATALOG.yaml`) |
| `processes:` | `technehub-labs/dea-catalog-business-processes` | Populated (see its `CATALOG.yaml`) |

(Per-catalog counts live in each repo's generated `CATALOG.yaml` — hardcoded numbers here rot; the values this table previously carried were already stale.)

This catalog has secondary references to the `dea:catalog-*` self-identity records, which remain in the legacy form on purpose.

---

## 🚀 Contributor Workflow

To add the first record to this catalog:

1. **Identify the party and evidence.** Choose the canonical name and slug, and gather evidence per `docs/FOUNDATIONS.md` §2 (unresolvable parties go to `catalog-research/CANDIDATE-REGISTER.md`, not into this tree).
2. **File a Change Request (CR).** Create or reference an existing CR in `change-requests/` (e.g., `CR-<NS>-NN-<title>.md`); the carrier CR must reference every admitted id (IDM-008).
3. **Create the record + README.** Place the file at the correct flat-layout subtree (`docs/RECORD-STANDARD.md` has the shape and the README template); mint the hash6 per `docs/FOUNDATIONS.md` §3.
4. **Run Local Conformance.** Execute `scripts/check_schema.py`, `scripts/check_pointer.py`, `scripts/check_id_system.py --strict`, `scripts/check_entity_system.py --strict`, and the pytest suite locally. The CI pipeline runs the same gates on every PR (the `ci.yml` early-exit self-adjusts once records exist — nothing to drop).
5. **Regenerate Reconciliation Artifacts.** Run `scripts/regenerate_catalog.py --schema catalog-index-schema/catalog-index-schema.json` as the FINAL commit action, then `--check` must pass.
6. **Submit PR.** Link the PR to the CR. The CI pipeline enforces the gates described above.

For deeper metamodel definitions and the canonical id-system / entity-storage-layout specs, refer to:

* `technehub-labs/dea-metaframework` → `docs/id-system.md` (org-wide id contract)
* `technehub-labs/dea-metaframework` → `docs/entity-storage-layout.md` (§3 flat-layout-for-non-ECF)
* `technehub-labs/dea-metaframework` → `docs/conformance.md` (CST suite reference)
* `schemas/entity.schema.json` (record schema)
