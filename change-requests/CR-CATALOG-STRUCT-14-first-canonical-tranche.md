# CR-CATALOG-STRUCT-14: First Canonical Tranche (11 Stakeholder Records)

**Status**: Proposed
**Layer**: L1 (Stakeholders Catalog)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-08
**Trigger**: Owner directive 2026-11-08 to advance the catalog to an active, well-enriched state; the tranche decision (same day): admit the full evidence-gated set, including the owner's governing-board capacity record. Executes the CR-CATALOG-STRUCT-13 contract against the regulations catalog's eight active records and the fleet's own artifacts. Authored agent-side on eaojnr's behalf; agency recorded here per the CR-BP-118 cardinal rule.
**Carrier**: this file
**Lands against**: `main` @ `e69fd61` (post CR-CATALOG-STRUCT-13, PR #16)
**Depends on**: CR-CATALOG-STRUCT-12, CR-CATALOG-STRUCT-13

## 1. Admitted records

The catalog's first canonical tranche: 3 organisation/governance/community records + 8 regulators, one-to-one with the regulations catalog's eight active `dea:regulation-*` records (each edge targets a live sibling record — evidence channel 2; official websites cited as public record — channel 3; the enterprise's own artifacts are channel 1 for the supplier/community/board capacities).

| id | Name | stakeholder_type | Edge(s) |
|---|---|---|---|
| `stakeholders:stakeholder-github-inc-msn3q2` | GitHub, Inc. | supplier | — (Deferred: C-001 enterprise anchor) |
| `stakeholders:stakeholder-oss-community-nf74fy` | TechNeHub Labs open-source community | community | — (Deferred: C-001) |
| `stakeholders:stakeholder-governing-board-hgr5us` | Emmanuel A. Otchere (governing board) | board | — (Deferred: C-001) |
| `stakeholders:stakeholder-eu-data-protection-authorities-rs8g75` | European data-protection authorities (EDPB and national DPAs) | regulator | `enforces` → `dea:regulation-eu-gdpr` |
| `stakeholders:stakeholder-eu-trade-secret-authorities-zwf29g` | EU member-state trade-secret authorities | regulator | `enforces` → `dea:regulation-eu-trade-secrets-directive` |
| `stakeholders:stakeholder-uk-information-commissioner-5e64th` | UK Information Commissioner's Office (ICO) | regulator | `enforces` → `dea:regulation-uk-gdpr` |
| `stakeholders:stakeholder-california-privacy-protection-agency-mtxygk` | California Privacy Protection Agency (CPPA) and California Attorney General | regulator | `enforces` → `dea:regulation-us-ccpa-cpra` |
| `stakeholders:stakeholder-pci-security-standards-council-ek8khf` | PCI Security Standards Council (PCI SSC) | regulator | `publishes` → `dea:regulation-pci-dss` |
| `stakeholders:stakeholder-us-securities-and-exchange-commission-ucaru6` | US Securities and Exchange Commission (SEC) | regulator | `enforces` → `dea:regulation-us-securities-insider-trading` |
| `stakeholders:stakeholder-hhs-office-for-civil-rights-hf7e8x` | US HHS Office for Civil Rights (OCR) | regulator | `enforces` → `dea:regulation-us-hipaa` |
| `stakeholders:stakeholder-us-department-of-justice-nqbwya` | US Department of Justice (DOJ) | regulator | `enforces` → `dea:regulation-us-dtsa` |

Tranche decisions worth recording:

- **The EU trade-secrets directive gets its own record** (member-state competent authorities and courts) rather than overloading the EU DPAs record — the enforcing sets are legally distinct.
- **PCI SSC carries `publishes`, not `enforces`**: the sibling record describes PCI DSS as the global *contractual* regime; the council governs the standard's content while the card networks enforce acceptance.
- **The board record carries the governance capacity only** (name + capacity; no contact details) — the Actors boundary per FOUNDATIONS §1; the description states the dual-capacity rule.
- **Records 1–3 assert no edges**: their natural targets (`serves`/`governs` onto the enterprise) await the C-001 enterprise-anchor decision (candidate register). Each README carries the explicit `Deferred:` note per RECORD-STANDARD §1.6.

## 2. Changes

| Area | Change |
|---|---|
| `entities/v1-alpha/<slug>-<hash6>/` | 11 new record subtrees, each with the record YAML (metamodel-faithful projection; `lifecycle_status: active`, `version: 1.0.0`) + per-record README (IDM-007) per the RECORD-STANDARD §3 template. Ids minted per the refined FOUNDATIONS §3 derivation (id line elided + self-ids normalized to `<SELF>`; sha256[:4] big-endian mod 31^6, MSB-first over the 31-symbol alphabet) — reproducible, no fixed-point search; minting tool: workspace `tools/emit_sh_records.py` against spec `tools/spec-sh-tranche-1.json` (both retained as the audit trail). |
| `docs/FOUNDATIONS.md` §3 | The hash-derivation refinement above, recorded in the contract (supersedes the STRUCT-13 wording). |
| `reconciliation/entity-system-registry.yaml` | ES-002 `profiles.Stakeholder` registered: `required_fields: [stakeholder_type, lifecycle_status, external_references]` (the RECORD-STANDARD §1 obligations beyond CST-004's id/type/name/version/lifecycle_status). |
| `CATALOG.yaml` | Regenerated as the final commit action: 11 canonical entities; `open_change_requests` arithmetic unchanged at 1 (this carrier). |

## 3. NOT-List

- **No customers/partners/investors admitted** — candidate register C-002..C-004 remain honest zeros; admission awaits verifiable evidence.
- **No enterprise-anchor record invented** — C-001 stays open; deferred edges stay deferred.
- **No new relationship types** — `enforces`/`publishes` were registered by STRUCT-13; nothing asserted outside the registered set.
- **No schema changes** — the STRUCT-12 projection validates all 11 records as-is.
- **No stakeholder_type widening** — all records use the metamodel's 7-value enum.

## 4. Acceptance criteria

- AC-01 All 11 ids above resolve as canonical records at the IDM-005 paths; `check_id_system.py --strict` CONFORMANT (11 records, 0 findings; this CR references every id — IDM-008 coherence on the PR).
- AC-02 `check_schema.py` reports 11 records validating against the projection; fixtures behave.
- AC-03 `check_entity_system.py --strict` CONFORMANT: every record's `type` passes the registered Stakeholder profile; every asserted edge uses a registered canonical type with `source_types: [Stakeholder]`.
- AC-04 `CATALOG.yaml` shows `canonical: 11`, per-entity `state: canonical` entries with the hyphen-form paths; regenerator `--check` exit 0.
- AC-05 Every record subtree carries a README.md with the five RECORD-STANDARD sections; the three deferred records carry explicit `Deferred:` notes; the description blockquote equals the record `description` verbatim.
- AC-06 All other local gates pass (`check_pointer`, `check_authorship`, `check_catalog_index`, pytest 62).
- AC-07 CHANGELOG `[Unreleased]` entry; CR index row; CR-CATALOG-STRUCT-13 status closed to `Merged (PR #16)` (standing discipline).

## 5. Follow-ons (named, not in this CR)

- C-001 enterprise-anchor decision (where the enterprise-as-party node lives) → unblocks the three deferred edges.
- Root-model lifecycle flip (`dea:entity-stakeholder` `scaffold` → `existing`) in dea-architecture-framework + governance register refresh.
- Future tranches: candidate-register resolutions, any new regulator anchored to future regulation records.
