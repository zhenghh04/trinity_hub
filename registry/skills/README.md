# Skills registry

One YAML file per skill, named `<id>.yaml`, validated against
[`../../schemas/skill_entry.schema.json`](../../schemas/skill_entry.schema.json).

A skill is a reusable capability an agent *loads* — it has no endpoint and is not a
conversational participant (that's an [agent](../agents/)). The entry here is a **pointer** to
where the skill actually lives (`source.repo`).

## Add yours

```bash
cp _TEMPLATE.yaml <your-id>.yaml
$EDITOR <your-id>.yaml
python ../../scripts/validate_registry.py
python ../../scripts/build_index.py            # refresh ../INDEX.md
```

Then open a PR. Full guide: **[../../docs/contribute-a-skill.md](../../docs/contribute-a-skill.md)**.

## Rules

- Filename **must** equal `id`.
- **No secrets.** Never commit keys/tokens; list them as `requirements:` instead.
- `source.repo` must be an **HTTPS** URL.
- Files starting with `_` are ignored by the validator/index.

## Examples

- [`xanes-analysis.yaml`](xanes-analysis.yaml) — a materials-science spectroscopy skill.
