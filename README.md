# Stakeholders

> External or affected parties whose relationship with the enterprise is engaged in or affected by enterprise processes.

**Layer:** L1 · **Entity:** `SH` · **Metamodel:** [v0.2.1](https://github.com/technehub-labs/dea-metamodel) (OpenDEAM v0.2.1, ADR-0002)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=SH)

## Status

This is a **scaffold** repository — created during the Process taxonomy rollout. Content population is planned for a subsequent phase.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:entity-stakeholder` |
| Class Alias | `SH` |
| Layer | L1 |
| Metamodel Version | v0.2.1 |

## Catalog Structure

```
dea-catalog-stakeholders/
├── metamodel-pointer.yaml     ← entity mapping (do not edit manually)
├── CATALOG.yaml               ← generated catalog index (do not edit manually)
├── entities/
│   └── v1-alpha/              ← catalog entries go here (Phase 2)
│       └── README.md
├── schemas/                   ← JSON Schema for this entity type
│   └── entity.schema.json
├── catalog-index-schema/      ← schema for the generated CATALOG.yaml
├── change-requests/           ← CR governance (see README.md therein)
├── classifications/           ← classification artifacts (Phase 2)
├── contributions/             ← contribution queue (Phase 2)
├── reconciliation/            ← gate registries (authorship, entity system)
├── scripts/                   ← vendored regenerator + conformance gates
└── .github/workflows/         ← validate, catalog-conformance, validate-allocation,
                                 validate-authorship, validate-entity-system
```

`ci.yml` validates entries against `schemas/entity.schema.json` (early-exit while the entities tree is empty); the other four workflows run the conformance gates on every push and PR to `main`.

## Boundary

**Stakeholders are NOT internal performers.** Internal performers (employees, teams, systems, AI agents) are modeled separately as **Actors** in [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors).

The same person can be a Stakeholder of one process (e.g. performance review) and an Actor of another (e.g. payroll processing).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the [DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.