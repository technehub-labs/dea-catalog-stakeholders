# CR-CATALOG-STRUCT-16: Role-First Restructure (Role Classes as Canonical Records)

**Status**: Open
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-10
**Trigger**: Owner directive 2026-11-10 — the catalog was requested to be generalized (stakeholders as reusable, jurisdiction-free role records, per the flat-file role-catalog convention); the canonical tranche instead landed named parties (`california-privacy-protection-agency-mtxygk`, `uk-information-commissioner-5e64th`, ...), which defeats reusability: a consumer of `entities/` sees jurisdictions, and the reusable layer lived only as documentation (`classifications/`). This CR restructures the catalog so the role class is the record and the named party is instance evidence. Authored agent-side on eaojnr's behalf; agency recorded here per the CR-BP-118 cardinal rule.
**Carrier**: this file
**Lands against**: `main` @ `e206c5db89da436cb97ffdabe843d400526345bf` (post STRUCT-15, PR #19 + #20)
**Depends on**: CR-CATALOG-STRUCT-14, CR-CATALOG-STRUCT-15
**Supersedes** (record form, not content): the 11 party-form canonical records of STRUCT-14 — retired, not deleted; their evidence, dossiers, and ids are retained as engaged-instance history.

## 1. What lands

The catalog's record identity inverts from **party-first** (a named party with
roles as documentation) to **role-first** (a jurisdiction-free role class with
named parties as instance evidence) — the convention the flat-file role
catalog (workbook) and the STRUCT-15 taxonomy already carry:

| Area | Change |
|---|---|
| 12 new canonical records | One subtree per role class with enterprise engagement: `gdpr-supervisory-authority`, `data-protection-coordination-authority`, `data-protection-supervisory-authority`, `state-consumer-privacy-regulator`, `health-data-regulation-authority`, `securities-and-markets-regulator`, `justice-enforcement-authority`, `trade-secret-enforcement-authority`, `payment-card-standards-body`, `open-source-licensee-community`, `source-control-and-ci-platform-supplier`, `governing-board-authority`. Ids minted assign-once per FOUNDATIONS §3 (`stakeholders:stakeholder-<role-slug>-<hash6>`); geography lives only in instance evidence rows. |
| 11 party records retired | `lifecycle_status: retired` in place at the subtree root (FOUNDATIONS §5's no-successor shape; the subtree holds no live canonical successor), version bumped to 1.1.0, a `superseded-by` external reference to the role record, and a supersession sentence in the description. Never deleted, ids never recomputed: the party subtrees and their STRUCT-15 dossiers remain as the engaged-instance history (cross-repo references stay resolvable). Their asserted edges move to the role records — the retired records stop asserting (edge history preserved in the retained dossiers). |
| Edges re-expressed at role level | The 8 asserted edges move to the role records, asserted **through the engaged instance for this enterprise** (rationale states the instance; the sibling regulation record still anchors the regime, evidence channel 2). `enforces` ×7, `publishes` ×1 — same targets as STRUCT-14; ES-003 register untouched (types and targets unchanged). The EU GDPR regulation record gains a second source (the coordination-authority class joins the supervisory-authority class) — an honest statement about the collective engaged instance. |
| 48 dossier files | Each role record carries the STRUCT-15 dossier shape (4 files): `evidence-chain.md` now holds the **full class corpus** (all `E-####` rows for the class — engaged instances and market instances; market rows assert no enterprise engagement), `stakeholder-profile.md` defines the capacity (definition, mandate and goals, what the class does, engagement via named instances), `correlations.md` re-expresses the party correlations at class level, `README.md` indexes with provenance. |
| `docs/FOUNDATIONS.md` | §2 admission contract restated: canonical records are **role classes** — admitted when the class is typified (≥3 URL instance evidence, or the two by-design exceptions) AND the enterprise-engagement instance is named in the chain; §3 slug convention becomes the role-class slug (jurisdiction-free); §4 edges asserted at role level through engaged instances; §5 gains the no-successor retirement shape (retired in place at the subtree root). |
| `docs/RECORD-STANDARD.md` | Per-record obligations restated for role-class records: instance-evidence rows obligation; the retirement/supersession rule for party-form records. |
| `docs/EVIDENCE-STANDARD.md` | Dossier contract restated at class level: the chain carries the class corpus; profiles define capacities; party dossiers remain as retired-instance history. |
| `classifications/stakeholder-role-taxonomy.md` | Each of the 12 canonicalized classes gains its canonical record id; the 11 typified market-only classes are marked candidates (no enterprise engagement). |
| `catalog-research/CANDIDATE-REGISTER.md` | C-005: the 11 typified market-only role classes (evidence resolves; engagement absent — admit a class-record when engagement appears). |
| `entities/v1-alpha/README.md`, `CHANGELOG.md`, CR index, `CATALOG.yaml` | Topology note (12 canonical role records + 11 retired party subtrees), changelog entry, index row, regenerated index. |

## 2. NOT-List

- **No party record is deleted** — 11 retire; ids are assign-once, never recomputed (FOUNDATIONS §3, IDM-004).
- **No schema, gate, workflow, or id-system change** — the record shape, hash6 derivation, and every gate remain exactly as STRUCT-12/14 ratified them.
- **No ES-003 relationship-type change** — `enforces`/`publishes` remain the only asserted types, targets remain `dea:regulation-*`.
- **No market instance gains enterprise engagement** — their rows evidence classes only, per the STRUCT-15 honest discipline.
- **No new stakeholder_type** — the metamodel v1.0.0 enum is unchanged; the honest zeros (customer/partner/investor) stay zeros (C-002..C-004).
- **The 11 typified market-only classes are NOT admitted** — they stay candidates (C-005): typification evidences a class; admission requires the enterprise-engagement instance.

## 3. Acceptance criteria

- AC-01: 12 canonical role records validate (check_schema, check_id_system --strict); every id is freshly minted per FOUNDATIONS §3 with the record's slug and hash6.
- AC-02: The 11 party records read `lifecycle_status: retired` in place at their subtree roots (v1.1.0, `superseded-by` references, asserted edges relinquished to the role records); their subtree dossiers remain; no record file is removed.
- AC-03: CATALOG.yaml regenerates current: `canonical: 12`, `retired: 11`, `entities: 23`, per-entity `research_count: 4`, `research_files: 92`.
- AC-04: Every evidence row of the 133-row corpus appears in exactly one role record chain if its class is canonical (75 rows across the 12 canonical chains — the 11 named engaged instances plus market rows), with market rows explicitly asserting no engagement; the 58 rows of the 11 market-only classes stay in the taxonomy (C-005).
- AC-05: All gates green: catalog index (strict), pointer, schema, id system (strict), entity system (strict), authorship (strict), CST 16/16, tests.
- AC-06: Correlations targets all resolve to live sibling records; asserted edges equal the 8 STRUCT-14 edges re-expressed at role level (same targets, same types).

## 4. Follow-ons

- Workbook flat-file role catalog: DONE alongside this CR — the 12 canonical rows carry the minted record ids and paths, the evidence log's role ids and repo-status rows were re-pointed (engaged instances named, market rows asserting no engagement), and the summary integrity checks re-verified clean. The workbook remains the role-catalog working view.
- C-001 (enterprise anchor) and the deferred edges it blocks: unchanged.
- When enterprise engagement evidence appears for a candidate class (C-005), admit it as a role record on this pattern.
