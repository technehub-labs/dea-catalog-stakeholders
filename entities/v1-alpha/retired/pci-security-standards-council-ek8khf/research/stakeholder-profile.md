# PCI Security Standards Council (PCI SSC) — stakeholder profile

> Defining the stakeholder: what the party is, its goals, what it does, and how
> it engages the enterprise. Per `docs/EVIDENCE-STANDARD.md`; the record's
> description remains the normative one-liner — this profile expands it.

## Definition

The PCI Security Standards Council is the global standards body (founded by the major card networks) that develops and maintains the Payment Card Industry Data Security Standard and its companion standards (payment application security, PIN transaction security, 3-D Secure). The council governs the standards' content and their adoption program (assessor qualifications); acceptance enforcement is contractual — the card networks enforce against merchants and processors. The record carries `publishes` (not `enforces`) per the STRUCT-14 tranche decision.

The record's normative description (verbatim): *The PCI Security Standards Council, the industry body founded by the card networks that maintains and publishes the PCI Data Security Standard. The council governs the standard's content; compliance is enforced contractually through the card networks' acceptance regimes, under which the enterprise's payment-card processing engagement runs.*

## Mandate and goals

- Secure the payment ecosystem: protect payment-account data wherever it is accepted, processed, stored, or transmitted.
- Maintain open, globally applicable security standards that keep pace with threats.
- Drive adoption through qualified-assessor programs and training rather than direct enforcement.

## What they do

- Develops and versions PCI DSS and companion standards (public document library, ~3-year major release cycles historically).
- Operates qualification programs for assessors (QSAs, ASVs, CPAs) and PIN assessors.
- Publishes guidance, blogs, and lifecycle documents for the payment community.
- Manages the standards' change process (request-for-change intake from the industry).

## Engagement with the enterprise

The enterprise treats PCI DSS as its contractual payment-security regime (the sibling regulation record); the council's published standards are what the enterprise's security capabilities adopt. The card networks — not the council — would enforce against the enterprise, hence `publishes`.

## Role classes (typified)

- `sh-role:payment-card-standards-body` — Payment-card standards body (stakeholder_type `regulator`); 1 corpus row(s) in this record's chain
