# Changelog

All notable changes to the Stakeholders Catalog (dea-catalog-stakeholders) are documented here. Format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this
repository is governed by change requests (`change-requests/`).

## [Unreleased]

### CR-CATALOG-STRUCT-11: CI Hygiene (Pinned Dependencies, Unified Python, Job Timeouts)

Review 2026-10-27 concern 8, the last deferred recommendation. Every pip install is now `==`-pinned (`pyyaml==6.0.3`, `jsonschema==4.26.0`, `pytest==9.1.1`; the versions the full suite passed under locally, proven on 3.12 by this PR's runners); `python-version: "3.12"` is unified across workflows (`catalog-conformance.yml` gains `actions/setup-python@v5`, `validate-entity-system.yml` drops `3.x`, `validate-authorship.yml` moves `@v4` -> `@v5`); and every directly-defined job carries `timeout-minutes` (15 conformance / 10 others). `validate-allocation.yml` is a reusable-workflow call whose timeout is owned upstream. Actions SHA-pinning deliberately deferred (BC-39 §8 precedent). Carrier: `change-requests/CR-CATALOG-STRUCT-11-ci-hygiene-pinning-and-timeouts.md`.

### CR status close: CR-CATALOG-STRUCT-10

Per the standing landing discipline (introduced by CR-CATALOG-STRUCT-08 §2.2): CR-CATALOG-STRUCT-10's Status closes to `Merged` with landing evidence — merged as PR #10 and landed on `main` via the stack-completion PR #11 (PRs #9/#10 had merged into their stacked base branches, not `main`; #11 carried the verified stack). `CATALOG.yaml` regenerated: `open_change_requests` 1 -> 0; the index is now spotless (all carriers closed with PR evidence).

### CR-CATALOG-STRUCT-10: Gate Honesty, CI Test Wiring, Id-Namespace Alignment, Doc Truth

Four truth fixes in the layer that proves this catalog's trust, landed while the catalog is still empty. (1) `validate-entity-system.yml` no longer runs its strict gate with `continue-on-error: true` — the step can now actually block. (2) `catalog-conformance.yml` runs the full pytest suite (`python -m pytest tests/ -q`), retiring the install-but-never-run pytest step; the entity-system test module now runs in CI. (3) `reconciliation/entity-system-registry.yaml` identity flips to the org-wide form the repo's own IDM gate already enforces (`stakeholders:` prefix, hash6; `dea:` demoted to legacy) — previously the two id gates demanded mutually exclusive forms, which the first entity admission would have hit. (4) Doc truth sweep: CONTRIBUTING retitled for this repo (was "dea-catalog-processes") with real workflow names; cardinal-rules glob corrected to stakeholder records; entities README now lists only gates/artifacts that exist here (phantom register-audit/CR-metadata/allocation gates and reconciliation artifacts marked as Phase 2, not present tense) and points to each sibling's `CATALOG.yaml` instead of hardcoded counts; README metamodel claim aligned to the pointer (v0.2.1 / OpenDEAM v0.2.1; was v3.0.0-alpha from the pre-adoption scaffold), viewer badge `?entity=SH`, structure tree reflects the actual repo. The regenerator now falls back to the pointer's generated `conformance_status` when no top-level `status` exists, so `CATALOG.yaml` renders `status: draft` instead of a false `active` (the index schema's status enum admits draft, not scaffold). Carrier: `change-requests/CR-CATALOG-STRUCT-10-gate-honesty-ci-wiring-id-namespace-doc-truth.md`.

### Pre-CHANGELOG history (backfill, CR-CATALOG-STRUCT-10 §2.4)

This CHANGELOG was created with CR-CATALOG-STRUCT-06 (PR #6); earlier notable changes previously existed nowhere:

- PRs #1/#2: scaffold, LICENSE/NOTICE, metamodel-pointer mapping, CI fix (`dsanders11/json-schema-validate-action`).
- `822b566` / `2da0826`: metamodel-pointer regenerated from OpenDEAM v0.2.1 (ADR-0002); allocation pin (`validate-allocation.yml`).
- PR #3: CR-CATALOG-STRUCT-05 stakeholders catalog adoption (vendored regenerator/gate/schema, `catalog-conformance.yml`, `CATALOG.yaml`, `TEMPLATE_VERSION`).
- PR #4: org-wide id system bring-up (Wave 3): `scripts/check_id_system.py` (IDM-001..008).
- PR #5: entities/v1-alpha structural README mirrored from the processes template (flat layout, non-ECF).

### CR-CATALOG-STRUCT-09: Authorship Gate Table-Format Bypass (AUT-001 Coverage Hole)

`scripts/check_authorship.py` parsed only line-format `**Owner**:`/`**Author**:` fields, so table-format CR metadata (`| **Author** | ... |`, the shape of CR-CATALOG-STRUCT-06/07) was invisible to the gate: a CR carrying `| **Author** | Coder (for eaojnr) |` passed `--strict` with 0 findings (reproduced during the 2026-10-27 review), and 2 of 3 CRs on `main` were effectively unchecked. Fixed: `_extract_value` now extracts anchored table-format rows for `**...**` field paths (exact key match; adjacent table keys cannot match), and a new AUT-002 presence rule fires when a CR matching the registered glob exposes no authorship field at all. Five regression tests added (bypass probe, allowlist-clean, adjacent-key negatives, presence rule, line-format compatibility); the gate remains CONFORMANT on the live tree, now with all CR files actually covered. Carrier: `change-requests/CR-CATALOG-STRUCT-09-authorship-table-format-bypass.md`.

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
