# State consumer-privacy regulator — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-state-consumer-privacy-regulator-r9h6sp`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:state-consumer-privacy-regulator` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `sibling-record`: `dea:regulation-us-ccpa-cpra (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 4 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0048 | California Privacy Protection Agency (CPPA) and California Attorney General | privacy; us-ca | 2 (sibling-record anchor) | https://cppa.ca.gov | engaged instance (this enterprise) |
| E-0049 | Colorado Attorney General (enforces the Colorado Privacy Act) | us-co | 3 (public record) | https://co.colorado.gov/law | market instance (no enterprise engagement) |
| E-0050 | Texas Attorney General (enforces the Texas Data Privacy and Security Act) | us-tx | 3 (public record) | https://www.texasattorneygeneral.gov | market instance (no enterprise engagement) |
| E-0051 | Virginia Attorney General (enforces the Virginia Consumer Data Protection Act) | us-va | 3 (public record) | https://www.virginia.gov/agencies/office-of-the-attorney-general/ | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0048.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-ccpa-cpra (dea-catalog-regulations) | — | the regime record these authorities enforce (the asserted `enforces` edge target) |
| 3 (public record) | official-website | California Attorney General — CCPA enforcement and guidance | https://oag.ca.gov/privacy | the AG's CCPA portal (enforcement guidance, regulations history under the CCPA) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-ccpa-cpra` — The state authority holds rulemaking and enforcement powers under the subnational consumer-privacy statute; for this enterprise the engaged instance is the California Privacy Protection Agency and the California Attorney General under the CCPA as amended by the CPRA. The sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

