# Source-control and CI platform supplier — stakeholder profile (role class)

> Defining the role class: what the capacity is, its goals, what the class does,
> and which named instances engage the enterprise. Per
> `docs/EVIDENCE-STANDARD.md`; the record's description remains the normative
> one-liner — this profile expands it. CR-CATALOG-STRUCT-16: this record is the
> role class; named parties are instance evidence, never the record identity.

## Definition

The external platform supplier hosting the enterprise's source control, CI runners, code review and organization access control. Role record, typified by >=3 logged URL evidence instances of the platform-supplier class; the named vendors are instance evidence (engagement asserted only where in-repo evidence exists).

The record's normative description (verbatim): *The external platform supplier hosting the enterprise's source control, CI runners, code review and organization access control. Role record, typified by >=3 logged URL evidence instances of the platform-supplier class; the named vendors are instance evidence (engagement asserted only where in-repo evidence exists). Role-class record (CR-CATALOG-STRUCT-16): the named parties that hold this capacity are instance evidence, never the record identity; for this enterprise the engaged instance is GitHub, Inc. (host of every repository in the fleet).*

## Mandate and goals

(Class capacity, expanded from the engaged instances' mandate.)

- Operate the platform's stated purpose: to be where developers build software (hosting, collaboration, and delivery for the world's code).
- Keep the hosted corpus available, durable, and secure (platform reliability, supply-chain security features such as secret scanning and dependency alerts).
- Sustain open-source ecosystems: free public hosting, open licensing workflows, and community tooling.
- Provide organizations governance surfaces (teams, permissions, audit trails) that enterprises rely on for platform governance.

## What the class does

- Hosts git repositories for the technehub-labs organization, including this catalog's repository and the sibling OpenDEA catalog fleet.
- Executes the enterprise's CI: the `.github/workflows/*.yml` pipelines (validate, catalog-conformance, entity-system, authorship, allocation) run on GitHub-hosted Actions runners.
- Serves the organization's public community site via GitHub Pages (the technehub-labs.github.io surface).
- Provides pull-request review, issues, releases, and branch protection that the enterprise's change-request/PR landing discipline runs on.
- Operates platform-level security features (secret scanning, Dependabot-style dependency alerts) over the hosted corpus.

## Engagement with the enterprise (named instances)

For this enterprise the engaged instance is GitHub, Inc. (host of every repository in the fleet)
(corpus rows: E-0125).

The enterprise consumes the platform as a supplier: every repository, every CI run, and the public community site operate on the stakeholder's infrastructure. The record's outward `serves`/`supplies` edges are deferred until the C-001 enterprise-anchor decision (candidate register); the dependency is nonetheless fully evidenced in-repo.

## Retired party record (engaged-instance history)

- `stakeholders:stakeholder-github-inc-msn3q2` — retired by CR-CATALOG-STRUCT-16, superseded by this record; its
  dossier remains at `entities/v1-alpha/github-inc-msn3q2/research/` as the
  engaged-instance history.
