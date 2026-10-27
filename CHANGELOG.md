# Changelog

All notable changes to the Stakeholders Catalog (dea-catalog-stakeholders) are documented here. Format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this
repository is governed by change requests (`change-requests/`).

## [Unreleased]

### CR-CATALOG-STRUCT-08: Main-Green Remediation (Counter Fix, CR Statuses, Index Row, Metaframework Ref Pin)

`main` has been red on `catalog-conformance` since 2026-10-14 (both October merges landed red), with two independent causes; this CR fixes both. `scripts/regenerate_catalog.py` `count_open_change_requests` now parses a CR status token from either house metadata shape (bold-line `**Status**: X` and table `| **Status** | X |`), closes on the org-consistent terminal set `{Merged, Landed, Applied, Accepted, Rejected, Superseded, Withdrawn}` (as landed in CR-DEA-BC-38), and drops the duplicated `"Status**: Merged"` condition inherited from the vendored copy (`:518`); the old substring heuristic miscounted a carrier CR that quotes the buggy line. Landed CR statuses backfilled with landing evidence: STRUCT-05 -> `Merged (PR #3)`, STRUCT-06 -> `Merged (PR #6)`, STRUCT-07 -> `Merged (PR #7)`. CR index gains the missing STRUCT-06 row and a standing discipline note (every landing PR closes prior carriers' statuses and regenerates `CATALOG.yaml`). The `dea-metaframework` checkout in `catalog-conformance.yml` is pinned to `ref: v2.6.0` (CST-013/014). `CATALOG.yaml` regenerated: truthful `open_change_requests` under the fixed counter (3 -> 0 prior CRs; this carrier open). Carrier: `change-requests/CR-CATALOG-STRUCT-08-main-green-counter-statuses-ref-pin.md`.

### CR-CATALOG-STRUCT-07: Entity System Stage 5-6 (Stakeholders Slice)

Stakeholders slice of the General Entity System institutionalisation (cross-repo cascade T7 of the umbrella programme). New `reconciliation/entity-system-registry.yaml` (per-repo; generic; no profiles; canonical pattern `^dea:stakeholder-[a-z0-9-]+$`). New `scripts/check_entity_system.py` (5-rule umbrella gate; copied verbatim from `dea-catalog-processes`). New `tests/test_check_entity_system.py` (32 tests; 4 pilot-specific tests made generic for cross-repo portability; all pass). New `.github/workflows/validate-entity-system.yml` (CI). Live: gate vacuously CONFORMANT (0 entities in file_globs). D-004 clean. 118a/b/c authorship gates remain CONFORMANT.

### CR-CATALOG-STRUCT-06: Authorship Cardinal Rule (R1, R2) - Org-Wide Propagation Slice

User directive 2026-10-13: "no `Coder` / `Agent` / agent or tool names in any
authorship field of any published artifact". The CR-BP-118 cardinal rules (R1
and R2) are propagated to this repo. New blocking gate
`scripts/check_authorship.py` (CR-BP-118 / AUT-001..003), data-driven from
`reconciliation/authorship-fields.yaml` (allowlist
`{Emmanuel A. Otchere, TechNeHub Labs}`; denylist
`{Coder, Agent, Hermes, Claude, GPT, Cline, OpenAI, MiniMax, MiniMax-M3}`).
The repo's authorship-bearing field set is identical to the 118a baseline
(`**Owner**`, `**Author**` in `change-requests/CR-*.md`); no per-repo
extension is needed. CI wiring: new workflow
`.github/workflows/validate-authorship.yml` runs the gate in `--strict` mode
on every push and PR. 21/21 `test_check_authorship` pass. Carrier:
`change-requests/CR-CATALOG-STRUCT-06-authorship-cardinal-rule.md`.
