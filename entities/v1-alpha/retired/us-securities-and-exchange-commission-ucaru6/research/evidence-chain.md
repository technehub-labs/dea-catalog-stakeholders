# US Securities and Exchange Commission (SEC) — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-us-securities-and-exchange-commission-ucaru6`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://www.sec.gov`
- `sibling-record`: `dea:regulation-us-securities-insider-trading (dea-catalog-regulations)`

## 2. Typified corpus rows

### Class `securities-and-markets-regulator` — Securities and markets regulator

Role class `sh-role:securities-and-markets-regulator` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0058 | 2 (sibling-record anchor) | official-website | https://www.sec.gov | https://www.sec.gov |


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-securities-insider-trading (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |
| 3 (public record) | official-website | SEC — enforcement, rulemaking, and EDGAR disclosure systems | https://www.sec.gov | resolves the authority and its capacities (rulemaking, examinations, enforcement, disclosure operations) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-securities-insider-trading` — The SEC enforces US securities-law insider-trading prohibitions; the sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

