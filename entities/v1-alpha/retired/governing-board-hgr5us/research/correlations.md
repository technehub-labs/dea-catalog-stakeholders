# Emmanuel A. Otchere (governing board) — correlations to related entities

> Documentation-grade correlations (per `docs/EVIDENCE-STANDARD.md` §5): how
> this stakeholder relates to the enterprise's regulation, capability, process,
> service, and actor records across the catalog fleet. These are NOT ES-003
> relationship instances — the record's asserted edges are only those in its
> YAML (`enforces`/`publishes`); everything here is evidence-basis documentation.
> Every target id resolves to a live record in its sibling catalog (verified
> 2026-11-10); target lifecycle states are noted where not canonical.

## Capabilities

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `capabilities:capability-enterprise-governance-uas48u` (Enterprise Governance) | state: canonical | The board's ratification authority IS the enterprise governance capability in its directing sense. | Channel 1: governance CRs record the owner directives; the standing landing discipline is the board's process. |
| `capabilities:capability-strategic-planning-k3rz7a` (Strategic Planning) | state: canonical | Strategy-setting sits with the directing authority. | Channel 1: tranche/population decisions recorded in the CRs are strategic choices about the catalog portfolio. |
| `capabilities:capability-portfolio-and-investment-management-m4kw72` (Portfolio And Investment Management) | state: canonical | The catalog fleet portfolio is owned and prioritized by the board. | Channel 1: the fleet's adoption/advancement CRs are all carried by owner directives. |

## Processes

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `processes:process-ge-build-3p38us` (Establish Governance Bodies) | state: canonical | Establish Governance Bodies: this record is evidence the enterprise's governance body exists and operates. | Channel 1: the board's in-repo ratification trail. |
| `processes:process-ge-operate-hs7wf3` (Operate Governance Oversight) | state: canonical | Operate Governance Oversight: the board operates the oversight the enterprise's governance processes describe. | Channel 1: CR ratification + standing discipline across the fleet. |

## Actors

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `actors:actor-architect-example-rwpe9z` (Architect Example) | state: canonical | Dual-capacity boundary (FOUNDATIONS §1): the same natural person holds performer capacities that live in the Actors catalog; this record carries the governance capacity only. | FOUNDATIONS §1 (the boundary contract itself). |

## Deferred

- `governs` edge onto the enterprise anchor awaits C-001.
- Contact details are deliberately absent from the record (name + capacity only, per the STRUCT-14 tranche decision).
