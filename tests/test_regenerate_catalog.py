"""Tests for the vendored regenerate_catalog.py (CR-CATALOG-STRUCT-12).

Pins the vendored copy's behavior on this repo's IDM-005 layout: the
canonical record file uses the hyphen-form filename
(``stakeholders-stakeholder-<slug>-<hash6>.yaml`` — the record id with
``:`` normalized to ``-``), and ``infer_state`` must recognize it. The
pre-fix colon-only lookup misclassified every hyphen-named canonical
record as a candidate (the vendored-regenerator bug family; fixed
upstream in dea-metaframework PR #58 and carried by this re-vendor).
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "regenerate_catalog.py"

RECORD_ID = "stakeholders:stakeholder-github-platform-a2b4c6"
HYPHEN_NAME = "stakeholders-stakeholder-github-platform-a2b4c6.yaml"
CANONICAL_DICT = {
    "id": RECORD_ID,
    "type": "Stakeholder",
    "name": "GitHub",
    "version": "1.0.0",
    "lifecycle_status": "active",
    "stakeholder_type": "supplier",
}


def _load_module():
    spec = importlib.util.spec_from_file_location("regenerate_catalog_test", SCRIPT)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _make_subtree(tmp_path: Path) -> Path:
    subtree = tmp_path / "github-platform-a2b4c6"
    subtree.mkdir()
    (subtree / HYPHEN_NAME).write_text(
        "\n".join(
            [
                f"id: {RECORD_ID}",
                "type: Stakeholder",
                "name: GitHub",
                "version: 1.0.0",
                "lifecycle_status: active",
                "stakeholder_type: supplier",
            ]
        )
    )
    return subtree


def test_vendored_default_schema_path_points_at_repo_layout():
    mod = _load_module()
    assert mod.DEFAULT_SCHEMA_PATH == "catalog-index-schema/catalog-index-schema.json"


def test_entity_id_read_from_hyphen_named_file(tmp_path):
    mod = _load_module()
    subtree = _make_subtree(tmp_path)
    assert mod.entity_id_from_subtree(subtree) == RECORD_ID


def test_infer_state_recognizes_hyphen_form_canonical(tmp_path):
    mod = _load_module()
    subtree = _make_subtree(tmp_path)
    # The colon-form filename must NOT exist (that is the whole point of
    # the regression: the pre-#58 lookup only checked this form).
    assert not (subtree / f"{RECORD_ID}.yaml").exists()
    state, canonical_path = mod.infer_state(subtree, dict(CANONICAL_DICT))
    assert state == "canonical"
    assert canonical_path == f"entities/v1-alpha/{RECORD_ID}/{HYPHEN_NAME}"


def test_infer_state_hyphen_form_retired(tmp_path):
    mod = _load_module()
    subtree = _make_subtree(tmp_path)
    retired = dict(CANONICAL_DICT, lifecycle_status="retired")
    state, canonical_path = mod.infer_state(subtree, retired)
    assert state == "retired"
    assert canonical_path == f"entities/v1-alpha/{RECORD_ID}/{HYPHEN_NAME}"
