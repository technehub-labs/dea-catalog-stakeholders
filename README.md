# Stakeholders

> External or affected parties whose relationship with the enterprise is engaged in or affected by enterprise processes.

**Layer:** L1 · **Entity:** `SH` · **Metamodel:** [v1.0.0](https://github.com/technehub-labs/dea-metamodel) (OpenDEAM v0.9.0 allocation pin, CR-CATALOG-STRUCT-12)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=SH)

## Status

**Active and populated** (2026-11-08): 11 canonical records — the platform supplier, the OSS community, the governing-board capacity, and 8 regulators anchored one-to-one to the regulations catalog's active records. The population contract is [`docs/FOUNDATIONS.md`](./docs/FOUNDATIONS.md); the per-record standard is [`docs/RECORD-STANDARD.md`](./docs/RECORD-STANDARD.md); candidates awaiting resolvable evidence live in [`catalog-research/CANDIDATE-REGISTER.md`](./catalog-research/CANDIDATE-REGISTER.md).

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:entity-stakeholder` |
| Class Alias | `SH` |
| Layer | L1 |
| Metamodel Version | 1.0.0 (schema); OpenDEAM allocation pin v0.9.0 |

## Catalog Structure

```
dea-catalog-stakeholders/
├── metamodel-pointer.yaml     ← entity allocation declaration (validated, do not hand-edit)
├── CATALOG.yaml               ← generated catalog index (do not edit manually)
├── entities/
│   └── v1-alpha/              ← one subtree per record (record YAML + README)
├── docs/                      ← FOUNDATIONS (population contract) + RECORD-STANDARD
├── catalog-research/          ← candidate register
├── schemas/                   ← entity schema (metamodel projection) + relationship schema + fixtures
├── catalog-index-schema/      ← schema for the generated CATALOG.yaml
├── change-requests/           ← CR governance (see README.md therein)
├── classifications/           ← classification artifacts (Phase 2)
├── contributions/             ← contribution queue (Phase 2)
├── reconciliation/            ← gate registries (authorship, entity system)
├── scripts/                   ← vendored regenerator + conformance gates (pointer, schema, id, authorship, entity system)
└── .github/workflows/         ← validate, catalog-conformance, validate-allocation,
                                 validate-authorship, validate-entity-system
```

`ci.yml` validates entries against `schemas/entity.schema.json` (early-exit while the entities tree is empty); the other four workflows run the conformance gates on every push and PR to `main`.

## Boundary

**Stakeholders are NOT internal performers.** Internal performers (employees, teams, systems, AI agents) are modeled separately as **Actors** in [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors).

The same person can be a Stakeholder of one process (e.g. performance review) and an Actor of another (e.g. payroll processing).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the [DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.