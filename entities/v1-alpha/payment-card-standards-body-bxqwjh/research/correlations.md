# Payment-card standards body — correlations to related entities

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
| `dea:regulation-pci-dss` (Pci Dss) | state: canonical | Asserted edge: `publishes` (rationale in the record: the council governs the standard's content while the card networks enforce acceptance). | Channel 2: the regulations catalog's PCI DSS record (live sibling target). |

## Capabilities

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `capabilities:capability-security-management-wmzc7c` (Security Management) | state: canonical | The enterprise's security capability adopts the standards this council publishes (PCI DSS-family controls). | Channel 2: the PCI DSS regime record anchors the regime the council maintains. |
| `capabilities:capability-regulation-management-gya4d8` (Regulation Management) | state: canonical | The standards this body publishes are managed as a contractual regime by the enterprise's regulation-management capability. | Channel 2: the PCI DSS sibling record (described there as the global contractual regime). |

## Processes

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `processes:process-ge-design-kpsj5b` (Design Policies and Controls) | state: canonical | Design Policies and Controls: PCI DSS-derived control design is an instance of this enterprise process. | Channel 2: the regime record defines the control objectives the design process consumes. |

## Services

| target | state | nature of the correlation | basis |
|---|---|---|---|
| `services:service-pci-segmentation-monitoring-cuw7q6` (Pci Segmentation Monitoring) | state: canonical | The enterprise service that evidences the segmentation controls PCI DSS requires. | Channel 2: the regime record; the service operationalizes its control objectives. |

## Deferred

- None.
