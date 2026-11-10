# CR-CATALOG-STRUCT-15: Evidence-Chain Dossiers for the Canonical Tranche

**Status**: Open (PR #19)
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-10
**Trigger**: Owner directive 2026-11-10 to extend the catalog to capture the evidence exhaustively: each stakeholder subtree gets a dossier — evidence chain, profile (definition, goals, activities), and correlations to the enterprise's related entities. Authored agent-side on eaojnr's behalf; agency recorded here per the CR-BP-118 cardinal rule.
**Carrier**: this file
**Lands against**: `main` @ `55eb8efd1104da34079336956bae06119c0d9f9d` (post CR-CATALOG-STRUCT-14 status close, PR #17)
**Depends on**: CR-CATALOG-STRUCT-13, CR-CATALOG-STRUCT-14

## 1. What lands

The catalog's first content extension since the tranche: a **research dossier
per canonical record** (44 files across the 11 subtrees) plus the two
catalog-level artifacts that make the evidence first-class:

| Area | Change |
|---|---|
| `docs/EVIDENCE-STANDARD.md` | New: the dossier contract — subtree `research/` layout, the exhaustive evidence-chain obligations (E-#### rows, channels, URL-or-honest-note rule), the profile obligations (definition / mandate & goals / what they do / engagement), and the correlations contract (documentation-grade, live targets, basis required, deferred explicit). |
| `classifications/stakeholder-role-taxonomy.md` | New controlled vocabulary: 23 reusable, jurisdiction-free role classes (`sh-role:<slug>`) over the metamodel `stakeholder_type` enum, carrying the full typified corpus — 133 `E-####` evidence rows (name, jurisdiction, URL), with the ≥3-URL typification rule and its two by-design exceptions (collective licensee community; single-incumbent board). |
| `entities/v1-alpha/<slug>-<hash6>/research/` | 4 files per record subtree (11 subtrees): `README.md` (CST-009 index + provenance), `evidence-chain.md` (admission evidence + corpus rows + supporting evidence + asserted edges + honest notes), `stakeholder-profile.md` (definition, mandate and goals, what they do, enterprise engagement, role classes), `correlations.md` (regulations / capabilities / processes / services / actors — every target a live sibling record, states noted, basis named, deferred explicit). |
| `docs/RECORD-STANDARD.md` | §5 added: the record subtree now also carries the research dossier per EVIDENCE-STANDARD. |
| `entities/v1-alpha/README.md` | Topology section updated: the subtree diagram gains the `research/` dossier; pointer to the new standard. |
| `CATALOG.yaml` | Regenerated as the final commit action: per-entity `research_count: 4`, catalog `research_files: 44`, `open_change_requests` carried by this CR. |

Correlation coverage (all documentation-grade, ES-003 untouched): each
regulator's dossier correlates its enforced-regime record plus the enterprise
capability/process/service records that operationalize compliance (privacy,
security, financial-stewardship, legal-matter families, resolved against the
sibling catalogs' live CATALOG.yaml indexes); the supplier's dossier
correlates the technology/change/supplier-management capabilities, the
supplier services, and the CI actor whose workflows run on the platform; the
community's dossier correlates idea-management and license-management; the
board's dossier correlates the governance capabilities, the governance
processes, and the Actors-catalog dual-capacity boundary.

## 2. NOT-List

- **No new records admitted** — the 11 canonical records and their ids are untouched; market-instance rows in the taxonomy evidence classes only and assert no enterprise engagement (candidate-side truth).
- **No schema changes** — `schemas/entity.schema.json` and the projection gate are untouched.
- **No new relationship types or instances** — ES-003 register untouched; dossier correlations are explicitly documentation-grade (EVIDENCE-STANDARD §5).
- **No gate changes** — CST-009's research-README rule is consumed, not modified; dossier files are Markdown precisely so the ES/IDM/schema gates' record scope is unaffected.
- **No candidate-register changes** — C-001..C-004 stay as they are; the dossiers restate the deferred edges verbatim.

## 3. Acceptance criteria

- AC-01 All 44 research files land at the §1 layout paths; every subtree with research files carries `research/README.md` (CST-009 zero warnings).
- AC-02 Every correlation target id resolves to a live record in its sibling catalog's CATALOG.yaml at authoring time (capabilities / processes / services / actors / regulations), with non-canonical target states noted in the tables.
- AC-03 Every `E-####` id cited in a dossier resolves in the taxonomy corpus; the taxonomy carries all 133 rows exactly once; every canonical-party row is duplicated in its record's chain (44 rows) and the 89 market-instance rows live in the taxonomy only.
- AC-04 Gates green on the PR: `check_schema.py` (11 records validate; research files out of scope by design), `check_id_system.py --strict`, `check_entity_system.py --strict`, `check_pointer.py`, `check_catalog_index.py --strict`, CST-001..CST-015, `check_authorship.py --strict`, pytest 62, regenerator `--check` exit 0.
- AC-05 The record YAMLs are byte-identical to `main` (dossiers are additive only).
- AC-06 CHANGELOG `[Unreleased]` entry; CR index row; EVIDENCE-STANDARD linked from RECORD-STANDARD §5 and the entities README.

## 4. Follow-ons (named, not in this CR)

- C-001 enterprise-anchor decision unblocks the deferred edges restated in the supplier/community/board dossiers.
- Correlation maintenance: when a correlated sibling record retires or migrates ids, the dossiers' tables need a truth pass (candidate: a fleet-wide correlation-sweep CR).
- The 89 taxonomy-only market-instance rows are future candidate material if enterprise engagement ever becomes verifiable; they are not admissible today.
