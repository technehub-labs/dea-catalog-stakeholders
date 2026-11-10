# EU member-state trade-secret competent authorities — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-eu-trade-secret-authorities-zwf29g`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016L0943`
- `sibling-record`: `dea:regulation-eu-trade-secrets-directive (dea-catalog-regulations)`

## 2. Typified corpus rows


### Class `trade-secret-enforcement-authority` — Trade-secret enforcement authority

Role class `sh-role:trade-secret-enforcement-authority` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0066 | 2 (sibling-record anchor) | official-website | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016L0943 | *(no single URL — see note)* |

Collective-capacity record with an honest evidence gap: the enforcing set is a class of member-state courts and competent authorities; no single official URL exists for the class (noted in the typified corpus, row E-0066).


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-eu-trade-secrets-directive (dea-catalog-regulations) | — | the regime record this class enforces (the asserted `enforces` edge target) |
| 3 (public record) | court-of-justice | Court of Justice of the European Union (CJEU) — interpretation of Directive (EU) 2016/943 | https://curia.europa.eu | the EU-level court whose preliminary rulings bind member-state enforcement of the directive |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-eu-trade-secrets-directive` — Directive (EU) 2016/943 is enforced by member-state competent authorities and courts once transposed; the sibling record anchors the directive (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- No single official website: the class has no URL (row E-0066 notes this honestly); the CJEU site evidences the EU-level interpretation layer only.
