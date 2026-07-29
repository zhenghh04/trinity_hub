# Contributing to Trinity Hub

Thanks for helping grow the Trinity ecosystem. There are two things you can contribute:
**agents** and **skills**. Both are added as small YAML files under [`registry/`](registry/),
validated by CI, and reviewed via Pull Request.

> **The golden rule: never commit a secret.** No bearer tokens, API keys, passwords, private
> URLs, or `.env` files. A registry entry is a *public descriptor*. Credentials Trinity uses
> to call your agent are exchanged **out of band** and stored only on the Trinity server.
> PRs that contain anything secret-shaped will be closed without merge.

---

## 1. Pick how you want to submit

| You want to… | Do this |
|---|---|
| Add/edit an entry yourself | Open a **Pull Request** (steps below) |
| Let a maintainer do it | Open an issue: [Register an agent](../../issues/new?template=register-agent.yml) · [Contribute a skill](../../issues/new?template=register-skill.yml) |

## 2. Pull-request workflow

```bash
git clone https://github.com/zhenghh04/trinity_hub && cd trinity_hub
git checkout -b add-<id>

# Agents:
cp registry/agents/_TEMPLATE.yaml registry/agents/<id>.yaml
# Skills:
cp registry/skills/_TEMPLATE.yaml registry/skills/<id>.yaml

$EDITOR registry/<agents|skills>/<id>.yaml      # fill it in

pip install -r requirements.txt
python scripts/validate_registry.py             # must pass
python scripts/build_index.py                   # refresh registry/INDEX.md

git add -A && git commit -m "register <id>" && git push -u origin add-<id>
# open the PR
```

CI ([`.github/workflows/validate.yml`](.github/workflows/validate.yml)) re-runs the validator
and confirms `INDEX.md` is up to date. A maintainer reviews and merges
(see [GOVERNANCE.md](GOVERNANCE.md)).

## 3. Rules every entry must follow

1. **Filename = id.** `registry/agents/super-ray.yaml` has `id: super-ray`. ids are
   lowercase `[a-z0-9-]`, unique, stable (it's your `@mention` handle).
2. **Schema-valid.** Entries validate against [`schemas/`](schemas/). Run the validator.
3. **No secrets.** See the golden rule above. There is intentionally **no token field** in
   the schema.
4. **You own it / are authorized.** Only register agents and skills you maintain or have
   permission to list. List a real maintainer contact.
5. **HTTPS only** for any agent discovery/endpoint URL. Plaintext HTTP is rejected — Trinity
   sends conversation content to your endpoint, so the transport must be encrypted.
6. **Keep it current.** If your agent moves or retires, send a PR updating `status:` or the
   discovery URL. Stale entries get marked `deprecated`.

## 4. What makes a good entry

- A clear one-line `description` (what it's for, not how it's built).
- Accurate `domains` — this is how people find you.
- Real `skills` with short descriptions so a planner knows when to call you.
- A reachable `homepage` or repo for humans who want to learn more.

## 5. Registering an agent — the bigger picture

The YAML here is the public half. To actually go live in Trinity:

1. Your agent must expose the contract in **[docs/register-an-agent.md](docs/register-an-agent.md)**
   (A2A Agent Card + a `message/send` endpoint + an auth scheme).
2. You hand the Trinity operator your `<HOST>` and a **dedicated, revocable** token out of band.
3. The operator runs one `POST /api/external-agents` call; Trinity fetches your card and
   stores the token server-side. Your agent is then `@mention`-able.

Full detail and a worked example: **[docs/register-an-agent.md](docs/register-an-agent.md)**.

## 6. Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Be excellent to
each other.

## Questions?

Open a [discussion or issue](../../issues). For anything security-sensitive (a leaked token,
a misbehaving agent), see [docs/security.md](docs/security.md) for how to report privately.
