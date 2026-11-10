# GitHub, Inc. — stakeholder profile

> Defining the stakeholder: what the party is, its goals, what it does, and how
> it engages the enterprise. Per `docs/EVIDENCE-STANDARD.md`; the record's
> description remains the normative one-liner — this profile expands it.

## Definition

GitHub, Inc. (a subsidiary of Microsoft Corporation) is the supplier operating the GitHub platform: git-based source-control hosting, pull-request review, Actions continuous integration, Packages delivery, Pages publishing, and organization-level governance tooling. In this catalog the record carries the enterprise's platform-supplier relationship: the TechNeHub Labs organization's repositories, CI pipelines, and public site all run on the stakeholder's platform.

The record's normative description (verbatim): *Platform supplier to TechNeHub Labs: GitHub, Inc. hosts every repository in the OpenDEA fleet — source control, CI runners (GitHub Actions), pull-request review, and the private-org access control that gates the catalog corpus. This record carries the supplier capacity only.*

## Mandate and goals

- Operate the platform's stated purpose: to be where developers build software (hosting, collaboration, and delivery for the world's code).
- Keep the hosted corpus available, durable, and secure (platform reliability, supply-chain security features such as secret scanning and dependency alerts).
- Sustain open-source ecosystems: free public hosting, open licensing workflows, and community tooling.
- Provide organizations governance surfaces (teams, permissions, audit trails) that enterprises rely on for platform governance.

## What they do

- Hosts git repositories for the technehub-labs organization, including this catalog's repository and the sibling OpenDEA catalog fleet.
- Executes the enterprise's CI: the `.github/workflows/*.yml` pipelines (validate, catalog-conformance, entity-system, authorship, allocation) run on GitHub-hosted Actions runners.
- Serves the organization's public community site via GitHub Pages (the technehub-labs.github.io surface).
- Provides pull-request review, issues, releases, and branch protection that the enterprise's change-request/PR landing discipline runs on.
- Operates platform-level security features (secret scanning, Dependabot-style dependency alerts) over the hosted corpus.

## Engagement with the enterprise

The enterprise consumes the platform as a supplier: every repository, every CI run, and the public community site operate on the stakeholder's infrastructure. The record's outward `serves`/`supplies` edges are deferred until the C-001 enterprise-anchor decision (candidate register); the dependency is nonetheless fully evidenced in-repo.

## Role classes (typified)

- `sh-role:source-control-and-ci-platform-supplier` — Source-control and CI platform supplier (stakeholder_type `supplier`); 1 corpus row(s) in this record's chain
- `sh-role:package-registry-supplier` — Package-registry supplier (stakeholder_type `supplier`); adjacent class, no separate assertion
