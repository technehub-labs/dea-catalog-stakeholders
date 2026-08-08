# Stakeholders

> External or affected parties whose relationship with the enterprise is engaged in or affected by enterprise processes.

**Layer:** L1 · **Entity:** `SH` · **Metamodel:** [v3.0.0-alpha](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=Stakeholder)

## Status

This is a **scaffold** repository — created during the Process taxonomy rollout. Content population is planned for a subsequent phase.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:entity-stakeholder` |
| Class Alias | `SH` |
| Layer | L1 |
| Metamodel Version | v3.0.0-alpha |

## Catalog Structure

```
dea-catalog-stakeholders/
├── metamodel-pointer.yaml   ← entity mapping (do not edit manually)
├── entities/
│   └── v1-alpha/          ← catalog entries go here
│       └── README.md
├── schemas/                ← JSON Schema for this entity type
│   └── entity.schema.json
└── .github/
    └── workflows/
        └── ci.yml         ← validates entries against schema
```

## Boundary

**Stakeholders are NOT internal performers.** Internal performers (employees, teams, systems, AI agents) are modeled separately as **Actors** in [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors).

The same person can be a Stakeholder of one process (e.g. performance review) and an Actor of another (e.g. payroll processing).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the [DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.