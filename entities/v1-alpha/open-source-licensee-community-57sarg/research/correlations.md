# Open-source licensee community — correlations to related entities

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
| `capabilities:capability-idea-management-86dckf` (Idea Management) | state: canonical | Community feedback and contributions feed the enterprise's idea pipeline. | Channel 1: the corpus is published for public consumption; its issue trackers are the intake surface. |
| `capabilities:capability-technology-enablement-y6nkws` (Technology Enablement) | state: canonical | The community consumes the enterprise's technology through the same platform surfaces the enterprise builds on. | Channel 1 + 3: the org and repository surfaces are the community's engagement surface. |

## Services

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `services:service-software-license-management-9r46ga` (Software License Management) | state: canonical | The enterprise service that manages the license instruments (Apache-2.0 LICENSE + NOTICE) constituting this community. | Channel 1: LICENSE and NOTICE in every published repo, including this one. |

## Deferred

- Edges onto the enterprise (the community's relationship to the anchor node) await C-001.
- Named downstream licensees are intentionally NOT recorded: the community is a collective capacity; specific adopters become candidates only if and when verifiable engagement evidence exists.
