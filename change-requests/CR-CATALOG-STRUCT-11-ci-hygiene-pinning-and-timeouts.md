# CR-CATALOG-STRUCT-11: CI Hygiene (Pinned Dependencies, Unified Python, Job Timeouts)

**Status**: Proposed
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Review 2026-10-27 concern 8 / recommendation 5 (deferred from the STRUCT-08/09/10 carriers to keep them reviewable; the last open recommendation of that review). Authored agent-side on eaojnr's behalf; agency recorded here per the CR-BP-118 cardinal rule.
**Carrier**: this file
**Lands against**: `main` @ `e247e2f` (stacked on the CR-10 status-close PR #12)
**Depends on**: none functionally; lands after PR #12 for single-step index arithmetic

## 1. Problem (review concern 8)

CI hygiene defects shared with the sibling repos, none blocking but all cheap to fix while the repo is quiet:

- **Unpinned pip dependencies** in every workflow that installs anything (`catalog-conformance.yml`: `pip install pyyaml jsonschema pytest`; `validate-authorship.yml`: `pip install pytest`; `validate-entity-system.yml`: `pip install pyyaml`). A breaking upstream release turns CI red for reasons unrelated to any change.
- **`python-version` inconsistent** across workflows: `3.12` (validate-authorship, on `setup-python@v4`), `3.x` (validate-entity-system, on `setup-python@v5`), and none at all (catalog-conformance runs on the runner's default interpreter).
- **No `timeout-minutes` anywhere**: a hung job burns a full runner allocation (6h default).

## 2. Changes

| Workflow | Change |
|---|---|
| `catalog-conformance.yml` | `timeout-minutes: 15`; new `actions/setup-python@v5` with `python-version: "3.12"` (deterministic interpreter); `pip install pyyaml==6.0.3 jsonschema==4.26.0 pytest==9.1.1` |
| `validate-authorship.yml` | `timeout-minutes: 10`; `setup-python@v4` -> `@v5` (unify with the rest of the org); `pip install pytest==9.1.1` |
| `validate-entity-system.yml` | `timeout-minutes: 10`; `python-version: "3.x"` -> `"3.12"`; `pip install pyyaml==6.0.3` |
| `ci.yml` | `timeout-minutes: 10` (no pip/python of its own; the `dsanders11` action runs self-contained) |
| `validate-allocation.yml` | No change possible: the job is a reusable-workflow call, and `timeout-minutes` is not settable on a caller job; the timeout is owned by `dea-architecture-framework`'s `validate-against-model.yml` upstream |

The pinned versions are the ones the full local suite (58 tests, all gates, CST 16/16) passed under on 2026-10-27; the PR's own runner pass proves them under 3.12.

## 3. Acceptance criteria

- AC-01 All five workflows parse as valid YAML (`python -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))"` per file).
- AC-02 `grep -Rn "pip install" .github/workflows/` shows only `==`-pinned installs.
- AC-03 `grep -Rn "python-version" .github/workflows/` shows `"3.12"` everywhere it appears.
- AC-04 `grep -Ln "timeout-minutes" .github/workflows/*.yml` returns only `validate-allocation.yml` (reusable call; owned upstream).
- AC-05 Local gates unchanged: `check_authorship --strict` exit 0, `pytest tests/ -q` 58 passed, regenerator `--check` exit 0.
- AC-06 CI on the PR: all five workflows green under the pinned versions on 3.12.
- AC-07 CHANGELOG `[Unreleased]` entry; CR index row added; `CATALOG.yaml` regenerated (this carrier Proposed -> count 1 on this stack).

## 4. NOT-List

- **Actions SHA-pinning deferred** (deliberately): resolving outside-org action tag SHAs is not possible from the current environment, and pinning the moving major tags (`@v4`, `@v5`) to SHAs requires an org-wide minor-version policy. Same deferral as capabilities CR-DEA-BC-39 §8. The `dsanders11/json-schema-validate-action@v2.1.0` and `dea-architecture-framework@v0.2.1` pins stay as-is (the latter is already a release-tag pin).
- No workflow trigger changes (`pull_request: branches: [main]` semantics untouched).
- No script changes, no gate changes, no schema changes.
- No `requirements.txt` / dependency lockfile introduction: three pinned installs across three workflows do not justify a lockfile yet; first entity admission can introduce one if the dependency set grows.
