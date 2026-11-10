# Payment-card standards body — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-payment-card-standards-body-bxqwjh`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:payment-card-standards-body` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `sibling-record`: `dea:regulation-pci-dss (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 3 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0070 | PCI Security Standards Council (PCI SSC) | payment-card | 2 (sibling-record anchor) | https://www.pcisecuritystandards.org | engaged instance (this enterprise) |
| E-0071 | Accredited Standards Committee X9 (ANSI financial services) | us | 3 (public record) | https://x9.org | market instance (no enterprise engagement) |
| E-0072 | EMVCo (jointly owned by the card networks) | global | 3 (public record) | https://www.emvco.com | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0070.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-pci-dss (dea-catalog-regulations) | — | the contractual-regime record whose standard this council maintains (the asserted `publishes` edge target) |
| 3 (public record) | standards-library | PCI SSC document library (PCI DSS, PA-SSC, 3DS Core and related standards) | https://www.pcisecuritystandards.org/document_library | the published standards this body maintains — the `publishes` capacity in artifact form |

## 4. Asserted edges carried by the record

- `publishes` -> `dea:regulation-pci-dss` — The standards body maintains and publishes the payment-card security standard; for this enterprise the engaged instance is the PCI Security Standards Council, whose PCI DSS is the global contractual regime, not jurisdiction-bound (publishes, not enforces). The sibling record anchors the standard (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

