#!/usr/bin/env python3
"""Operator tool: register Trinity Hub agents into a running Trinity server.

Reads every `registry/agents/<id>.yaml` and POSTs each to
`<trinity-url>/api/external-agents`, turning a curated registry into live,
@mention-able agents. Run by a **Trinity operator** against *their* server.

Credentials are NOT in the registry. Per-agent tokens come from a separate,
git-ignored tokens file (or are omitted, leaving the agent registered as
`pending` until a token is supplied). The operator's own bearer (to call the
admin API) comes from --operator-token or $TRINITY_OPERATOR_TOKEN.

    pip install pyyaml
    # dry run — prints what would be sent, tokens redacted:
    python scripts/sync_to_trinity.py --trinity-url https://trinity.example --dry-run
    # real run:
    export TRINITY_OPERATOR_TOKEN=...           # admin/session bearer for the API
    python scripts/sync_to_trinity.py --trinity-url https://trinity.example \
        --tokens-file operator-tokens.yaml      # git-ignored; {agent-id: "<token>"}

Tokens file (YAML or JSON), git-ignored, never committed:
    super-ray: "the-bearer-token-super-ray-issued-us"
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing deps. Run:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "registry" / "agents"


def _load_entries(only: str | None, statuses: set[str]) -> list[dict]:
    out = []
    for f in sorted(AGENTS_DIR.glob("*.yaml")):
        if f.name.startswith("_"):
            continue
        try:
            data = yaml.safe_load(f.read_text()) or {}
        except yaml.YAMLError as e:
            sys.exit(f"{f.relative_to(ROOT)}: invalid YAML: {e}")
        if not isinstance(data, dict) or not data.get("id"):
            continue
        if only and data["id"] != only:
            continue
        if data.get("status", "pending") not in statuses:
            continue
        out.append(data)
    return out


def _load_tokens(path: str | None) -> dict:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        sys.exit(f"tokens file not found: {path}")
    try:
        return yaml.safe_load(p.read_text()) or {}
    except yaml.YAMLError as e:
        sys.exit(f"{path}: invalid YAML: {e}")


def _body_for(entry: dict, token: str) -> dict:
    disc = entry.get("discovery", {}) or {}
    auth = entry.get("auth", {}) or {}
    body = {
        "id": entry["id"],
        "name": entry.get("name", ""),
        "protocol": entry.get("protocol", "a2a"),
        "domains": entry.get("domains") or [],
        "description": entry.get("description", ""),
        "icon": entry.get("icon", ""),
        "color": entry.get("color", ""),
        "auth_scheme": auth.get("scheme", "none"),
    }
    if auth.get("header"):
        body["auth_header"] = auth["header"]
    if disc.get("card_url"):
        body["card_url"] = disc["card_url"]
    if disc.get("endpoint"):
        body["endpoint"] = disc["endpoint"]
    if token and body["auth_scheme"] != "none":
        body["auth_token"] = token
    return body


def _post(url: str, body: dict, op_token: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), method="POST",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {op_token}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read().decode()[:2000]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:2000]
    except Exception as e:                                    # noqa: BLE001
        return 0, str(e)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trinity-url", required=True, help="base URL of the Trinity server")
    ap.add_argument("--operator-token", default=os.environ.get("TRINITY_OPERATOR_TOKEN", ""),
                    help="admin/session bearer to call the API (or $TRINITY_OPERATOR_TOKEN)")
    ap.add_argument("--tokens-file", default="", help="git-ignored YAML/JSON: {agent-id: token}")
    ap.add_argument("--only", default="", help="register just this agent id")
    ap.add_argument("--status", default="pending,active",
                    help="comma-separated statuses to sync (default: pending,active)")
    ap.add_argument("--dry-run", action="store_true", help="print bodies (tokens redacted), don't POST")
    args = ap.parse_args()

    statuses = {s.strip() for s in args.status.split(",") if s.strip()}
    entries = _load_entries(args.only or None, statuses)
    tokens = _load_tokens(args.tokens_file or None)
    if not entries:
        print("no matching agents in registry/agents/")
        return 0
    if not args.dry_run and not args.operator_token:
        sys.exit("missing --operator-token (or $TRINITY_OPERATOR_TOKEN)")

    url = args.trinity_url.rstrip("/") + "/api/external-agents"
    ok = fail = 0
    for e in entries:
        aid = e["id"]
        token = tokens.get(aid, "")
        body = _body_for(e, token)
        scheme = body["auth_scheme"]
        if scheme != "none" and not token:
            print(f"⚠ {aid}: no token in tokens file — registering as pending (not callable yet)")

        if args.dry_run:
            shown = dict(body)
            if "auth_token" in shown:
                shown["auth_token"] = "***REDACTED***"
            print(f"\n[dry-run] POST {url}\n" + json.dumps(shown, indent=2, ensure_ascii=False))
            continue

        code, resp = _post(url, body, args.operator_token)
        if code in (200, 201):
            ok += 1
            print(f"✓ {aid}: {code}")
        else:
            fail += 1
            print(f"✗ {aid}: {code} {resp}")

    if not args.dry_run:
        print(f"\ndone: {ok} registered, {fail} failed, of {len(entries)} matched")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
