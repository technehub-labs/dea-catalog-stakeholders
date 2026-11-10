# Trade-secret enforcement authority — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-trade-secret-enforcement-authority-2374nw`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:trade-secret-enforcement-authority` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `sibling-record`: `dea:regulation-eu-trade-secrets-directive (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 4 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0066 | EU member-state trade-secret authorities | trade-secrets; eu | 2 (sibling-record anchor) | — | engaged instance (this enterprise) |
| E-0067 | Court of Justice of the European Union (CJEU) | eu | 3 (public record) | https://curia.europa.eu | market instance (no enterprise engagement) |
| E-0068 | Ministry of Economy, Trade and Industry (METI, Japan) | jp | 3 (public record) | https://www.meti.go.jp | market instance (no enterprise engagement) |
| E-0069 | US Department of Justice (trade-secret capacity, DTSA) | us | 3 (public record) | https://www.justice.gov | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0066.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-eu-trade-secrets-directive (dea-catalog-regulations) | — | the regime record this class enforces (the asserted `enforces` edge target) |
| 3 (public record) | court-of-justice | Court of Justice of the European Union (CJEU) — interpretation of Directive (EU) 2016/943 | https://curia.europa.eu | the EU-level court whose preliminary rulings bind member-state enforcement of the directive |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-eu-trade-secrets-directive` — Trade-secret protection statutes are enforced by national and supranational authorities and courts; for this enterprise the engaged instance is the EU member-state competent authorities and courts under Directive (EU) 2016/943 as transposed. The sibling record anchors the directive (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- No single official website: the class has no URL (row E-0066 notes this honestly); the CJEU site evidences the EU-level interpretation layer only.
- E-0066 (EU member-state trade-secret authorities): no single `stakeholder_url` exists for this instance — Collective canonical record (member-state competent authorities and courts); no single URL exists for the class - regime anchor at EUR-Lex. Role typified by the CJEU/METI/DOJ URL evidence rows..
