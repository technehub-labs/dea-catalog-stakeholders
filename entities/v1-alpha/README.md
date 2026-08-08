# v1-alpha Catalog Entries

This directory will hold Stakeholder catalog entries once Phase 2 content population begins.

Each entry should be a YAML file following the schema in `../../schemas/entity.schema.json`. Example shape:

```yaml
id: dea:stakeholder-acme-corp
type: Stakeholder
name: ACME Corporation
stakeholder_type: customer
relationship_direction: inbound
description: ACME Corp is a customer of the enterprise's logistics platform.
version: 1.0.0
```

See [DEA Metamodel stakeholder schema](https://github.com/technehub-labs/dea-metamodel/blob/main/schemas/entities/stakeholder.json) for the full canonical definition.