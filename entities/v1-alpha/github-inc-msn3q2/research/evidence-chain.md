# GitHub, Inc. — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-github-inc-msn3q2`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `github-org`: `technehub-labs`
- `official-website`: `https://github.com`

## 2. Typified corpus rows


### Class `source-control-and-ci-platform-supplier` — Source-control and CI platform supplier

Role class `sh-role:source-control-and-ci-platform-supplier` in the taxonomy; stakeholder_type `supplier`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0125 | 1 (in-repo primary) | github-org | technehub-labs | https://github.com |

### Class `package-registry-supplier` — Package-registry supplier

Role class `sh-role:package-registry-supplier` in the taxonomy; stakeholder_type `supplier`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|

Adjacent class: the package-registry supplier class is evidenced by npm (operated by GitHub, Inc.); this record carries only the source-control/CI platform capacity, not a separate registry-supplier assertion.


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 1 (in-repo primary) | ci-workflow | .github/workflows/ci.yml + .github/workflows/catalog-conformance.yml (this repo) | — | the enterprise's validation pipelines are defined in-repo and execute on this stakeholder's hosted Actions runners |
| 1 (in-repo primary) | source-control-hosting | repositories of the technehub-labs organization, incl. this catalog repo | https://github.com/technehub-labs | the entire OpenDEA fleet is hosted on the stakeholder's platform |
| 3 (public record) | official-website | GitHub, Inc. corporate site | https://github.com | resolves the party (a Microsoft subsidiary operating the GitHub platform) and its capacity as platform supplier |

## 4. Asserted edges carried by the record

- None asserted. `serves` / `supplies` edges onto the enterprise await the C-001 enterprise-anchor decision (candidate register); the record asserts no edges today per RECORD-STANDARD §1.6.

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- `serves` / `supplies` edges onto the enterprise await the C-001 enterprise-anchor decision (candidate register); the record asserts no edges today per RECORD-STANDARD §1.6.
