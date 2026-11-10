# PCI Security Standards Council (PCI SSC) — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-pci-security-standards-council-ek8khf`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://www.pcisecuritystandards.org`
- `sibling-record`: `dea:regulation-pci-dss (dea-catalog-regulations)`

## 2. Typified corpus rows


### Class `payment-card-standards-body` — Payment-card standards body

Role class `sh-role:payment-card-standards-body` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0070 | 2 (sibling-record anchor) | official-website | https://www.pcisecuritystandards.org | https://www.pcisecuritystandards.org |


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-pci-dss (dea-catalog-regulations) | — | the contractual-regime record whose standard this council maintains (the asserted `publishes` edge target) |
| 3 (public record) | standards-library | PCI SSC document library (PCI DSS, PA-SSC, 3DS Core and related standards) | https://www.pcisecuritystandards.org/document_library | the published standards this body maintains — the `publishes` capacity in artifact form |

## 4. Asserted edges carried by the record

- `publishes` -> `dea:regulation-pci-dss` — PCI SSC maintains and publishes the PCI Data Security Standard (the sibling record describes the standard as the global contractual regime, not jurisdiction-bound — publishes, not enforces); evidence channel 2.

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

