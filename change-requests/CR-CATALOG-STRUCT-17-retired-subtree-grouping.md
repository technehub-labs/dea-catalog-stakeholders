# CR-CATALOG-STRUCT-17: Retired-Subtree Grouping (State-Grouped Layout for Fully-Retired Records)

**Status**: Open
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-10
**Trigger**: Owner directive 2026-11-10 — after STRUCT-16 the 11 retired party records still sat beside the canonical role-class records at the entities root (retired in place, per FOUNDATIONS §5's then-current no-successor shape), so a consumer of `entities/` still saw named parties mixed into the reusable set; the owner asked why and preferred them visually separated. Upstream `dea-metaframework` PR #63 (CR-CATALOG-STRUCT-12 state-grouped subtrees; release v2.8.0) landed the tooling that makes the separation standard: `regenerate_catalog.py`, `check_catalog_index.py`, and the CST enumerate subtrees under top-level state groupings (`research/`, `candidates/`, `retired/`) and derive recorded paths from disk position, with CST-010 guarding lifecycle agreement under the grouping. This CR carries that layout into this catalog: the 11 fully-retired party records move under `entities/v1-alpha/retired/`, unchanged. Authored agent-side on eaojnr's behalf; agency recorded here per the CR-BP-118 cardinal rule.
**Carrier**: this file
**Lands against**: `main` @ `468fcbbfb60db1a7a8038479ee72e26119aeecde` (post STRUCT-16 status close, PR #21 + #22)
**Depends on**: CR-CATALOG-STRUCT-16; upstream `dea-metaframework` CR-CATALOG-STRUCT-12 (PR #63; release v2.8.0)
**Supersedes** (layout only): STRUCT-16's in-place retirement position for the 11 party records — the records, ids, versions, dossiers, and supersession content are unchanged; only their location on disk moves to the §5 standard grouped shape (applied retroactively to the STRUCT-16 retirements).

## 1. What lands

| Area | Change |
|---|---|
| 11 party subtrees grouped | The fully-retired party-form records move unchanged from their flat locations to `entities/v1-alpha/retired/<dir>/`: `stakeholders:stakeholder-california-privacy-protection-agency-mtxygk`, `stakeholders:stakeholder-eu-data-protection-authorities-rs8g75`, `stakeholders:stakeholder-eu-trade-secret-authorities-zwf29g`, `stakeholders:stakeholder-github-inc-msn3q2`, `stakeholders:stakeholder-governing-board-hgr5us`, `stakeholders:stakeholder-hhs-office-for-civil-rights-hf7e8x`, `stakeholders:stakeholder-oss-community-nf74fy`, `stakeholders:stakeholder-pci-security-standards-council-ek8khf`, `stakeholders:stakeholder-uk-information-commissioner-5e64th`, `stakeholders:stakeholder-us-department-of-justice-nqbwya`, `stakeholders:stakeholder-us-securities-and-exchange-commission-ucaru6`. Pure relocation: every record YAML, subtree README, and `research/` dossier is byte-identical to main; ids are assign-once and never recomputed; no content, version, or lifecycle change. |
| Grouping index | `entities/v1-alpha/retired/README.md` — the grouping's contract (moved unchanged; ids never recomputed; CST-010 lifecycle agreement) and the superseded-by table: each retired party mapped to its canonical role-class successor (verified 1:1 against the record yamls). |
| Role-record dossier paths re-pointed | The 12 canonical role records' `research/stakeholder-profile.md` files reference the engaged instance's retained dossier location; those 12 path references now point at the grouped location (`entities/v1-alpha/retired/<dir>/research/`) — path text only, no other content change (a repo-wide sweep confirms no other stale flat-path reference remains). |
| Tooling re-vendor (v2.8.0) | `scripts/regenerate_catalog.py` and `scripts/check_catalog_index.py` re-vendored from upstream main (== v2.8.0): state-grouped subtree enumeration, recorded paths derived from disk position, and the upstream default `--schema` location (this repo's invocations pass `--schema catalog-index-schema/catalog-index-schema.json` explicitly — workflow and tests pin it). `catalog-index-schema/catalog-index-schema.json` re-vendored as a byte refresh; the contract is unchanged (required fields and patterns identical; grouped paths were already admitted by the `entities/v1-alpha/.+` pattern). |
| Workflow pin bump | `.github/workflows/catalog-conformance.yml`: metaframework `ref: v2.6.0` → `ref: v2.8.0` (the release carrying the grouped-subtree tooling; its content is already merged upstream as PR #63). No step changes. |
| IDM-005 two-location rule | `scripts/check_id_system.py`: a record file now resolves at `entities/v1-alpha/<dir>/` OR `entities/v1-alpha/<state>/<dir>/` (state in `research`/`candidates`/`retired`, per entity-storage-layout §3.2), and `_load_all_records()` enumerates the grouped patterns — the 11 relocated records stay under IDM discipline (strict run: 23 records, 0 findings). |
| `docs/FOUNDATIONS.md` | §2 topology note and §5 step 5 restated: grouping under `entities/v1-alpha/retired/` is the standard shape for fully-retired records (no live canonical successor); the per-subtree `retired/` shape remains for subtrees that retain a live canonical record. STRUCT-16's in-place position is superseded as a layout. |
| `entities/v1-alpha/README.md` | Topology diagram gains the `retired/` grouping lines; the party-records note restated as grouped per this CR. |
| Test pins updated | `tests/test_regenerate_catalog.py`: pins updated to the v2.8.0 vendored behavior (explicit `--schema` invocation against the repo layout; disk-position-derived entity paths) plus a new grouped-layout test (`infer_state` emits `entities/v1-alpha/retired/<dir>/...` for grouped subtrees). |
| CR index, `CHANGELOG.md`, `CATALOG.yaml` | Index row, changelog entry, regenerated index: entity paths emit the grouped form; counts unchanged from main (`entities: 23`, `canonical: 12`, `retired: 11`, `research_files: 92`); `open_change_requests: 1` while this CR is Open. |

## 2. NOT-List

- **No record content change** — the 11 retired record YAMLs and their 44 research dossier files are byte-identical to main; the move touches paths only. The 12 role records' profile files change exactly one path line each (the engaged-instance dossier location).
- **No id is recomputed** — assign-once (FOUNDATIONS §3, IDM-004); the 11 party ids and the 12 role-class ids are untouched, and cross-repo references stay resolvable.
- **No record is deleted or admitted** — the candidate register is untouched (C-005 stays); the 9 role-level asserted edges are unchanged (ES-003 register untouched).
- **No CATALOG.yaml contract change** — the re-vendored index schema is a byte refresh with identical required fields and patterns.
- **No workflow step change** — only the metaframework ref pins from v2.6.0 to v2.8.0.
- **No gate is weakened** — IDM-005's extension is a location rule (two allowed positions per entity-storage-layout §3.2), not a discipline change; upstream CST gains the CST-010 grouped-lifecycle guard.

## 3. Acceptance criteria

- AC-01: The 11 party subtrees exist under `entities/v1-alpha/retired/` with byte-identical contents; no copy remains at the old flat locations (each id appears exactly once in CATALOG.yaml, at its grouped path).
- AC-02: All gates green in the grouped layout: catalog index (strict, 23 entities), pointer, schema, id system (strict, 23 records, 0 findings), entity system (strict), authorship (strict), tests (63 passed), CST 17/17 including CST-010, regenerator `--check` clean against the pinned schema.
- AC-03: Vendored scripts and index schema equal upstream v2.8.0; the workflow pins `ref: v2.8.0`.
- AC-04: `entities/v1-alpha/retired/README.md` lists the 11 parties with `superseded-by` references that resolve 1:1 to live canonical role-class records.
- AC-05: `docs/FOUNDATIONS.md` §5 names the grouped shape as the standard for fully-retired records, and the entities README topology shows the grouping.
- AC-06: CATALOG.yaml counts unchanged from main — `entities: 23`, `canonical: 12`, `retired: 11`, `research_files: 92` (only entity paths and `open_change_requests` differ).
- AC-07: No stale flat-path reference remains — every in-repo reference to the 11 party subtrees points at the grouped location (the 12 role-record profiles re-pointed; the party dossiers carry no flat-path self-references).

## 4. Follow-ons

- Release tag **v2.8.0** on `dea-metaframework` main (owner action; the workflow pins the tag, whose content is already merged as PR #63) — the conformance workflow requires it to resolve.
- Status close after merge per the standing landing discipline (STRUCT-10 precedent): Status → `Merged (PR #N)`, then regenerate CATALOG.yaml so `open_change_requests` returns to 0.
- Other fleet catalogs adopt the grouping when they acquire fully-retired records (the v2.8.0 tooling supports them out of the box).
