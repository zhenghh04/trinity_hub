<!-- Thanks for contributing to Trinity Hub! Please complete the checklist. -->

## What does this PR add or change?

<!-- e.g. "Register the Foo agent" / "Add the bar-analysis skill" / "Fix Super Ray endpoint" -->

## Type

- [ ] New agent (`registry/agents/<id>.yaml`)
- [ ] New skill (`registry/skills/<id>.yaml`)
- [ ] Update to an existing entry
- [ ] Docs / tooling

## Checklist

- [ ] **No secrets** — no tokens, keys, passwords, or `.env` content anywhere in the diff.
- [ ] `python scripts/validate_registry.py` passes locally.
- [ ] `python scripts/build_index.py` run and `registry/INDEX.md` committed.
- [ ] Filename equals the entry `id`.
- [ ] All `discovery` / `homepage` / `source.repo` URLs are **HTTPS**.
- [ ] I maintain or am authorized to list this agent/skill, and a real maintainer contact is present.

## Notes for reviewers

<!-- Anything special: pending TLS, experimental status, etc. -->
