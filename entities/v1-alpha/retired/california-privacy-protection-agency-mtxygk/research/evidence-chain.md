# California Privacy Protection Agency (CPPA) and California Attorney General — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-california-privacy-protection-agency-mtxygk`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://cppa.ca.gov`
- `sibling-record`: `dea:regulation-us-ccpa-cpra (dea-catalog-regulations)`

## 2. Typified corpus rows


### Class `state-consumer-privacy-regulator` — State consumer-privacy regulator

Role class `sh-role:state-consumer-privacy-regulator` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0048 | 2 (sibling-record anchor) | official-website | https://cppa.ca.gov | https://cppa.ca.gov |

Dual-authority record: the CPPA (rulemaking/enforcement under the CPRA) and the California AG (CCPA enforcement) are recorded together as the enforcing set for the CCPA/CPRA regime, per the STRUCT-14 tranche decision.


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-ccpa-cpra (dea-catalog-regulations) | — | the regime record these authorities enforce (the asserted `enforces` edge target) |
| 3 (public record) | official-website | California Attorney General — CCPA enforcement and guidance | https://oag.ca.gov/privacy | the AG's CCPA portal (enforcement guidance, regulations history under the CCPA) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-ccpa-cpra` — The CPPA (rulemaking, enforcement) and the California Attorney General (civil enforcement) enforce the CCPA/CPRA; the sibling record anchors the jurisdiction (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.

