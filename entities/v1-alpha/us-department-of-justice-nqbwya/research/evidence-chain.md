# US Department of Justice (DOJ) — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-us-department-of-justice-nqbwya`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://www.justice.gov`
- `sibling-record`: `dea:regulation-us-dtsa (dea-catalog-regulations)`

## 2. Typified corpus rows


### Class `justice-enforcement-authority` — Justice/enforcement authority

Role class `sh-role:justice-enforcement-authority` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0062 | 2 (sibling-record anchor) | official-website | https://www.justice.gov | https://www.justice.gov |

### Class `trade-secret-enforcement-authority` — Trade-secret enforcement authority

Role class `sh-role:trade-secret-enforcement-authority` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0069 | 3 (public record) | official-website | https://www.justice.gov | https://www.justice.gov |

Dual-capacity note: the DOJ appears in two role classes — the justice/enforcement class (E-0062) and the trade-secret enforcement class (E-0069, the DTSA capacity). Both rows are carried in this record's chain.


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-us-dtsa (dea-catalog-regulations) | — | the regime record this authority enforces (the asserted `enforces` edge target) |
| 3 (public record) | official-website | US DOJ — federal law enforcement, including DTSA civil actions | https://www.justice.gov | resolves the authority and its enforcement capacities (federal criminal and civil enforcement) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-us-dtsa` — The DOJ enforces the Defend Trade Secrets Act (2016); the sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- The justice/enforcement capacity has no regulation-specific edge yet: no general federal-enforcement regime record exists in the regulations catalog; the capacity is recorded honestly with the URL evidence row only.
