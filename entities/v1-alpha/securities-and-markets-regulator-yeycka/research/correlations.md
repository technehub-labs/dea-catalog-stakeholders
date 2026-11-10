# Securities and markets regulator — correlations to related entities

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

## Regulations

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `dea:regulation-us-securities-insider-trading` (Us Securities Insider Trading) | state: canonical | Asserted edge: `enforces` (rationale in the record: the sibling record anchors the insider-trading regime). | Channel 2: the regulations catalog's record (live sibling target). |

## Capabilities

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `capabilities:capability-financial-stewardship-c7xtfk` (Financial Stewardship) | state: canonical | The enterprise's financial-stewardship capability operates under the securities regime this authority enforces. | Channel 2: the enforced regulation record. |
| `capabilities:capability-portfolio-and-investment-management-m4kw72` (Portfolio And Investment Management) | state: canonical | Investment decisions are made under the insider-trading regime's constraints (MNPI handling). | Channel 2: the enforced regulation record anchors the regime. |
| `capabilities:capability-risk-management-h9uxdw` (Risk Management) | state: canonical | Regulatory risk from securities regimes is managed by this enterprise capability. | Channel 2: the enforced regulation record. |

## Services

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `services:service-regulatory-change-tracking-fdjj9j` (Regulatory Change Tracking) | state: canonical | The enterprise service that tracks this authority's rulemaking and enforcement posture. | Channel 2: the regime this role class enforces (sibling regulation record); the enterprise service operationalizes its duties. |
| `services:service-regulatory-examination-management-vavpcu` (Regulatory Examination Management) | state: canonical | The enterprise service that would manage any examination interaction with this authority. | Channel 2: the regime this role class enforces (sibling regulation record); the enterprise service operationalizes its duties. |
| `services:service-whistleblower-report-intake-vnznfh` (Whistleblower Report Intake) | state: canonical | The enterprise's internal report-intake service; its outputs can interface with the SEC whistleblower program. | Channel 2: the regime this role class enforces (sibling regulation record); the enterprise service operationalizes its duties. |

## Deferred

- None.
