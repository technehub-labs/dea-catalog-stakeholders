# Stakeholder Role Taxonomy (controlled vocabulary)

> CR-CATALOG-STRUCT-15. The controlled vocabulary of reusable, jurisdiction-free
> stakeholder role classes, with the typified evidence corpus: every evidence
> row (`E-####`) gathered for this catalog, grouped by class. A role class is a
> **capacity**, never a named party: named parties are evidence instances (in the
> canonical records' research dossiers, or candidate-side here). Classes reference
> the metamodel v1.0.0 `stakeholder_type` enum (`schemas/entity.schema.json`); they
> do not widen it. Verified 2026-11-10.

## Contract

- Class ids: `sh-role:<slug>` (documentation-grade; not entity ids).
- Typification rule: a class is typified by >= 3 evidence rows with a resolvable
  `stakeholder_url` pointing at the named instance. Two exceptions are carried by
  design and noted per class: the collective licensee community and the
  single-incumbent governing board (canonical capacities; 3 URL evidence surfaces each).
- Evidence rows live in exactly one home: rows for the canonical role classes are
  cross-referenced from (and duplicated in) their record dossiers; rows for
  market instances assert **no enterprise engagement** — they evidence a class only.
- Canonicalization (CR-CATALOG-STRUCT-16): a class whose enterprise-engagement
  instance is evidenced lands as a canonical role-class record
  (`entities/v1-alpha/<role-slug>-<hash6>/`); the record id
  (`stakeholders:stakeholder-<slug>-<hash6>`) and this file's class id
  (`sh-role:<slug>`) stay distinct — class ids are documentation-grade, record
  ids are entity ids. A class with typified market evidence but no engagement
  stays documentation-only (candidate register C-005).
- Honest zeros: no customer/partner/investor classes exist; the enum values remain
  empty by evidence, tracked as C-002..C-004 in the candidate register.

## The `stakeholder_type` enum (the classes' relationship kind)

| enum value | Role-type definition |
|---|---|
| `regulator` | External party holding statutory or regime authority over the enterprise's processing, products or commerce: empowered to enforce, supervise or adjudicate a regulation, or to develop and publish a standard that the enterprise must satisfy. Roles classified here are typified by >=3 logged URL evidence instances of named authorities. |
| `supplier` | External party that provides a platform, hosting, registry or other input the enterprise's processes depend on. The relationship class is supply; roles classified here are typified by >=3 logged URL evidence instances of the supplier class, with enterprise engagement asserted only where in-repo evidence exists. |
| `community` | External collective affected by or engaging the enterprise's corpus: open-source licensees, consumers, and the ecosystem stewards that author or certify the licenses it publishes under. Collective-capacity roles carry the threshold-not-applicable flag honestly. |
| `board` | The enterprise's directing or governing authority in its governance capacity only: ownership, ratification and release decisions. Single-incumbent by organization design; performer capacities are out of scope (Actors catalog boundary). |
| `customer` | External party that acquires or consumes the enterprise's products or services. Honest zero today: no org-verifiable customer evidence exists (candidate register C-002); no role records reference this type yet. |
| `partner` | External party engaged with the enterprise in joint commercial or delivery activity. Honest zero today (candidate register C-003); no role records reference this type yet. |
| `investor` | External party holding an ownership or investment interest. Honest zero for non-owner investors today (candidate register C-004); the owner's governance capacity is recorded under the board type, not here. |

## Classes by enum value

| enum value | classes | evidence rows |
|---|---|---|
| `regulator` | 17 | 111 |
| `supplier` | 2 | 6 |
| `community` | 3 | 13 |
| `board` | 1 | 3 |
| `customer` | 0 | 0 |
| `partner` | 0 | 0 |
| `investor` | 0 | 0 |

## `sh-role:gdpr-supervisory-authority` — GDPR supervisory authority

- stakeholder_type: `regulator`
- Definition: The supervisory authority competent for the GDPR within its jurisdiction, holding investigation, corrective and enforcement powers over the enterprise's jurisdiction-facing processing. Role record: the GDPR supervisory capacity is common across every GDPR-governed territory; the competent authority of each is carried as instance evidence, never as the record identity.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-gdpr-supervisory-authority-qryy8j` (`entities/v1-alpha/gdpr-supervisory-authority-qryy8j/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 30 (30 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0001 | Agencia Espanola de Proteccion de Datos (AEPD) | data-protection; eu; es | https://www.aepd.es |
| E-0002 | Austrian Data Protection Authority (Datenschutzbehoerde, DSB) | data-protection; eu; at | https://www.dsb.gv.at |
| E-0003 | Autoriteit Persoonsgegevens (Netherlands) | data-protection; eu; nl | https://autoriteitpersoonsgegevens.nl |
| E-0004 | Belgian Data Protection Authority (Autorite de protection des donnees / Gegevensbeschermingsautoriteit, APD-GBA) | data-protection; eu; be | https://www.autoriteprotectiondonnees.be |
| E-0005 | Bulgarian Commission for Personal Data Protection (CPDP) | data-protection; eu; bg | https://www.cpdp.bg |
| E-0006 | Comissao Nacional de Proteccao de Dados (Portugal, CNPD) | data-protection; eu; pt | https://www.cnpd.pt |
| E-0007 | Commission Nationale de l'Informatique et des Libertes (CNIL) | data-protection; eu; fr | https://www.cnil.fr |
| E-0008 | Commission Nationale pour la Protection des Donnees (Luxembourg, CNPD) | data-protection; eu; lu | https://www.cnpd.lu |
| E-0009 | Croatian Personal Data Protection Agency (AZOP) | data-protection; eu; hr | https://www.azop.hr |
| E-0010 | Danish Data Protection Agency (Datatilsynet, Denmark) | data-protection; eu; dk | https://www.datatilsynet.dk |
| E-0011 | Data Protection Authority of the Principality of Liechtenstein | data-protection; eea; li | https://www.datenschutzstelle.li |
| E-0012 | Data Protection Commission (Ireland, DPC) | data-protection; eu; ie | https://www.dataprotection.ie |
| E-0013 | Data State Inspectorate (Latvia, DVI) | data-protection; eu; lv | https://www.dvi.gov.lv |
| E-0014 | Estonian Data Protection Inspectorate (Andmekaitse Inspektsioon, AKI) | data-protection; eu; ee | https://www.aki.ee |
| E-0015 | Garante per la protezione dei dati personali (Italy) | data-protection; eu; it | https://www.garanteprivacy.it |
| E-0016 | German Federal Commissioner for Data Protection and Freedom of Information (BfDI) | data-protection; eu; de | https://www.bfdi.bund.de |
| E-0017 | Hellenic Data Protection Authority (Greece, DPA) | data-protection; eu; gr | https://www.dpa.gr |
| E-0018 | Hungarian National Authority for Data Protection and Freedom of Information (NAIH) | data-protection; eu; hu | https://www.naih.hu |
| E-0019 | Icelandic Data Protection Authority (Personuvernd) | data-protection; eea; is | https://www.personuvernd.is |
| E-0020 | Information Commissioner of the Republic of Slovenia | data-protection; eu; si | https://www.ip-rs.si |
| E-0021 | National Supervisory Authority for Personal Data Processing (Romania, ANSPDCP) | data-protection; eu; ro | https://www.dataprotection.ro |
| E-0022 | Norwegian Data Protection Authority (Datatilsynet, Norway) | data-protection; eea; no | https://www.datatilsynet.no |
| E-0023 | Office for Personal Data Protection (Czech Republic, UOOU) | data-protection; eu; cz | https://uoou.gov.cz |
| E-0024 | Office for Personal Data Protection (Slovakia) | data-protection; eu; sk | https://dataprotection.gov.sk |
| E-0025 | Office of the Commissioner for Personal Data Protection (Cyprus) | data-protection; eu; cy | https://www.dataprotection.gov.cy |
| E-0026 | Office of the Data Protection Ombudsman (Finland) | data-protection; eu; fi | https://www.tietosuoja.fi/en/ |
| E-0027 | Office of the Information and Data Protection Commissioner (Malta, IDPC) | data-protection; eu; mt | https://www.idpc.org.mt |
| E-0028 | Personal Data Protection Office (Poland, UODO) | data-protection; eu; pl | https://uodo.gov.pl |
| E-0029 | State Data Protection Inspectorate (Lithuania, VDAI) | data-protection; eu; lt | https://vdai.lrv.lt |
| E-0030 | Swedish Authority for Privacy Protection (Integritetsskyddsmyndigheten, IMY) | data-protection; eu; se | https://www.imy.se |

## `sh-role:data-protection-coordination-authority` — Data-protection coordination authority

- stakeholder_type: `regulator`
- Definition: The body coordinating or supervising data-protection enforcement above the single-jurisdiction level (a coordination board of national authorities, an institutional supervisor, or the global assembly of privacy regulators), engaging the enterprise through consistent-application decisions and cross-border enforcement coordination. Role record, typified by >=3 logged URL evidence instances; each named body is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-data-protection-coordination-authority-rj5pwj` (`entities/v1-alpha/data-protection-coordination-authority-rj5pwj/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0031 | European data-protection authorities (EDPB and national DPAs) | data-protection; eu | https://edpb.europa.eu |
| E-0032 | European Data Protection Supervisor (EDPS) | data-protection; eu | https://edps.europa.eu |
| E-0033 | Global Privacy Assembly | global | https://globalprivacyassembly.org |

## `sh-role:data-protection-supervisory-authority` — Data-protection supervisory authority

- stakeholder_type: `regulator`
- Definition: The supervisory authority enforcing a national data-protection regime (UK GDPR, FADP, PIPEDA, Privacy Act 1988, LGPD, PDPO, APPI, PDPA, NZ Privacy Act 2020, PIPL, PIPA and equivalents) with enforcement powers over the enterprise's jurisdiction-facing processing. Role record: the capacity is common across governed territories; each named authority is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-data-protection-supervisory-authority-48udqa` (`entities/v1-alpha/data-protection-supervisory-authority-48udqa/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 11 (11 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0034 | UK Information Commissioner's Office (ICO) | data-protection; uk | https://ico.org.uk |
| E-0035 | Cyberspace Administration of China (CAC) | data-protection; cn | http://www.cac.gov.cn |
| E-0036 | National Data Protection Authority of Brazil (ANPD) | data-protection; br | https://www.gov.br/anpd |
| E-0037 | Office of the Australian Information Commissioner (OAIC) | data-protection; au | https://www.oaic.gov.au |
| E-0038 | Office of the Privacy Commissioner (New Zealand) | data-protection; nz | https://www.privacy.org.nz |
| E-0039 | Office of the Privacy Commissioner for Personal Data (Hong Kong) | data-protection; hk | https://www.pcpd.org.hk |
| E-0040 | Office of the Privacy Commissioner of Canada (OPC) | data-protection; ca | https://www.priv.gc.ca |
| E-0041 | Personal Data Protection Commission (Singapore, PDPC) | data-protection; sg | https://www.pdpc.gov.sg |
| E-0042 | Personal Information Protection Commission (Japan, PPC) | data-protection; jp | https://www.ppc.go.jp |
| E-0043 | Personal Information Protection Commission (Republic of Korea, PIPC) | data-protection; kr | https://www.pipc.go.kr |
| E-0044 | Swiss Federal Data Protection and Information Commissioner (FDPIC) | data-protection; ch | https://www.edoeb.admin.ch |

## `sh-role:provincial-data-protection-authority` — Provincial data-protection authority

- stakeholder_type: `regulator`
- Definition: The data-protection authority of a provincial or sub-federal jurisdiction enforcing its own private-sector privacy statute (e.g. Canadian provincial PIPA/Law 25 regimes), with oversight of processing engaging the enterprise in that jurisdiction. Role record, typified by >=3 logged URL evidence instances; each province's authority is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0045 | Commission d'acces a l'information du Quebec (CAI) | data-protection; ca-qc | https://www.cai.gouv.qc.ca |
| E-0046 | Office of the Information and Privacy Commissioner for British Columbia (Canada) | data-protection; ca-bc | https://www.oipc.bc.ca |
| E-0047 | Office of the Information and Privacy Commissioner of Alberta (Canada) | data-protection; ca-ab | https://www.oipc.ab.ca |

## `sh-role:state-consumer-privacy-regulator` — State consumer-privacy regulator

- stakeholder_type: `regulator`
- Definition: The state or provincial authority holding rulemaking and enforcement powers under a subnational consumer-privacy statute (e.g. the CCPA as amended by the CPRA, the Colorado Privacy Act, the TDPSA, the VCDPA), over the enterprise's jurisdiction-facing processing. Role record: the capacity is common across governed subnational territories; the state agencies and attorneys general are instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-state-consumer-privacy-regulator-r9h6sp` (`entities/v1-alpha/state-consumer-privacy-regulator-r9h6sp/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 4 (4 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0048 | California Privacy Protection Agency (CPPA) and California Attorney General | privacy; us-ca | https://cppa.ca.gov |
| E-0049 | Colorado Attorney General (enforces the Colorado Privacy Act) | us-co | https://co.colorado.gov/law |
| E-0050 | Texas Attorney General (enforces the Texas Data Privacy and Security Act) | us-tx | https://www.texasattorneygeneral.gov |
| E-0051 | Virginia Attorney General (enforces the Virginia Consumer Data Protection Act) | us-va | https://www.virginia.gov/agencies/office-of-the-attorney-general/ |

## `sh-role:consumer-protection-regulator` — Consumer-protection regulator

- stakeholder_type: `regulator`
- Definition: The authority enforcing consumer-protection and fair-trading law against unfair or deceptive practices, including data-security cases, over commercial processing that engages the enterprise's consumer-facing commerce. Role record, typified by >=3 logged URL evidence instances across jurisdictions; each named authority is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0052 | Australian Competition and Consumer Commission (ACCC) | au | https://www.accc.gov.au |
| E-0053 | Competition and Markets Authority (CMA, UK) | uk | https://www.gov.uk/government/organisations/competition-and-markets-authority |
| E-0054 | US Federal Trade Commission (FTC) | consumer-protection; us | https://www.ftc.gov |

## `sh-role:health-data-regulation-authority` — Health-data regulation authority

- stakeholder_type: `regulator`
- Definition: The authority regulating the processing of health-related personal data (e.g. the HIPAA Privacy and Security Rules in the US, PHIPA health-information custodians in Ontario, HIQA's health-information framework in Ireland), with enforcement powers over the enterprise's health-data-touching processing. Role record: the health-data regulatory capacity is common across governed territories; the named offices are instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-health-data-regulation-authority-yfkmah` (`entities/v1-alpha/health-data-regulation-authority-yfkmah/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0055 | US HHS Office for Civil Rights (OCR) | health-data; us | https://www.hhs.gov/ocr |
| E-0056 | Health Information and Quality Authority (HIQA, Ireland) | ie | https://www.hiqa.ie |
| E-0057 | Information and Privacy Commissioner of Ontario (health-information capacity) | ca-on | https://www.ipc.on.ca |

## `sh-role:securities-and-markets-regulator` — Securities and markets regulator

- stakeholder_type: `regulator`
- Definition: The authority enforcing securities and markets law, including insider-trading prohibitions anchored in the regulations catalog, engaging the enterprise wherever securities-law duties attach. Role record, typified by >=3 logged URL evidence instances across jurisdictions; each named authority is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-securities-and-markets-regulator-yeycka` (`entities/v1-alpha/securities-and-markets-regulator-yeycka/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 4 (4 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0058 | US Securities and Exchange Commission (SEC) | securities; us | https://www.sec.gov |
| E-0059 | Australian Securities and Investments Commission (ASIC) | au | https://asic.gov.au |
| E-0060 | Financial Conduct Authority (FCA, UK) | uk | https://www.fca.org.uk |
| E-0061 | Ontario Securities Commission (OSC, Canada) | ca-on | https://www.osc.ca |

## `sh-role:justice-enforcement-authority` — Justice/enforcement authority

- stakeholder_type: `regulator`
- Definition: The justice department or equivalent enforcement authority prosecuting civil and criminal violations of national statute in national courts (including the Defend Trade Secrets Act (2016) in the US). Role record: the justice-enforcement capacity is common across governed territories; the named departments are instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-justice-enforcement-authority-hkuap7` (`entities/v1-alpha/justice-enforcement-authority-hkuap7/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 4 (4 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0062 | US Department of Justice (DOJ) | trade-secrets; us | https://www.justice.gov |
| E-0063 | Australian Attorney-General's Department | au | https://www.ag.gov.au |
| E-0064 | Department of Justice (Canada) | ca | https://www.justice.gc.ca |
| E-0065 | UK Ministry of Justice | uk | https://www.gov.uk/government/organisations/ministry-of-justice |

## `sh-role:trade-secret-enforcement-authority` — Trade-secret enforcement authority

- stakeholder_type: `regulator`
- Definition: The authority or court enforcing trade-secret protection statutes in national and supranational regimes (the Defend Trade Secrets Act in the US, Directive (EU) 2016/943 in member states, the Unfair Competition Prevention Act in Japan). Role record: the trade-secret enforcement capacity is common across governed territories; the named authorities and courts are instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-trade-secret-enforcement-authority-2374nw` (`entities/v1-alpha/trade-secret-enforcement-authority-2374nw/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 4 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0066 | EU member-state trade-secret authorities | trade-secrets; eu | *(no single URL — honest note in the class)* |
| E-0067 | Court of Justice of the European Union (CJEU) | eu | https://curia.europa.eu |
| E-0068 | Ministry of Economy, Trade and Industry (METI, Japan) | jp | https://www.meti.go.jp |
| E-0069 | US Department of Justice (trade-secret capacity, DTSA) | us | https://www.justice.gov |

## `sh-role:payment-card-standards-body` — Payment-card standards body

- stakeholder_type: `regulator`
- Definition: The industry standards body founded or owned by the card networks that maintains and publishes payment-card security and interoperability standards, governing the standards' content while compliance is enforced contractually through the networks' acceptance regimes. Role record, typified by >=3 logged URL evidence instances; each named body is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-payment-card-standards-body-bxqwjh` (`entities/v1-alpha/payment-card-standards-body-bxqwjh/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0070 | PCI Security Standards Council (PCI SSC) | payment-card | https://www.pcisecuritystandards.org |
| E-0071 | Accredited Standards Committee X9 (ANSI financial services) | us | https://x9.org |
| E-0072 | EMVCo (jointly owned by the card networks) | global | https://www.emvco.com |

## `sh-role:cybersecurity-agency` — Cybersecurity agency

- stakeholder_type: `regulator`
- Definition: The technical authority for cybersecurity whose advisories, baselines and secure-software guidance shape the security posture and supply-chain expectations on the enterprise's published software. Role record: the capacity is common across governed territories; each named agency is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 7 (7 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0073 | Agence nationale de la securite des systemes d'information (ANSSI) | cybersecurity; fr | https://cyber.gouv.fr |
| E-0074 | Australian Cyber Security Centre (ACSC) | cybersecurity; au | https://www.cyber.gov.au |
| E-0075 | Canadian Centre for Cyber Security | cybersecurity; ca | https://www.cyber.gc.ca |
| E-0076 | Cybersecurity and Infrastructure Security Agency (CISA) | cybersecurity; us | https://www.cisa.gov |
| E-0077 | European Union Agency for Cybersecurity (ENISA) | cybersecurity; eu | https://www.enisa.europa.eu |
| E-0078 | German Federal Office for Information Security (BSI) | cybersecurity; de | https://www.bsi.bund.de |
| E-0079 | UK National Cyber Security Centre (NCSC) | cybersecurity; uk | https://www.ncsc.gov.uk |

## `sh-role:intellectual-property-administration-authority` — Intellectual-property administration authority

- stakeholder_type: `regulator`
- Definition: The office administering copyright, trademark and design registration and policy for the works the enterprise publishes under open-source licenses, engaged by the corpus's copyright and licensing posture. Role record, typified by >=3 logged URL evidence instances; each named office is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 4 (4 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0080 | European Union Intellectual Property Office (EUIPO) | eu | https://www.euipo.europa.eu/en |
| E-0081 | Intellectual Property Office (UK) | uk | https://www.gov.uk/government/organisations/intellectual-property-office |
| E-0082 | United States Copyright Office | intellectual-property; us | https://www.copyright.gov |
| E-0083 | World Intellectual Property Organization (WIPO) | international | https://www.wipo.int |

## `sh-role:technical-standards-development-organization` — Technical standards-development organization

- stakeholder_type: `regulator`
- Definition: The standards body that develops and publishes the technical standards on which the enterprise's formats, protocols and security baselines rely. Role record, typified by >=3 logged URL evidence instances; each named body is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 14 (14 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0084 | Center for Internet Security (CIS) | security | https://www.cisecurity.org |
| E-0085 | Cloud Security Alliance | cloud | https://cloudsecurityalliance.org |
| E-0086 | Ecma International | international | https://www.ecma-international.org |
| E-0087 | Forum of Incident Response and Security Teams (FIRST) | security | https://www.first.org |
| E-0088 | IEEE Standards Association | international | https://standards.ieee.org |
| E-0089 | International Electrotechnical Commission (IEC) | international | https://www.iec.ch |
| E-0090 | International Organization for Standardization (ISO) | international | https://www.iso.org |
| E-0091 | Internet Engineering Task Force (IETF) | internet | https://www.ietf.org |
| E-0092 | OASIS Open | international | https://www.oasis-open.org |
| E-0093 | OWASP Foundation | security | https://owasp.org |
| E-0094 | US National Institute of Standards and Technology (NIST) | us | https://www.nist.gov |
| E-0095 | Unicode Consortium | international | https://home.unicode.org |
| E-0096 | Web Hypertext Application Technology Working Group (WHATWG) | web | https://whatwg.org |
| E-0097 | World Wide Web Consortium (W3C) | web | https://www.w3.org |

## `sh-role:telecommunications-standards-organization` — Telecommunications standards organization

- stakeholder_type: `regulator`
- Definition: The standards body developing and publishing telecommunications network and service standards, whose published specifications define the interfaces and security baselines for any telecommunications-touching engagement of the enterprise. Role record, typified by >=3 logged URL evidence instances; each named organization is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 5 (5 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0098 | 3rd Generation Partnership Project (3GPP) | international | https://www.3gpp.org |
| E-0099 | Alliance for Telecommunications Industry Solutions (ATIS) | us | https://www.atis.org |
| E-0100 | European Telecommunications Standards Institute (ETSI) | eu | https://www.etsi.org |
| E-0101 | International Telecommunication Union (ITU) | international | https://www.itu.int |
| E-0102 | TM Forum | international | https://www.tmforum.org |

## `sh-role:telecommunications-regulator` — Telecommunications regulator

- stakeholder_type: `regulator`
- Definition: The regulator licensing and supervising telecommunications networks, services and spectrum, whose lawful-access, interception, security and resilience obligations can engage telecommunications-touching processing of the enterprise. Role record: the capacity is common across governed territories; each named regulator is instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 6 (6 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0103 | Australian Communications and Media Authority (ACMA) | au | https://www.acma.gov.au |
| E-0104 | Autorite de regulation des communications electroniques (ARCEP, France) | fr | https://www.arcep.fr |
| E-0105 | Bundesnetzagentur (BNetzA, Germany) | de | https://www.bundesnetzagentur.de |
| E-0106 | Canadian Radio-television and Telecommunications Commission (CRTC) | ca | https://crtc.gc.ca |
| E-0107 | Federal Communications Commission (FCC, US) | us | https://www.fcc.gov |
| E-0108 | Ofcom (UK) | uk | https://www.ofcom.org.uk |

## `sh-role:internet-identifier-registry-operator` — Internet identifier and vulnerability registry operator

- stakeholder_type: `regulator`
- Definition: The operator of a global identifier registry (Internet parameter/port registries, DNS coordination, vulnerability identifiers) on which the enterprise's networked services and security communications rely. Role record, typified by >=3 logged URL evidence instances; the named operators are instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0109 | Internet Assigned Numbers Authority (IANA) | internet | https://www.iana.org |
| E-0110 | Internet Corporation for Assigned Names and Numbers (ICANN) | internet-governance; international | https://www.icann.org |
| E-0111 | MITRE Corporation (CVE Program) | security | https://www.cve.org |

## `sh-role:open-source-licensee-community` — Open-source licensee community

- stakeholder_type: `community`
- Definition: The community of external licensees and consumers of the enterprise's open-source corpus, affected by its licensing and publication decisions and distinct from internal performers (Actors catalog boundary). Collective-capacity role: the community is the evidence-bearing class itself, so the named-party typification threshold is not applicable; corpus artifacts log the evidence.
- Typification: n/a — collective capacity (canonical; 3 URL evidence surfaces of the collective)
- Canonical record: `stakeholders:stakeholder-open-source-licensee-community-57sarg` (`entities/v1-alpha/open-source-licensee-community-57sarg/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0112 | TechNeHub Labs open-source community | open-source | https://github.com/technehub-labs |
| E-0113 | TechNE Hub public community site | org | https://technehub-labs.github.io |
| E-0114 | technehub-labs corpus repositories (licensee surface) | org | https://github.com/technehub-labs/dea-catalog-stakeholders |

## `sh-role:open-source-license-steward` — Open-source license steward

- stakeholder_type: `community`
- Definition: The nonprofit steward that authors, maintains or certifies an open-source license under which the enterprise publishes (and the license-lineage voices that define what open source means), engaged by the enterprise's licensing decisions. Role record, typified by >=3 logged URL evidence instances; the named foundations are instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 6 (6 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0115 | Apache Software Foundation | open-source; licensing | https://www.apache.org |
| E-0116 | Eclipse Foundation | open-source; governance | https://www.eclipse.org |
| E-0117 | Free Software Foundation (FSF) | open-source; licensing | https://www.fsf.org |
| E-0118 | Open Source Initiative (OSI) | open-source; licensing | https://opensource.org |
| E-0119 | Rust Foundation | open-source; rust | https://foundation.rust-lang.org |
| E-0120 | Software Freedom Conservancy | open-source; compliance | https://sfconservancy.org |

## `sh-role:open-source-ecosystem-foundation` — Open-source ecosystem foundation

- stakeholder_type: `community`
- Definition: The foundation that hosts open-source projects, security initiatives or community programs within whose ecosystem the enterprise's corpus circulates, an affected party in the enterprise's publication and security practice. Role record, typified by >=3 logged URL evidence instances; the named foundations are instance evidence.
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 4 (4 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0121 | Cloud Native Computing Foundation (CNCF) | open-source; cloud | https://www.cncf.io |
| E-0122 | Internet Society | internet; open-standards | https://www.internetsociety.org |
| E-0123 | Linux Foundation | open-source; security | https://www.linuxfoundation.org |
| E-0124 | Python Software Foundation (PSF) | open-source; python | https://www.python.org |

## `sh-role:source-control-and-ci-platform-supplier` — Source-control and CI platform supplier

- stakeholder_type: `supplier`
- Definition: The external platform supplier hosting the enterprise's source control, CI runners, code review and organization access control. Role record, typified by >=3 logged URL evidence instances of the platform-supplier class; the named vendors are instance evidence (engagement asserted only where in-repo evidence exists).
- Typification: typified (>=3 URL evidence)
- Canonical record: `stakeholders:stakeholder-source-control-and-ci-platform-supplier-cbnhwy` (`entities/v1-alpha/source-control-and-ci-platform-supplier-cbnhwy/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0125 | GitHub, Inc. | platform; hosting | https://github.com |
| E-0126 | Atlassian (Bitbucket) | market | https://bitbucket.org |
| E-0127 | GitLab Inc. | market | https://about.gitlab.com |

## `sh-role:package-registry-supplier` — Package-registry supplier

- stakeholder_type: `supplier`
- Definition: The external registry supplier hosting the third-party packages the enterprise's toolchain installs at run time, engaged by the supply chain and its security posture. Role record, typified by >=3 logged URL evidence instances of the registry-supplier class; the named registries are instance evidence (engagement asserted only where in-repo evidence exists).
- Typification: typified (>=3 URL evidence)
- Canonical record: none — typified market-instance class; no enterprise engagement is evidenced (candidate register C-005).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0128 | Python Package Index (PyPI) | registry; python | https://pypi.org |
| E-0129 | RubyGems.org | market | https://rubygems.org |
| E-0130 | npm (GitHub/Microsoft) | market | https://www.npmjs.com |

## `sh-role:governing-board-authority` — Governing board / directing authority

- stakeholder_type: `board`
- Definition: The governing-board capacity directing the enterprise: organization ownership, change-request ratification and release decisions. Single-incumbent role by organization design, so the named-party typification threshold is not applicable; the officeholder is instance evidence, and any performer capacity is out of scope here (Actors catalog boundary, docs/FOUNDATIONS.md s1).
- Typification: n/a — single-incumbent capacity (canonical; 3 URL evidence surfaces of one officeholder)
- Canonical record: `stakeholders:stakeholder-governing-board-authority-2wdtyy` (`entities/v1-alpha/governing-board-authority-2wdtyy/`; CR-CATALOG-STRUCT-16) — the class carries an evidenced enterprise-engagement instance (named in the record's evidence chain).
- Corpus rows: 3 (3 with a `stakeholder_url`)

| evidence_id | named instance | jurisdiction | stakeholder_url |
|---|---|---|---|
| E-0131 | Emmanuel A. Otchere (governing board) | governance | https://github.com/eaojnr |
| E-0132 | dea-catalog-stakeholders repository (maintainer surface) | org | https://github.com/technehub-labs/dea-catalog-stakeholders |
| E-0133 | technehub-labs organization (ownership surface) | org | https://github.com/technehub-labs |

