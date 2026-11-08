# Stakeholders Catalog — Foundations (CR-CATALOG-STRUCT-13)

This document is the population contract for the Stakeholders catalog: what
belongs here, what evidence admits a record, how ids are minted, where the
boundaries run, and which relationship types the catalog asserts. The
machine-checkable subset of the record obligations lives in
[`RECORD-STANDARD.md`](RECORD-STANDARD.md); the candidate register lives at
[`catalog-research/CANDIDATE-REGISTER.md`](../catalog-research/CANDIDATE-REGISTER.md).

## 1. Scope and boundary

A **Stakeholder** is an external or affected party whose relationship with
the enterprise is engaged in or affected by enterprise processes
(`dea:entity-stakeholder`, OpenDEAM v0.9.0, alias `SH`, layer L1,
building block `L1-external-parties`).

**Boundary against Actors** (`technehub-labs/dea-catalog-actors`, namespace
`actors:`): internal performers — employees, teams, systems, AI agents —
are Actors, not Stakeholders. The same natural person can hold both
capacities; this catalog records only the *external/governance* capacity
(e.g. the owner as the enterprise's governing board, not the owner as a
process performer). When a capacity is ambiguous, the Actors catalog wins
for performer roles and this catalog records the residual
governance/influence capacity with the dual capacity stated in the record's
description.

**Enterprise-involving relationships** (supply, regulation, hosting,
governance) are asserted from the Stakeholder record outward. The enterprise
itself has no canonical anchor record yet — see the candidate register
(C-001) — so edges that would terminate on the enterprise are deferred with
an explicit `Deferred:` note in the record README, per the record standard.

## 2. Evidence channels (admission contract)

A record is admitted **canonical** only against org-verifiable evidence.
Three channels, in authority order:

1. **In-repo primary** — an artifact committed in a TechNeHub Labs
   repository: LICENSE/NOTICE files, CI workflow definitions, governance
   CRs, catalog records (e.g. a `dea:regulation-*` record in
   `dea-catalog-regulations`). Evidence cites the repo-relative path (or
   the sibling repo + path).
2. **Sibling-record anchor** — the stakeholder's relationship is anchored
   to a canonical record in another catalog (the regulations catalog is the
   standing example: each regulator record's `enforces`/`publishes` edge
   targets a live `dea:regulation-*` id, which itself carries jurisdiction
   evidence).
3. **Public record** — for parties whose existence and role are matters of
   public record (a national data-protection authority, a standards
   consortium): the record's `external_references` carries the
   system/identifier pair (e.g. system `official-website`, identifier the
   authority's URL) and the description names the capacity.

A record that cannot cite channel 1 or 2, and whose channel-3 evidence does
not resolve to a specific named authority/body, is **not admitted**; it
goes to the candidate register instead (customers and partners are there
today, honestly unresolvable).

## 3. Id minting convention

Canonical id form (IDM-001, org-wide): `stakeholders:stakeholder-<slug>-<hash6>`.

- `<slug>` is lower-kebab (`github-platform`, `uk-information-commissioner`).
- `<hash6>` is assigned **once, at admission**, per
  `dea-metaframework/docs/id-system.md` §2.5: first 4 bytes of the record
  file's SHA-256, big-endian, rendered as 6 base-31 digits over the
  31-symbol alphabet `abcdefghjkmnpqrstuvwxyz23456789`. It is never
  recomputed against live content afterwards; IDM-004 checks form only.
- Storage (IDM-005): subtree `entities/v1-alpha/<slug>-<hash6>/`, record
  file `stakeholders-stakeholder-<slug>-<hash6>.yaml` (the id with `:`
  normalized to `-`), plus a `README.md` in the same subtree (IDM-007).

## 4. Relationship policy

Relationship instances follow the metamodel relationship-instance contract
(vendored at `schemas/relationship-instance.schema.json`; 120-type normative
enum). This catalog registers the types it actually asserts in
`reconciliation/entity-system-registry.yaml` (ES-003 `canonical_types`);
asserting an unregistered type fails the ES gate.

Registered at STRUCT-13, ahead of the first tranche:

| Type | Direction | Use |
|---|---|---|
| `enforces` | Stakeholder → `dea:regulation-*` | A regulator/authority that enforces the regulation. |
| `publishes` | Stakeholder → `dea:regulation-*` | A standards body that maintains/publishes the standard the regulation record anchors. |

Every relationship instance carries `direction: source-to-target` and a
`rationale` naming the evidence. Targets are cross-catalog ids
(`dea:regulation-*` — the regulations catalog's namespace is `dea:`; those
strings pass IDM-003/IDM-006 untouched). Relationship instances carry **no
instance `id`**: any `stakeholders:`-prefixed string inside a record is
treated as a reference by IDM-003 and must resolve to a live record id, so
instance ids are omitted rather than minted.

## 5. Lifecycle and admission workflow

Records carry `lifecycle_status` (metamodel enum: proposed / planned /
active / deprecated / retired; CST-004 requires it on canonical records).
The admission workflow:

1. Candidate recorded in `catalog-research/CANDIDATE-REGISTER.md` (or a
   subtree `research/` dir for heavier investigations).
2. Evidence gathered per §2; a CR drafted (the carrier CR must reference
   every admitted id — IDM-008).
3. Record file + README landed under the §3 storage layout with
   `lifecycle_status: active`, `version: 1.0.0`.
4. Gates: `check_schema.py` (projection + record validation),
   `check_id_system.py --strict`, `check_entity_system.py --strict` (ES-003
   types), CST suite, regenerator `--check` (CATALOG.yaml regenerated as
   the final commit action), IDM-008 PR coherence.
5. Deprecation/retirement follows the metamodel lifecycle vocabulary;
   retired records move under the subtree's `retired/` and are preserved,
   never deleted (BC-09 §8 precedent).

## 6. Docs and gates map

| Artifact | Role |
|---|---|
| `docs/FOUNDATIONS.md` (this file) | Population contract: scope, evidence, ids, relationships, lifecycle. |
| `docs/RECORD-STANDARD.md` | Per-record obligations + README template. |
| `catalog-research/CANDIDATE-REGISTER.md` | Candidates awaiting resolvable evidence; the honest-zero log. |
| `schemas/entity.schema.json` | Closed-world projection of the metamodel v1.0.0 Stakeholder schema. |
| `scripts/check_pointer.py` | Pointer ↔ allocation consistency (OpenDEAM v0.9.0). |
| `scripts/check_schema.py` | Schema-faithfulness projection gate + record validation. |
| `reconciliation/entity-system-registry.yaml` | ES gate config, incl. the §4 canonical relationship types. |
