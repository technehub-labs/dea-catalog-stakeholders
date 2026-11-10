# Governing board / directing authority — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-governing-board-authority-2wdtyy`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:governing-board-authority` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `github-org-ownership`: `eaojnr (owner role, technehub-labs org)`

## 2. Class corpus (typified evidence for the class)

All 3 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0131 | Emmanuel A. Otchere (governing board) | governance | 1 (in-repo primary) | https://github.com/eaojnr | engaged instance (this enterprise) |
| E-0132 | dea-catalog-stakeholders repository (maintainer surface) | org | 3 (public record) | https://github.com/technehub-labs/dea-catalog-stakeholders | market instance (no enterprise engagement) |
| E-0133 | technehub-labs organization (ownership surface) | org | 3 (public record) | https://github.com/technehub-labs | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0131.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 1 (in-repo primary) | governance-cr | change-requests/CR-CATALOG-STRUCT-14-first-canonical-tranche.md (owner directive + tranche decision, 2026-11-08) | — | the board's ratification authority exercised over the catalog's first tranche (recorded in-repo) |
| 3 (public record) | github-profile | eaojnr (owner of the technehub-labs organization) | https://github.com/eaojnr | resolves the natural person holding the governing-board capacity |
| 3 (public record) | github-org-ownership | technehub-labs organization ownership surface | https://github.com/technehub-labs | the ownership surface over which the board's capacity is exercised |

## 4. Asserted edges carried by the record

None asserted.

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- `governs` edge onto the enterprise anchor awaits C-001.
- Contact details are deliberately absent from the record (name + capacity only, per the STRUCT-14 tranche decision).

