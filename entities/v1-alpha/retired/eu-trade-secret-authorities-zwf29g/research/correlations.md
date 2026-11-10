# EU member-state trade-secret competent authorities — correlations to related entities

> Documentation-grade correlations (per `docs/EVIDENCE-STANDARD.md` §5): how
> this stakeholder relates to the enterprise's regulation, capability, process,
> service, and actor records across the catalog fleet. These are NOT ES-003
> relationship instances — the record's asserted edges are only those in its
> YAML (`enforces`/`publishes`); everything here is evidence-basis documentation.
> Every target id resolves to a live record in its sibling catalog (verified
> 2026-11-10); target lifecycle states are noted where not canonical.

## Regulations

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `dea:regulation-eu-trade-secrets-directive` (Eu Trade Secrets Directive) | state: canonical | Asserted edge: `enforces` (rationale in the record: the sibling record anchors the directive). | Channel 2: the regulations catalog's trade-secrets record (live sibling target). |

## Capabilities

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `capabilities:capability-legal-matter-management-zzbd2u` (Legal Matter Management) | state: canonical | The enterprise capability that manages legal matters, including protecting undisclosed information under this regime. | Channel 2: the trade-secrets regulation sibling record. |
| `capabilities:capability-information-management-6vjgdh` (Information Management) | state: canonical | The enterprise capability governing what is published (Apache-2.0 corpus) vs what is held undisclosed (the regime's protected class). | Channel 1: LICENSE/NOTICE publish decisions + channel 2: the regime record. |

## Services

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `services:service-legal-matter-management-rxb77c` (Legal Matter Management) | state: canonical | The enterprise service that would carry any misappropriation action under this regime. | Channel 2: the regime record defines the cause of action. |

## Deferred

- No single official website: the class has no URL (row E-0066 notes this honestly); the CJEU site evidences the EU-level interpretation layer only.
