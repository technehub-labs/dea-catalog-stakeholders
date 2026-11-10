# Source-control and CI platform supplier — correlations to related entities

> Documentation-grade correlations (per `docs/EVIDENCE-STANDARD.md` §5): how
> this role class relates to the enterprise's regulation, capability, process,
> service, and actor records across the catalog fleet. These are NOT ES-003
> relationship instances — the record's asserted edges are only those in its
> YAML (`enforces`/`publishes`); everything here is evidence-basis documentation.
> Every target id resolves to a live record in its sibling catalog (verified
> 2026-11-10); target lifecycle states are noted where not canonical.
> CR-CATALOG-STRUCT-16: correlations are capacity-level — this record is the role
> class; the engaged instances are named in the evidence chain, and the tables
> carry over from the retired party record's dossier (same live targets).

## Capabilities

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `capabilities:capability-technology-enablement-y6nkws` (Technology Enablement) | state: canonical | The enterprise capability the platform directly enables: source control, CI, and delivery tooling run on the stakeholder's platform. | Channel 1 (in-repo): `.github/workflows/*` execute on Actions; the fleet's repositories are hosted on the platform. |
| `capabilities:capability-change-management-hukdeq` (Change Management) | state: canonical | The enterprise's change discipline (CR -> PR -> gates -> merge) executes through the platform's PR machinery. | Channel 1: the landing discipline recorded across `change-requests/` is operated via pull requests on the platform. |
| `capabilities:capability-supplier-management-d6fuj4` (Supplier Management) | state: canonical | The enterprise capability that governs this supplier relationship. | This record is the supplier-side anchor of that capability (record asserts the supplier capacity). |

## Services

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `services:service-supplier-risk-scoring-yghbp7` (Supplier Risk Scoring) | state: canonical | The enterprise service that would score this platform supplier in supplier-risk terms. | Channel 1: supplier-side risk surfaces (hosting, CI, delivery) are all concentrated on this role class. |
| `services:service-supplier-onboarding-hwebjb` (Supplier Onboarding) | state: canonical | The enterprise service that onboards supplier relationships like this one. | The supplier relationship predates the catalog (fleet-hosted evidence); the service records the onboarding side. |

## Actors

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `actors:actor-architecture-ci-pipeline-cz8zmp` (Architecture Ci Pipeline) | state: canonical | The enterprise's CI actor executes on this role class's hosted runners. | Channel 1: the actor's workflows are the `.github/workflows/*.yml` files that run on the platform. |

## Deferred

- `serves` / `supplies` edges onto the enterprise await the C-001 enterprise-anchor decision (candidate register); the record asserts no edges today per RECORD-STANDARD §1.6.
