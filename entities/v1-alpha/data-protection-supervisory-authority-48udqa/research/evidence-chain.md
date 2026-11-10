# Data-protection supervisory authority — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-data-protection-supervisory-authority-48udqa`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:data-protection-supervisory-authority` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `sibling-record`: `dea:regulation-uk-gdpr (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 11 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0034 | UK Information Commissioner's Office (ICO) | data-protection; uk | 2 (sibling-record anchor) | https://ico.org.uk | engaged instance (this enterprise) |
| E-0035 | Cyberspace Administration of China (CAC) | data-protection; cn | 3 (public record) | http://www.cac.gov.cn | market instance (no enterprise engagement) |
| E-0036 | National Data Protection Authority of Brazil (ANPD) | data-protection; br | 3 (public record) | https://www.gov.br/anpd | market instance (no enterprise engagement) |
| E-0037 | Office of the Australian Information Commissioner (OAIC) | data-protection; au | 3 (public record) | https://www.oaic.gov.au | market instance (no enterprise engagement) |
| E-0038 | Office of the Privacy Commissioner (New Zealand) | data-protection; nz | 3 (public record) | https://www.privacy.org.nz | market instance (no enterprise engagement) |
| E-0039 | Office of the Privacy Commissioner for Personal Data (Hong Kong) | data-protection; hk | 3 (public record) | https://www.pcpd.org.hk | market instance (no enterprise engagement) |
| E-0040 | Office of the Privacy Commissioner of Canada (OPC) | data-protection; ca | 3 (public record) | https://www.priv.gc.ca | market instance (no enterprise engagement) |
| E-0041 | Personal Data Protection Commission (Singapore, PDPC) | data-protection; sg | 3 (public record) | https://www.pdpc.gov.sg | market instance (no enterprise engagement) |
| E-0042 | Personal Information Protection Commission (Japan, PPC) | data-protection; jp | 3 (public record) | https://www.ppc.go.jp | market instance (no enterprise engagement) |
| E-0043 | Personal Information Protection Commission (Republic of Korea, PIPC) | data-protection; kr | 3 (public record) | https://www.pipc.go.kr | market instance (no enterprise engagement) |
| E-0044 | Swiss Federal Data Protection and Information Commissioner (FDPIC) | data-protection; ch | 3 (public record) | https://www.edoeb.admin.ch | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0034.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-uk-gdpr (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-uk-gdpr` — The jurisdiction's supervisory authority enforces its national data-protection regime; for this enterprise the engaged instance is the UK Information Commissioner's Office, supervisory authority for the UK GDPR. The sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

