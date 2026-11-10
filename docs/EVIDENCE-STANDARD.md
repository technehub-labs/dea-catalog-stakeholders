# Evidence-Chain & Dossier Standard (CR-CATALOG-STRUCT-15)

Every canonical Stakeholder record subtree carries a **research dossier**: the
exhaustive evidence chain, the stakeholder profile, and the cross-catalog
correlations. This document is the contract for those files. The admission
contract (evidence channels, id minting, relationship policy) remains
[`FOUNDATIONS.md`](FOUNDATIONS.md); the record obligations remain
[`RECORD-STANDARD.md`](RECORD-STANDARD.md); this standard extends both to the
subtree's `research/` directory.

## 1. Subtree layout

```
entities/v1-alpha/<slug>-<hash6>/
├── stakeholders-stakeholder-<slug>-<hash6>.yaml   # the record (unchanged)
├── README.md                                      # the record's README (RECORD-STANDARD §3)
└── research/                                     # the dossier (this standard)
    ├── README.md                                 # required (CST-009) — index + provenance
    ├── evidence-chain.md                         # required — every evidence row
    ├── stakeholder-profile.md                    # required — defining, goals, activities
    └── correlations.md                           # required — related entities
```

The `research/` directory is the sanctioned location for non-record material
(the regenerator counts it per-subtree; the schema and IDM gates scope
themselves to record YAMLs; the ES gate walks only `.yaml`/`.yml` — dossier
files are Markdown precisely so no gate can mistake them for records). Never
place evidence or profile material inside the record YAML: the schema is a
closed-world projection and stays one.

## 2. Evidence chain (`evidence-chain.md`)

The chain is **exhaustive**: every row that grounds the record is logged, with
its channel per FOUNDATIONS §2 (in-repo primary / sibling-record anchor / public
record). Contract:

1. **Admission evidence** — the record's `external_references` pairs, restated
   with their channel and what each verifies.
2. **Typified corpus rows** — the record's rows from the catalog's typified
   evidence corpus (`classifications/stakeholder-role-taxonomy.md`), carrying
   their stable `E-####` ids, channel, system, identifier, and `stakeholder_url`.
   Every row that names this party belongs here.
3. **Supporting evidence beyond the corpus** — additional verified rows (an
   enforcement portal, a standards library, an in-repo artifact), each with the
   channel and a `verifies` statement.
4. **Asserted edges** — restated from the record YAML (the record remains the
   normative source; the chain never widens an edge).
5. **Honest notes** — rows without a URL are kept with the reason, never
   dropped; deferred edges are restated verbatim from the record README.

A `stakeholder_url` is required wherever one truthfully exists (public-record
rows); a class-of-authorities with no single website is recorded with that
note rather than a fabricated URL. Rows carry a `Verified YYYY-MM-DD` date.

## 3. Stakeholder profile (`stakeholder-profile.md`)

Defining the stakeholder beyond the record's one-line description:

1. **Definition** — what the party is; the record's description quoted
   verbatim as the normative one-liner.
2. **Mandate and goals** — the party's stated mission/purpose, at
   mandate level (no unverifiable specifics; no numbers that rot).
3. **What they do** — the party's activities, kept to stable,
   public-record facts.
4. **Engagement with the enterprise** — the capacity in which this party
   engages the enterprise, consistent with the record's description.
5. **Role classes** — the `sh-role:*` taxonomy classes this party
   instantiates, with the corpus row counts.

The profile is documentation: it can justify an admission (steward review
reads it) but never substitutes for the evidence chain.

## 4. Role taxonomy (`classifications/stakeholder-role-taxonomy.md`)

The controlled vocabulary of reusable, jurisdiction-free role classes
(`sh-role:<slug>`) with the full typified corpus: 133 `E-####` rows. Classes
are capacities, never named parties; named parties are evidence instances.
Market-instance rows assert no enterprise engagement and live only in the
taxonomy (candidate-side truth, per the candidate register's honest-zero
discipline). Every canonical-party row is duplicated in its record's chain so
the chain stands alone.

## 5. Correlations (`correlations.md`)

Correlations document how a stakeholder relates to the enterprise's other
catalogs (regulations, capabilities, processes, services, actors). Contract:

1. **Documentation-grade only** — a correlation is NOT an ES-003 relationship
   instance. The record's asserted edges are only the registered types in its
   YAML; asserting a new edge type requires the FOUNDATIONS §4 CR process.
2. **Live targets only** — every target id must resolve to a live record in
   the sibling catalog (`capabilities:`, `processes:`, `services:`, `actors:`,
   `dea:regulation-*`) at authoring time; the target's lifecycle state is
   noted where not canonical.
3. **Basis required** — every correlation names its evidence (channel +
   artifact). A correlation without a basis is deleted, not excused.
4. **Deferred entries explicit** — natural targets that do not exist yet are
   recorded under `Deferred:` with the blocker, mirroring the record README's
   rule.

## 6. Provenance and authorship

Each dossier `research/README.md` carries the landing CR, the date, and the
authorship-bearing actor. The AUT cardinal rule applies to these files as it
does everywhere: authorship fields carry the human principal only.

## 7. What this standard does NOT change

- No schema change (`schemas/entity.schema.json` untouched).
- No new relationship types (ES-003 register untouched).
- No new admissions (records and their ids unchanged).
- No gate change (CST-009 already requires the research README; the gates
  scope themselves as designed).
