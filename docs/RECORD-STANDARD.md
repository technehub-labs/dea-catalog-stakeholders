# Record Documentation Standard (CR-CATALOG-STRUCT-13)

Every canonical Stakeholder record must satisfy this standard.
`scripts/check_schema.py` and the ES/IDM gates enforce the
machine-checkable subset; steward review enforces the rest. The admission
contract (evidence channels, id minting, relationship policy) is in
[`FOUNDATIONS.md`](FOUNDATIONS.md).

## 1. Record file

One record per subtree: `entities/v1-alpha/<slug>-<hash6>/stakeholders-stakeholder-<slug>-<hash6>.yaml`.
Obligations beyond the schema (metamodel v1.0.0 projection, closed world):

1. `name` is the real name as consumers know it (organisation, authority,
   or capacity — e.g. `GitHub, Inc.`, `UK Information Commissioner's Office`,
   `Emmanuel A. Otchere (governing board capacity)`).
2. `description` states what the party is and the capacity in which it
   engages the enterprise — not a restatement of the name. Where a dual
   capacity exists (Actor vs Stakeholder), the description says which
   capacity this record carries (Actors boundary, FOUNDATIONS §1).
3. `stakeholder_type` is the metamodel enum value for the relationship
   class; never widened locally.
4. `lifecycle_status: active` on canonical admission (CST-004);
   `version: 1.0.0`.
5. `external_references` cites at least one resolvable system/identifier
   pair (FOUNDATIONS §2 evidence channels).
6. Relationship instances (when asserted) carry `direction:
   source-to-target`, a registered `relationship_type` (ES-003), and a
   `rationale` naming the evidence. No instance `id` field (FOUNDATIONS §4).
   Asserted only against live canonical targets; when the natural target
   does not exist yet, assert nothing and carry an explicit `Deferred:`
   note in the record README instead.

## 2. YAML conventions

- Dates single-quoted so they stay strings.
- Apostrophes escaped (`''`) in single-quoted prose; double quotes when the
  prose contains a colon.
- No `stakeholders:`-prefixed string anywhere except the record's own `id`
  and references to live record ids (IDM-003 treats every such string as a
  reference).

## 3. Per-record README

Each record subtree carries a `README.md` (IDM-007) with sections:

```markdown
# <Name>

> <the record's description, verbatim>

## Identity

id, stakeholder_type, version, lifecycle_status — one line each.

## Evidence

The external_references pairs, each with the channel (FOUNDATIONS §2) and
what it verifies. Any Deferred: notes.

## Relationships

The asserted typed edges (type → target → rationale), or "None asserted."
plus the Deferred: note when an edge awaits a target record.

## Provenance

Admission CR + PR, admission date, authorship-bearing actor.
```

## 4. What steward review adds

The gates cannot judge whether evidence *justifies* admission — only that
it resolves. Steward review (the PR review) checks: the evidence channel is
the right one, the description states the capacity honestly, deferred edges
are genuinely blocked on a missing target (not on missing homework), and
the candidate register stays truthful about what is *not* yet admissible.

## 5. Research dossier (CR-CATALOG-STRUCT-15)

Every canonical record subtree also carries a `research/` dossier — the
exhaustive evidence chain, the stakeholder profile, and the cross-catalog
correlations — per [`EVIDENCE-STANDARD.md`](EVIDENCE-STANDARD.md). The record
YAML and this standard's §1..§4 obligations are unchanged; the dossier is
documentation-grade and never widens the record.
