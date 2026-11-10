# US HHS Office for Civil Rights (OCR) — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-hhs-office-for-civil-rights-hf7e8x`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://www.hhs.gov/ocr`
- `sibling-record`: `dea:regulation-us-hipaa (dea-catalog-regulations)`

## 2. Typified corpus rows

### Class `health-data-regulation-authority` — Health-data regulation authority

Role class `sh-role:health-data-regulation-authority` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0055 | 2 (sibling-record anchor) | official-website | https://www.hhs.gov/ocr | https://www.hhs.gov/ocr |


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-hipaa (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |
| 3 (public record) | official-website | HHS OCR — HIPAA Privacy, Security, and Breach Notification enforcement | https://www.hhs.gov/ocr | resolves the authority and its enforcement capacity over protected health information |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-hipaa` — HHS OCR enforces the HIPAA Privacy and Security Rules; the sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

