# Justice/enforcement authority — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-justice-enforcement-authority-hkuap7`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:justice-enforcement-authority` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `sibling-record`: `dea:regulation-us-dtsa (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 4 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0062 | US Department of Justice (DOJ) | trade-secrets; us | 2 (sibling-record anchor) | https://www.justice.gov | engaged instance (this enterprise) |
| E-0063 | Australian Attorney-General's Department | au | 3 (public record) | https://www.ag.gov.au | market instance (no enterprise engagement) |
| E-0064 | Department of Justice (Canada) | ca | 3 (public record) | https://www.justice.gc.ca | market instance (no enterprise engagement) |
| E-0065 | UK Ministry of Justice | uk | 3 (public record) | https://www.gov.uk/government/organisations/ministry-of-justice | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0062.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-dtsa (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |
| 3 (public record) | official-website | US DOJ — federal law enforcement, including DTSA civil actions | https://www.justice.gov | resolves the authority and its enforcement capacities (federal criminal and civil enforcement) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-dtsa` — The justice department prosecutes civil and criminal violations of national statute; for this enterprise the engaged instance is the US Department of Justice, federal enforcement authority for the Defend Trade Secrets Act (2016). The sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- The justice/enforcement capacity has no regulation-specific edge yet: no general federal-enforcement regime record exists in the regulations catalog; the capacity is recorded honestly with the URL evidence row only.

