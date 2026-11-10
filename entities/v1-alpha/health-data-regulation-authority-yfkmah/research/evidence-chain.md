# Health-data regulation authority — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-health-data-regulation-authority-yfkmah`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:health-data-regulation-authority` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `sibling-record`: `dea:regulation-us-hipaa (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 3 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0055 | US HHS Office for Civil Rights (OCR) | health-data; us | 2 (sibling-record anchor) | https://www.hhs.gov/ocr | engaged instance (this enterprise) |
| E-0056 | Health Information and Quality Authority (HIQA, Ireland) | ie | 3 (public record) | https://www.hiqa.ie | market instance (no enterprise engagement) |
| E-0057 | Information and Privacy Commissioner of Ontario (health-information capacity) | ca-on | 3 (public record) | https://www.ipc.on.ca | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0055.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-hipaa (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |
| 3 (public record) | official-website | HHS OCR — HIPAA Privacy, Security, and Breach Notification enforcement | https://www.hhs.gov/ocr | resolves the authority and its enforcement capacity over protected health information |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-hipaa` — The authority regulates the processing of health-related personal data; for this enterprise the engaged instance is the US HHS Office for Civil Rights, enforcer of the HIPAA Privacy and Security Rules. The sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

