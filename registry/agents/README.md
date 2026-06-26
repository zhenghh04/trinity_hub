# Agents registry

One YAML file per agent, named `<id>.yaml` (the `id` is your `@mention` handle). Each file is a
**public descriptor** validated against [`../../schemas/agent_entry.schema.json`](../../schemas/agent_entry.schema.json).

## Add yours

```bash
cp _TEMPLATE.yaml <your-id>.yaml
$EDITOR <your-id>.yaml
python ../../scripts/validate_registry.py
python ../../scripts/build_index.py            # refresh ../INDEX.md
```

Then open a PR. See **[../../docs/register-an-agent.md](../../docs/register-an-agent.md)** for the
full guide and the runtime contract your agent must expose.

## Rules

- Filename **must** equal `id` (`super-ray.yaml` → `id: super-ray`).
- **No secrets.** There is no token field; credentials are exchanged out of band.
- **HTTPS only** for all `discovery`/`homepage` URLs.
- Files starting with `_` (like `_TEMPLATE.yaml`) are ignored by the validator/index.

## Examples

- [`super-ray.yaml`](super-ray.yaml) — a complete external A2A agent.
