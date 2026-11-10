# Data-protection coordination authority — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-data-protection-coordination-authority-rj5pwj`: the **class corpus** — every
> `E-####` row that evidences the role class `sh-role:data-protection-coordination-authority` — the engaged
> instances for this enterprise, what each row verifies, and where it comes from
> (channels per `docs/FOUNDATIONS.md` §2; dossier contract per
> `docs/EVIDENCE-STANDARD.md`; class-first per CR-CATALOG-STRUCT-16).
> Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://edpb.europa.eu`
- `sibling-record`: `dea:regulation-eu-gdpr (dea-catalog-regulations)`

## 2. Class corpus (typified evidence for the class)

All 3 corpus rows of the class, from the role taxonomy
(`classifications/stakeholder-role-taxonomy.md`). Engaged rows assert enterprise
engagement; market rows assert none — they evidence the class only.

| evidence_id | named instance | jurisdiction | channel | stakeholder_url | status |
|---|---|---|---|---|---|
| E-0031 | European data-protection authorities (EDPB and national DPAs) | data-protection; eu | 2 (sibling-record anchor) | https://edpb.europa.eu | engaged instance (this enterprise) |
| E-0032 | European Data Protection Supervisor (EDPS) | data-protection; eu | 3 (public record) | https://edps.europa.eu | market instance (no enterprise engagement) |
| E-0033 | Global Privacy Assembly | global | 3 (public record) | https://globalprivacyassembly.org | market instance (no enterprise engagement) |

Engaged-instance rows for this enterprise: E-0031.

## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-eu-gdpr (dea-catalog-regulations) | — | the regime record this collective enforces (the asserted `enforces` edge target) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-eu-gdpr` — The GDPR is enforced by the coordination board and the national supervisory authorities it coordinates; for this enterprise the engaged instance is the EDPB with the national DPAs. The sibling record anchors the regime (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- Member-state DPA sub-records are intentionally not admitted individually: the collective record carries the class; individual authorities would need their own engagement evidence to justify separate records.

