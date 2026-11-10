# Retired Records (State Grouping)

This directory is the **top-level state grouping** of the Stakeholders
catalog (entity-storage-layout §3.2, `dea-metaframework`
CR-CATALOG-STRUCT-12; adopted here by CR-CATALOG-STRUCT-17). Every direct
subdirectory is a fully-retired record subtree, moved here unchanged from
its former flat location so the canonical record set and the engagement
history are visually separated in the tree.

- Directory and record file names keep their id-derived form (IDM-005);
  a move recomputes nothing (ids are assign-once).
- Every record here carries `lifecycle_status: retired` and a
  `superseded-by` external reference to its canonical successor
  (CST-010 enforces the lifecycle agreement).
- The `research/` dossiers are retained as the engaged-instance history of
  the named parties of the first canonical tranche (CR-CATALOG-STRUCT-14):
  the record YAMLs remain the only normative artifacts; the dossiers are
  documentation-grade.

## Contents

The 11 retired party-form records, each superseded by its role-class
record (CR-CATALOG-STRUCT-16):

| Subtree | Superseded by |
|---|---|
| `california-privacy-protection-agency-mtxygk/` | `state-consumer-privacy-regulator-r9h6sp` |
| `eu-data-protection-authorities-rs8g75/` | `gdpr-supervisory-authority-qryy8j` |
| `eu-trade-secret-authorities-zwf29g/` | `trade-secret-enforcement-authority-2374nw` |
| `github-inc-msn3q2/` | `source-control-and-ci-platform-supplier-cbnhwy` |
| `governing-board-hgr5us/` | `governing-board-authority-2wdtyy` |
| `hhs-office-for-civil-rights-hf7e8x/` | `health-data-regulation-authority-yfkmah` |
| `oss-community-nf74fy/` | `open-source-licensee-community-57sarg` |
| `pci-security-standards-council-ek8khf/` | `payment-card-standards-body-bxqwjh` |
| `uk-information-commissioner-5e64th/` | `data-protection-supervisory-authority-48udqa` |
| `us-department-of-justice-nqbwya/` | `justice-enforcement-authority-hkuap7` |
| `us-securities-and-exchange-commission-ucaru6/` | `securities-and-markets-regulator-yeycka` |

The full record ids, versions, and evidence chains are in each subtree's
record YAML and `research/` dossier; `CATALOG.yaml` lists every entry with
`state: retired` and its grouped path.
