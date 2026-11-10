# Justice/enforcement authority — correlations to related entities

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
| `dea:regulation-us-dtsa` (Us Dtsa) | state: canonical | Asserted edge: `enforces` (rationale in the record: the sibling record anchors the DTSA regime). | Channel 2: the regulations catalog's DTSA record (live sibling target). |

## Capabilities

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `capabilities:capability-legal-matter-management-zzbd2u` (Legal Matter Management) | state: canonical | The enterprise capability that would carry any matter involving this authority (subpoenas, investigations, DTSA actions). | Channel 2: the DTSA regime record; the authority's enforcement role. |
| `capabilities:capability-risk-management-h9uxdw` (Risk Management) | state: canonical | Federal-enforcement risk is managed by this enterprise capability. | Channel 2: the DTSA record + the authority's general enforcement posture. |
| `capabilities:capability-information-management-6vjgdh` (Information Management) | state: canonical | The DTSA protects the enterprise's undisclosed information; this capability governs the publish/withhold boundary. | Channel 1: LICENSE/NOTICE publishing decisions; channel 2: the DTSA regime record. |

## Processes

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `processes:process-ge-operate-hxxyc9` (Audit Policy Compliance) | state: canonical | Audit Policy Compliance: the enterprise's audit process keeps the enterprise defensible under federal regimes. | Channel 2: the DTSA record. |

## Services

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `services:service-legal-matter-management-rxb77c` (Legal Matter Management) | state: canonical | The enterprise service for matters involving this authority. | Channel 2: the regime this role class enforces (sibling regulation record); the enterprise service operationalizes its duties. |

## Deferred

- The justice/enforcement capacity has no regulation-specific edge yet: no general federal-enforcement regime record exists in the regulations catalog; the capacity is recorded honestly with the URL evidence row only.
