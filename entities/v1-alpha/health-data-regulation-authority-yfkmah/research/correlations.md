# Health-data regulation authority — correlations to related entities

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
| `dea:regulation-us-hipaa` (Us Hipaa) | state: canonical | Asserted edge: `enforces` (rationale in the record: the sibling record anchors the HIPAA regime). | Channel 2: the regulations catalog's HIPAA record (live sibling target). |

## Capabilities

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `capabilities:capability-regulation-management-gya4d8` (Regulation Management) | state: canonical | The enterprise capability that tracks and manages the regulatory regimes this role class enforces. | Channel 2: the sibling regulation record anchors the regime this role class enforces. |
| `capabilities:capability-privacy-and-consent-management-h3mw69` (Privacy And Consent Management) | state: canonical | The enterprise capability that operates personal-data processing under the regime this role class supervises. | Channel 2: the enforced regulation record (regime) + the enterprise's public processing surfaces (channel 1). |

## Processes

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `processes:process-ge-operate-hxxyc9` (Audit Policy Compliance) | state: canonical | Audit Policy Compliance: the enterprise's compliance-audit process operates against the regimes this role class enforces. | Channel 2: the enforced regulation record; the audit process is its operational counterpart. |
| `processes:process-ge-operate-hs7wf3` (Operate Governance Oversight) | state: canonical | Operate Governance Oversight: the oversight loop through which the enterprise stays answerable to this regulator. | Channel 2: the sibling regulation record anchors the accountability regime. |

## Services

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `services:service-privacy-impact-assessment-95q6uz` (Privacy Impact Assessment) | state: canonical | Risk analyses the Security Rule requires for PHI systems. | Channel 2: the regime this role class enforces (sibling regulation record); the enterprise service operationalizes its duties. |
| `services:service-personal-data-breach-notification-6xtujc` (Personal Data Breach Notification) | state: canonical | The breach-notification duty this authority enforces under the Breach Notification Rule. | Channel 2: the regime this role class enforces (sibling regulation record); the enterprise service operationalizes its duties. |
| `services:service-privacy-notice-management-c8ecps` (Privacy Notice Management) | state: canonical | Notice-of-privacy-practices publication and maintenance (the Privacy Rule's NPP duty). | Channel 2: the regime this role class enforces (sibling regulation record); the enterprise service operationalizes its duties. |

## Deferred

- None.
