# Securities and markets regulator — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-securities-and-markets-regulator-yeycka`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:securities-and-markets-regulator` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `sibling-record`: `dea:regulation-us-securities-insider-trading (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 4 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0058 | US Securities and Exchange Commission (SEC) | securities; us | 2 (sibling-record anchor) | https://www.sec.gov | engaged instance (this enterprise) |
| E-0059 | Australian Securities and Investments Commission (ASIC) | au | 3 (public record) | https://asic.gov.au | market instance (no enterprise engagement) |
| E-0060 | Financial Conduct Authority (FCA, UK) | uk | 3 (public record) | https://www.fca.org.uk | market instance (no enterprise engagement) |
| E-0061 | Ontario Securities Commission (OSC, Canada) | ca-on | 3 (public record) | https://www.osc.ca | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0058.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-securities-insider-trading (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |
| 3 (public record) | official-website | SEC — enforcement, rulemaking, and EDGAR disclosure systems | https://www.sec.gov | resolves the authority and its capacities (rulemaking, examinations, enforcement, disclosure operations) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-securities-insider-trading` — The authority enforces securities and markets law; for this enterprise the engaged instance is the US Securities and Exchange Commission, enforcer of the insider-trading prohibitions anchored in the regulations catalog. The sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

