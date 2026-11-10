# Stakeholders Candidate Register (CR-CATALOG-STRUCT-13)

Candidates are parties this catalog might admit but whose evidence does not
yet satisfy the admission contract (`docs/FOUNDATIONS.md` §2). Entries are
investigations, not pending work: a candidate closes ADMITTED (a canonical
record lands, with this register updated) or NOT-ADMITTED (the verdict and
reason recorded here — the capabilities repo's candidate-closure precedent,
CR-DEA-BC-68).

| id | Candidate | stakeholder_type | Evidence status | Verdict |
|---|---|---|---|---|
| C-001 | The enterprise itself (TechNeHub Labs as the anchor node for `serves`/`governs` targets) | — (anchor node, not a stakeholder) | No canonical enterprise record exists in any catalog; the Actors catalog holds performers, not the enterprise-as-party. | OPEN — blocks supplier-side outward edges (GitHub hosting, community's platform relation); when a canonical enterprise anchor is stood up, the deferred edges land. |
| C-002 | Customers of TechNeHub Labs | customer | No org-verifiable artifact names any customer; no contract, statement, or client record exists in-repo. | OPEN (honest zero) — admitted only when verifiable evidence exists. |
| C-003 | Partners / resellers of TechNeHub Labs | partner | No org-verifiable artifact names any partner. | OPEN (honest zero). |
| C-004 | Investors other than the owner | investor | No external investment instrument or investor record is verifiable in-repo. | OPEN (honest zero). |
| C-005 | The 11 typified market-instance role classes — `provincial-data-protection-authority`, `consumer-protection-regulator`, `cybersecurity-agency`, `intellectual-property-administration-authority`, `technical-standards-development-organization`, `telecommunications-standards-organization`, `telecommunications-regulator`, `internet-identifier-registry-operator`, `open-source-license-steward`, `open-source-ecosystem-foundation`, `package-registry-supplier` | various (`regulator` ×8, `supplier` ×2, `community` ×1 — see the role taxonomy) | Typified (>=3 URL evidence of named market instances each; CR-CATALOG-STRUCT-16 role-first restructure), but no org-verifiable artifact asserts any instance's engagement with TechNeHub Labs — the admission contract (FOUNDATIONS §2) is not satisfied. | OPEN (market evidence, no engagement) — a class-record lands when enterprise engagement is evidenced; the classes remain available in `classifications/stakeholder-role-taxonomy.md`. |

The first canonical tranche (CR-CATALOG-STRUCT-14) admits the parties whose
evidence DOES resolve today: the platform supplier, the OSS community, the
governing-board capacity, and eight regulators anchored one-to-one to the
regulations catalog's eight active `dea:regulation-*` records.

CR-CATALOG-STRUCT-16 restates the catalog's record identity at class level: the
tranche's 11 named-party records are retired (never deleted; `superseded-by`
references retained, their dossiers kept as engaged-instance history) and 12
jurisdiction-free role-class records land as the canonical set — the
generalization the flat-file role catalog and the taxonomy already carried.
C-005 records the classes the restructure typified but could not canonicalize:
market evidence without enterprise engagement stays a candidate, per the
admission contract.
