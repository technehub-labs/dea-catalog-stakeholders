# CR-CATALOG-STRUCT-10: Gate Honesty, CI Test Wiring, Id-Namespace Alignment, Doc Truth

**Status**: Merged (PR #10, landed on `main` via the stack-completion PR #11)
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Review 2026-10-27 (`review-report-dea-catalog-stakeholders.md`, concerns 4, 5, 7; verified against `main` @ `de4a581`). The review was performed agent-side on eaojnr's behalf; agency is recorded here rather than in the authorship field, per the CR-BP-118 cardinal rule as propagated by CR-CATALOG-STRUCT-06.
**Carrier**: this file
**Lands against**: `main` @ `de4a581`
**Depends on**: lands after STRUCT-08 (index arithmetic) — content otherwise independent

## 1. Problem (verified on `main` @ `de4a581`)

Four truth deficits in the layer that proves this catalog's trust, all cheap to fix while the catalog is still empty:

1. **`validate-entity-system.yml` runs its strict gate with `continue-on-error: true`** — the step can never block a PR, while CR-CATALOG-STRUCT-07 §4 and the CHANGELOG advertise `--strict` on every PR. Vacuous today (0 entities) but structurally dishonest the day the first record lands.
2. **The test suite runs nowhere.** `catalog-conformance.yml` installs pytest and never runs a test; `tests/test_check_entity_system.py` (32 passing tests) executes in no workflow; only the authorship module runs, in a different workflow.
3. **The repo's two id gates contradict each other** about the canonical id form: `scripts/check_id_system.py:44` IDM-001 requires the org-wide form `^stakeholders:stakeholder-[a-z0-9-]+-[a-z2-9]{6}$` (namespace `stakeholders:`, content hash; `dea:` is legacy), while `reconciliation/entity-system-registry.yaml` (STRUCT-07) declares `canonical_prefix: "dea:"` / `canonical_pattern: "^dea:stakeholder-[a-z0-9-]+$"` (no hash). No future record can satisfy both. STRUCT-07's "pre-migration namespace state" framing postdates this repo's own Wave-3 IDM bring-up (PR #4, 2026-09-21) that already adopted the org-wide form — the registry, not the IDM gate, is the outlier.
4. **Documentation copied from siblings without adaptation** (details in §2.4): CONTRIBUTING titled for the wrong repo, a processes-repo glob in the cardinal rules, an entities README documenting gates and artifacts that do not exist here, a README whose metamodel claims predate the OpenDEAM pointer, and a `metamodel-pointer.yaml` shape that renders `CATALOG.yaml` as `status: active` while the pointer's real `catalog.status: scaffold` sits unread one level down.

## 2. Design

### 2.1 Remove the false blocking claim (`validate-entity-system.yml`)

Delete `continue-on-error: true` from the "Run Entity System gate (--strict)" step. Verified safe: the gate exits 0 on this tree (vacuously CONFORMANT, 0 entities in `file_globs`); the `--self-test` step is unaffected.

### 2.2 Wire the test suite into CI (`catalog-conformance.yml`)

Add one step after the gates (the workflow already installs pytest in its dependency step — this also retires the "installs pytest, never runs it" finding):

```yaml
      - name: Run test suite
        run: python -m pytest tests/ -q
```

This runs all 53+ tests (both modules) on every push/PR to `main`. The authorship module also keeps running in `validate-authorship.yml` (harmless duplication; that workflow's own gate+tests stay).

### 2.3 Align the entity-system registry to the org-wide id form

`reconciliation/entity-system-registry.yaml` `identity:` block flips to match IDM-001 exactly (the org-wide form this repo's own IDM gate and the entities README's cross-reference section already prescribe):

```yaml
identity:
  id_field: id
  canonical_prefix: "stakeholders:"
  canonical_pattern: "^stakeholders:stakeholder-[a-z0-9-]+-[a-z2-9]{6}$"
  legacy_prefix: "dea:"
  legacy_pattern: "^dea:stakeholder-[a-z0-9-]+$"
  legacy_migration_map: "reconciliation/migration-id-map.yaml"
```

`envelope.file_globs`, profiles, relationships, lifecycle, per-type gates, and the exception mechanism are untouched. Verified safe: the entity-system gate is vacuously CONFORMANT (0 entities), so the flip changes no live verdict; the migration map stays a declared path (absent today, as it is now) and is created when the first admission or the T8 follow-on needs it. After this flip, when the first Stakeholder record lands, ES-001 and IDM-001 demand the same id — instead of two mutually exclusive ones.

### 2.4 Doc truth sweep (file by file)

- **`CONTRIBUTING.md`**: title "Contributing to `dea-catalog-processes`" -> `dea-catalog-stakeholders`; "CI runs all 32 conformance gates" -> name the actual workflows (validate, catalog-conformance, validate-allocation, validate-authorship, validate-entity-system); the reference to `change-requests/CR-BP-118-authorship-cardinal-rule.md` (not in this repo) -> `change-requests/CR-CATALOG-STRUCT-06-authorship-cardinal-rule.md` (this repo's slice) with the CR-BP-118 authority noted in prose.
- **`docs/governance/cardinal-rules.md:19`**: authorship-bearing field glob `entities/v1-alpha/**/processes-*.yaml` (a processes-repo glob) -> `entities/v1-alpha/**/stakeholders-stakeholder-*.yaml` (this repo's future record shape, per `docs/entity-storage-layout` flat layout and IDM-005 filename derivation), with a note that registering the field in `reconciliation/authorship-fields.yaml` happens with the first admission CR.
- **`entities/v1-alpha/README.md`**: the gates list documents `check_register_audit.py`, `check_cr_metadata.py`, and an "allocate / validate" CI job that do not exist in this repo, and the reconciliation section lists `reconciliation/inventory.yaml`, `baseline/v1.yaml`, `conformance_report.yaml` that do not exist, claiming "CI enforces this". Replace with this repo's actual gates (schema validation via `ci.yml` early-exit, CST suite, IDM-001..008, authorship, entity-system, allocation pin, catalog index) and actual artifacts (`CATALOG.yaml`, `reconciliation/authorship-fields.yaml`, `reconciliation/entity-system-registry.yaml`); keep the not-yet-adopted items as an explicit Phase 2 list instead of present-tense claims. The id-form table's missing namespace colon (`stakeholders-<level>-<slug>-<hash6>`) -> `stakeholders:stakeholder-<slug>-<hash6>` (IDM-001 form; the cross-references section two paragraphs below already uses the colon form). Replace the hardcoded sibling counts (capabilities "31", processes "3,598" — both stale) with pointers to each repo's `CATALOG.yaml` so the table cannot rot again.
- **`README.md`**: "Metamodel: v3.0.0-alpha" (entity table row and header line) -> the pointer's values (`metamodel.version: v0.2.1`, `metamodel_version: ^0.2.1`, OpenDEAM v0.2.1 / ADR-0002) — the v3.0.0-alpha claim is from the pre-adoption scaffold (commit `cf57b58`) and predates the pointer regeneration (`822b566`); viewer badge `?entity=Stakeholder` -> `?entity=SH` (the pointer's generated `viewer_url`); the "Catalog Structure" tree -> the actual tree (add `change-requests/`, `classifications/`, `contributions/`, `reconciliation/`, `catalog-index-schema/`, `CATALOG.yaml`, `TEMPLATE_VERSION`, and the five workflows — the current tree shows only `ci.yml`).
- **`metamodel-pointer.yaml` / regenerator status fallback**: the pointer is machine-generated ("do not edit manually") and carries no top-level `status` key (only the nested `catalog.status: scaffold`), so the regenerator renders `CATALOG.yaml` as `status: active` while the pointer describes a scaffold. Fix in `scripts/regenerate_catalog.py` `build_catalog_metadata`, not in the pointer: `status = pointer.get("status") or pointer.get("conformance_status") or "active"`. Implementation-time discovery: the vendored index schema (and upstream `v2.6.0`) constrains `status` to the enum `{active, draft, deprecated, retired}` — a literal `scaffold` would fail `check_catalog_index.py` — so the fallback reads the pointer's own top-level `conformance_status: draft` (generated value, schema-legal, truthful). This also closes the gap between STRUCT-05's claim that the top-level metadata block includes `status` and what the pointer actually carries. Regenerate `CATALOG.yaml` in the same PR (`status: active` -> `status: draft`; `version` legitimately stays `0.0.0` — no catalog release exists yet, and `TEMPLATE_VERSION` is the template's version, not the catalog's).
- **`CHANGELOG.md`**: add a short "pre-CHANGELOG history" block under `[Unreleased]` recording PRs #1-#5 in one line each (scaffold, CI fix, pointer regeneration, allocation pin, adoption STRUCT-05, id-system bring-up, entities README mirror) — the file was created at PR #6, so notable changes before it currently exist nowhere.

### 2.5 Landing checklist (this CR)

Statuses of previously-merged carriers updated per the STRUCT-08 standing discipline; `change-requests/README.md` gains the STRUCT-10 row; `CATALOG.yaml` regenerated (count delta: prior carrier closed, this carrier open); `CHANGELOG.md` `[Unreleased]` entry for STRUCT-10.

## 3. Acceptance criteria

- AC-01 `grep -n "continue-on-error" .github/workflows/*.yml` returns no hits; `validate-entity-system.yml` strict step blocks (and exits 0 on this tree: `python3 scripts/check_entity_system.py --strict`).
- AC-02 `python -m pytest tests/ -q` runs as a blocking step in `catalog-conformance.yml`; suite passes (53+ tests).
- AC-03 `grep -n "canonical_pattern" reconciliation/entity-system-registry.yaml` matches IDM-001: prefix `stakeholders:`, pattern `^stakeholders:stakeholder-[a-z0-9-]+-[a-z2-9]{6}$`, legacy `dea:`; cross-check command `python3 scripts/check_id_system.py --strict` still exits 0.
- AC-04 No file in the repo claims a gate, workflow, artifact, count, or version that does not exist: `grep -rn "dea-catalog-processes" CONTRIBUTING.md` empty; `grep -n "processes-\*" docs/governance/cardinal-rules.md` empty; `grep -n "check_register_audit\|check_cr_metadata\|inventory.yaml\|conformance_report" entities/v1-alpha/README.md` empty (or the items are explicitly listed as Phase 2, not present tense); `grep -n "3.0.0-alpha" README.md` empty.
- AC-05 `CATALOG.yaml` renders `status: draft` (regenerator fallback via the pointer's `conformance_status`) and matches regenerator output (`--check` exit 0).
- AC-06 `CHANGELOG.md` carries the pre-CHANGELOG history block and the STRUCT-10 `[Unreleased]` entry.
- AC-07 `change-requests/README.md` carries the STRUCT-10 row and updated prior statuses; `CATALOG.yaml` open-count arithmetic per §2.5.

## 4. NOT-List

- No CI hygiene backlog: pip dependency pinning, `python-version` unification, actions-by-SHA, `timeout-minutes` — deferred (same class as the sibling repos' findings; fold into a later hygiene CR).
- No Phase 2 changes to `ci.yml` (early-exit removal, validator action swap) — owned by the first-admission CR per STRUCT-05.
- No `dependencies.yaml` introduction and no metaframework upstream changes (the CST pin landed as STRUCT-08 §2.4; the upstream `count_open_change_requests` fix is a separate metaframework CR).
- No manual edits to `metamodel-pointer.yaml` (machine-generated; the status fix is in the regenerator, §2.4).
- No entity admissions, no registry profiles, no migration-map creation (first admission CR; T8 follow-on).
