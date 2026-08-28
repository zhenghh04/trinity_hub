# Connecting GitHub (GITHUB_TOKEN)

Set a **`GITHUB_TOKEN`** so Trinity can act on GitHub *as you* — read your private
repositories, open issues and pull requests, push branches, and leave comments.
The token is stored **per user** and is never shared with other tenants.

If you only ever ask Trinity about public repos, you don't need this. Set it as
soon as you want Trinity to touch a private repo or write anything back to GitHub.

## 1. Create the token

Create a **classic** personal access token (starts with `ghp_`):

1. Go to **GitHub → Settings → Developer settings → Personal access tokens →
   Tokens (classic)** →
   [Generate new token (classic)](https://github.com/settings/tokens).
2. Give it a name you'll recognize (e.g. `trinity`) and an expiry.
3. Select the scopes below.
4. Generate it and **copy the value now** — GitHub shows it only once.

| Scope | When you need it |
|---|---|
| `repo` | Always — read/write repositories (issues, PRs, pushes, private repos) |
| `read:org` | Only if you work with **organization-owned** repos |
| `workflow` | Only if Trinity must edit GitHub Actions workflow files |

!!! warning "Use a classic token, not a fine-grained PAT"
    Fine-grained PATs do **not** yet work reliably for repo-write operations
    through the `gh` CLI and some API calls. If issue/PR creation or `git push`
    fails with a permission error while a fine-grained token is set, switch to a
    classic token — that resolves it in almost every case.

## 2. Set it in Trinity

Open **Settings → Environment**, add a variable named exactly **`GITHUB_TOKEN`**,
paste the token value, and save. It's stored against your account (per-tenant,
never committed to a repo) and injected only when Trinity runs work on your
behalf. → [Settings](settings.md#environment)

!!! danger "Never paste the token into chat"
    Put the token **only** in Settings → Environment. Don't paste it into a chat
    message or a file — treat it like a password. To rotate it, replace the value
    in Settings → Environment (and revoke the old one on GitHub).

The `gh` CLI Trinity uses honors both `GITHUB_TOKEN` and `GH_TOKEN`; set
**`GITHUB_TOKEN`** — Trinity forwards it to `gh` automatically.

## 3. Verify it works

Ask Trinity, in a chat:

> Check my GitHub access — run `gh api user` and `gh repo view <owner>/<repo>`.

You should see your GitHub login and the repo's metadata. A good end-to-end check
is to ask Trinity to open a throwaway issue on a repo you own and then close it.

## Troubleshooting

**"not logged into any GitHub hosts" — even though the token is set.**
`gh` doesn't always pick the token up from the environment on its own. Trinity
forwards it explicitly; if you hit this in a raw shell, prefix the command:
`GH_TOKEN="$GITHUB_TOKEN" gh <command>` (or run `echo "$GITHUB_TOKEN" | gh auth
login --with-token`).

**403 / "Resource not accessible" when creating an issue or PR, or `git push`
rejected.** The token is missing a scope or is a fine-grained PAT. Recreate it as
a **classic** token with `repo` (add `read:org` for org repos) and update it in
Settings → Environment.

**"Bad credentials" / 401.** The token is wrong, expired, or was revoked.
Generate a new one and replace the value in Settings → Environment.

**Can read public repos but not your private ones.** The `repo` scope isn't
selected — recreate the token with `repo` checked.

Next: **[API access →](api-access.md)**
