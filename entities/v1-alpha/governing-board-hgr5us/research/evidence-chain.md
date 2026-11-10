# Emmanuel A. Otchere (governing board) — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-governing-board-hgr5us`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `github-org-ownership`: `eaojnr (owner role, technehub-labs org)`

## 2. Typified corpus rows


### Class `governing-board-authority` — Governing board / directing authority

Role class `sh-role:governing-board-authority` in the taxonomy; stakeholder_type `board`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0131 | 1 (in-repo primary) | github-org-ownership | eaojnr (owner role, technehub-labs org) | https://github.com/eaojnr |
| E-0133 | 3 (public record) | official-website | https://github.com/technehub-labs | https://github.com/technehub-labs |

Single-incumbent capacity: three URL evidence surfaces of the same officeholder (profile, org, repositories); named-party typification is n/a by design for this capacity class.


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 1 (in-repo primary) | governance-cr | change-requests/CR-CATALOG-STRUCT-14-first-canonical-tranche.md (owner directive + tranche decision, 2026-11-08) | — | the board's ratification authority exercised over the catalog's first tranche (recorded in-repo) |
| 3 (public record) | github-profile | eaojnr (owner of the technehub-labs organization) | https://github.com/eaojnr | resolves the natural person holding the governing-board capacity |
| 3 (public record) | github-org-ownership | technehub-labs organization ownership surface | https://github.com/technehub-labs | the ownership surface over which the board's capacity is exercised |

## 4. Asserted edges carried by the record

- None asserted. `governs` edge onto the enterprise anchor awaits C-001.

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- `governs` edge onto the enterprise anchor awaits C-001.
- Contact details are deliberately absent from the record (name + capacity only, per the STRUCT-14 tranche decision).
