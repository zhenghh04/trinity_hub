# Governance

Trinity Hub is a lightly curated registry. The goal is low-friction contribution with enough
review to keep entries safe, accurate, and secret-free.

## Roles

- **Contributors** — anyone who opens a PR or issue to add/update an agent or skill.
- **Maintainers** — review and merge PRs, triage issues, and keep the schema/CI healthy.
  The current maintainer is the Trinity Agent Hub team (ALCF / Argonne National Laboratory).

## Review checklist (what a maintainer verifies before merge)

1. **Schema-valid** — CI is green (`scripts/validate_registry.py`).
2. **No secrets** — no tokens, keys, passwords, or private credentials anywhere in the diff.
3. **HTTPS** — every discovery/endpoint URL is `https://`.
4. **Ownership** — the submitter maintains or is authorized to list the agent/skill, and a
   real maintainer contact is present.
5. **Sanity** — id is unique and stable; description/domains/skills are accurate and not spam.
6. **Index** — `registry/INDEX.md` reflects the change (CI checks this).

## Acceptance & curation

- Entries that pass review are merged as-is. Maintainers may request edits for clarity.
- Entries are **descriptors, not endorsements** — listing an agent is not a security or
  quality guarantee. Operators decide what to actually register and run in their Trinity.
- **Removal / deprecation:** an entry may be marked `deprecated` (or removed) if its endpoint
  is persistently unreachable, it violates the Code of Conduct, it leaks secrets, or the
  maintainer requests it. Security issues are acted on immediately
  (see [docs/security.md](docs/security.md)).

## Changing the schema or process

Schema and tooling changes go through a PR like anything else, but require a maintainer to
confirm backward compatibility (existing entries must still validate, or be migrated in the
same PR).

## Decision making

Day-to-day decisions are made by maintainers via PR review. Disagreements are resolved by
discussion in the issue/PR; the maintainer team has the final call.
