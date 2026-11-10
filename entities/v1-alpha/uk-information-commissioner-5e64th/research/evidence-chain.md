# UK Information Commissioner's Office (ICO) — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-uk-information-commissioner-5e64th`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://ico.org.uk`
- `sibling-record`: `dea:regulation-uk-gdpr (dea-catalog-regulations)`

## 2. Typified corpus rows


### Class `data-protection-supervisory-authority` — Data-protection supervisory authority

Role class `sh-role:data-protection-supervisory-authority` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0034 | 2 (sibling-record anchor) | official-website | https://ico.org.uk | https://ico.org.uk |


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-uk-gdpr (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-uk-gdpr` — The ICO is the UK GDPR's supervisory authority; the sibling record anchors the jurisdiction (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

