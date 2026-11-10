# European data-protection authorities (EDPB and national DPAs) — evidence chain

> The exhaustive evidence chain for `stakeholders:stakeholder-eu-data-protection-authorities-rs8g75`: every row that grounds
> the record, what it verifies, and where it comes from (channels per
> `docs/FOUNDATIONS.md` §2; dossier contract per `docs/EVIDENCE-STANDARD.md`).
> Corpus rows carry stable `E-####` ids shared with the role taxonomy and the
> flat-file catalog. Verified 2026-11-10.

## 1. Admission evidence (the record's `external_references`)

- `official-website`: `https://edpb.europa.eu`
- `sibling-record`: `dea:regulation-eu-gdpr (dea-catalog-regulations)`

## 2. Typified corpus rows


### Class `gdpr-supervisory-authority` — GDPR supervisory authority

Role class `sh-role:gdpr-supervisory-authority` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0001 | 3 (public record) | official-website | https://www.aepd.es | https://www.aepd.es |
| E-0002 | 3 (public record) | official-website | https://www.dsb.gv.at | https://www.dsb.gv.at |
| E-0003 | 3 (public record) | official-website | https://autoriteitpersoonsgegevens.nl | https://autoriteitpersoonsgegevens.nl |
| E-0004 | 3 (public record) | official-website | https://www.autoriteprotectiondonnees.be | https://www.autoriteprotectiondonnees.be |
| E-0005 | 3 (public record) | official-website | https://www.cpdp.bg | https://www.cpdp.bg |
| E-0006 | 3 (public record) | official-website | https://www.cnpd.pt | https://www.cnpd.pt |
| E-0007 | 3 (public record) | official-website | https://www.cnil.fr | https://www.cnil.fr |
| E-0008 | 3 (public record) | official-website | https://www.cnpd.lu | https://www.cnpd.lu |
| E-0009 | 3 (public record) | official-website | https://www.azop.hr | https://www.azop.hr |
| E-0010 | 3 (public record) | official-website | https://www.datatilsynet.dk | https://www.datatilsynet.dk |
| E-0011 | 3 (public record) | official-website | https://www.datenschutzstelle.li | https://www.datenschutzstelle.li |
| E-0012 | 3 (public record) | official-website | https://www.dataprotection.ie | https://www.dataprotection.ie |
| E-0013 | 3 (public record) | official-website | https://www.dvi.gov.lv | https://www.dvi.gov.lv |
| E-0014 | 3 (public record) | official-website | https://www.aki.ee | https://www.aki.ee |
| E-0015 | 3 (public record) | official-website | https://www.garanteprivacy.it | https://www.garanteprivacy.it |
| E-0016 | 3 (public record) | official-website | https://www.bfdi.bund.de | https://www.bfdi.bund.de |
| E-0017 | 3 (public record) | official-website | https://www.dpa.gr | https://www.dpa.gr |
| E-0018 | 3 (public record) | official-website | https://www.naih.hu | https://www.naih.hu |
| E-0019 | 3 (public record) | official-website | https://www.personuvernd.is | https://www.personuvernd.is |
| E-0020 | 3 (public record) | official-website | https://www.ip-rs.si | https://www.ip-rs.si |
| E-0021 | 3 (public record) | official-website | https://www.dataprotection.ro | https://www.dataprotection.ro |
| E-0022 | 3 (public record) | official-website | https://www.datatilsynet.no | https://www.datatilsynet.no |
| E-0023 | 3 (public record) | official-website | https://uoou.gov.cz | https://uoou.gov.cz |
| E-0024 | 3 (public record) | official-website | https://dataprotection.gov.sk | https://dataprotection.gov.sk |
| E-0025 | 3 (public record) | official-website | https://www.dataprotection.gov.cy | https://www.dataprotection.gov.cy |
| E-0026 | 3 (public record) | official-website | https://www.tietosuoja.fi/en/ | https://www.tietosuoja.fi/en/ |
| E-0027 | 3 (public record) | official-website | https://www.idpc.org.mt | https://www.idpc.org.mt |
| E-0028 | 3 (public record) | official-website | https://uodo.gov.pl | https://uodo.gov.pl |
| E-0029 | 3 (public record) | official-website | https://vdai.lrv.lt | https://vdai.lrv.lt |
| E-0030 | 3 (public record) | official-website | https://www.imy.se | https://www.imy.se |

### Class `data-protection-coordination-authority` — Data-protection coordination authority

Role class `sh-role:data-protection-coordination-authority` in the taxonomy; stakeholder_type `regulator`; typified corpus rows for this party:

| evidence_id | channel | system | identifier | stakeholder_url |
|---|---|---|---|---|
| E-0031 | 2 (sibling-record anchor) | official-website | https://edpb.europa.eu | https://edpb.europa.eu |

Collective-capacity record: the GDPR supervisory class is evidenced by 30 national/EEA authority rows (E-0001..E-0030; 27 EU member states + 3 EEA-EFTA authorities participating via the EEA Agreement) plus the EDPB coordination row (E-0031).


## 3. Supporting evidence beyond the corpus

| channel | system | identifier | stakeholder_url | verifies |
|---|---|---|---|---|
| 2 (sibling-record anchor) | sibling-record | dea:regulation-eu-gdpr (dea-catalog-regulations) | — | the regime record this collective enforces (the asserted `enforces` edge target) |

## 4. Asserted edges carried by the record

- `enforces` -> `dea:regulation-eu-gdpr` — Regulation (EU) 2016/679 is enforced by the EDPB-coordinated national supervisory authorities; the sibling record anchors the jurisdiction (evidence channel 2).

## 5. Honest notes

- Rows without a `stakeholder_url` are recorded with the reason, never omitted.
- Market-instance rows that evidence a *class* but assert no enterprise
  engagement live only in `classifications/stakeholder-role-taxonomy.md`
  (candidate-side truth); this record's chain carries only rows for this party.
- Member-state DPA sub-records are intentionally not admitted individually: the collective record carries the class; individual authorities would need their own engagement evidence to justify separate records.
