#!/usr/bin/env python3
"""Validate every Trinity Hub registry entry against its JSON Schema.

Checks, for each registry/<agents|skills>/<id>.yaml (files starting with "_" and
non-YAML files are skipped):
  1. parses as YAML
  2. validates against schemas/<agent|skill>_entry.schema.json
  3. filename stem == entry `id`
  4. a light "no secrets" scan (belt-and-suspenders; the schema also forbids tokens)

Exit code 0 on success, 1 if any entry fails. Run before opening a PR; CI runs it too.

    pip install pyyaml jsonschema
    python scripts/validate_registry.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("Missing deps. Run:  pip install pyyaml jsonschema")

ROOT = Path(__file__).resolve().parent.parent
KINDS = {
    "agents": "schemas/agent_entry.schema.json",
    "skills": "schemas/skill_entry.schema.json",
}
# Lines that look like a leaked credential. `scheme: bearer` / `auth:` are NOT flagged
# because the key name isn't a secret-bearing key.
SECRET_RE = re.compile(
    r"(?i)\b(token|secret|password|passwd|api[_-]?key|access[_-]?key|client[_-]?secret)\b\s*[:=]\s*\S",
)
PEM_RE = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")


def _load_schema(rel: str) -> Draft202012Validator:
    import json
    return Draft202012Validator(json.loads((ROOT / rel).read_text()))


def main() -> int:
    errors: list[str] = []
    total = 0
    for kind, schema_rel in KINDS.items():
        validator = _load_schema(schema_rel)
        d = ROOT / "registry" / kind
        if not d.exists():
            continue
        for f in sorted(d.glob("*.yaml")):
            if f.name.startswith("_"):
                continue
            total += 1
            rel = f.relative_to(ROOT)
            raw = f.read_text()

            # 1. no-secrets scan
            for i, line in enumerate(raw.splitlines(), 1):
                if SECRET_RE.search(line) or PEM_RE.search(line):
                    errors.append(f"{rel}:{i}: looks like a secret — registry entries must "
                                  f"never contain credentials: {line.strip()[:80]}")

            # 2. parse
            try:
                data = yaml.safe_load(raw)
            except yaml.YAMLError as e:
                errors.append(f"{rel}: invalid YAML: {e}")
                continue
            if not isinstance(data, dict):
                errors.append(f"{rel}: top-level YAML must be a mapping")
                continue

            # 3. schema
            for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
                loc = "/".join(str(p) for p in err.path) or "(root)"
                errors.append(f"{rel}: [{loc}] {err.message}")

            # 4. filename == id
            if data.get("id") != f.stem:
                errors.append(f"{rel}: id '{data.get('id')}' must equal filename stem '{f.stem}'")

    if errors:
        print(f"✗ {len(errors)} problem(s) across {total} entr(ies):\n")
        for e in errors:
            print("  -", e)
        return 1
    print(f"✓ all {total} registry entr(ies) valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
