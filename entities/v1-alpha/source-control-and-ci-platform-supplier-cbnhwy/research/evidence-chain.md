# Source-control and CI platform supplier — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-source-control-and-ci-platform-supplier-cbnhwy`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:source-control-and-ci-platform-supplier` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `github-org`: `technehub-labs`

## 2. Class corpus (typified evidence for the class)

All 3 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0125 | GitHub, Inc. | platform; hosting | 1 (in-repo primary) | https://github.com | engaged instance (this enterprise) |
| E-0126 | Atlassian (Bitbucket) | market | 3 (public record) | https://bitbucket.org | market instance (no enterprise engagement) |
| E-0127 | GitLab Inc. | market | 3 (public record) | https://about.gitlab.com | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0125.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 1 (in-repo primary) | ci-workflow | .github/workflows/ci.yml + .github/workflows/catalog-conformance.yml (this repo) | — | the enterprise's validation pipelines are defined in-repo and execute on this stakeholder's hosted Actions runners |
| 1 (in-repo primary) | source-control-hosting | repositories of the technehub-labs organization, incl. this catalog repo | https://github.com/technehub-labs | the entire OpenDEA fleet is hosted on the stakeholder's platform |
| 3 (public record) | official-website | GitHub, Inc. corporate site | https://github.com | resolves the party (a Microsoft subsidiary operating the GitHub platform) and its capacity as platform supplier |

## 4. Asserted edges carried by the record

None asserted.

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- `serves` / `supplies` edges onto the enterprise await the C-001 enterprise-anchor decision (candidate register); the record asserts no edges today per RECORD-STANDARD §1.6.

