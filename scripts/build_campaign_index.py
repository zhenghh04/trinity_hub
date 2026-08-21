#!/usr/bin/env python3
"""Regenerate docs/campaigns/campaigns.json — data behind the "All campaigns" index.

Scans every campaign page (docs/campaigns/*/*.md except index.md) and extracts
the title plus the `**Key:** value · **Key:** value` metadata line each page
carries under its heading. No hand-curated data: if it isn't on the page, it
isn't in the index.

Deterministic (sorted by category, then path). Run after adding/editing a page:

    python scripts/build_campaign_index.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAMPAIGNS = ROOT / "docs" / "campaigns"
OUT = CAMPAIGNS / "campaigns.json"

CATEGORIES = {
    "trinity-runs": "Trinity runs",
    "science-campaigns": "Autonomous science",
    "engineering": "Performance engineering",
    "papers": "Paper reproductions",
}

# Known systems, for the facet filter (matched case-insensitively in metadata).
SYSTEMS = ["Aurora", "Cerebras", "Crux", "Frontier", "Odo", "Perlmutter",
           "Polaris", "Sirius", "Sophia", "Sunspot", "Tara"]

SYSTEM_KEYS = {"system", "system(s)", "systems", "facility", "facilities"}
OUTCOME_KEYS = {"outcome", "status", "result"}
KIND_KEYS = {"type", "code", "build", "port", "benchmark"}

PAIR_RE = re.compile(r"\*\*([^*]+?):\*\*\s*([^·]*)")
ICON_RE = re.compile(r":[a-z0-9_+-]+:\s*")
MD_RE = re.compile(r"[*_`]")


def _clean(s: str) -> str:
    return MD_RE.sub("", ICON_RE.sub("", s)).strip(" .·")


def _classify(outcome: str) -> str:
    o = outcome.lower()
    if any(w in o for w in ("negative", "fail", "blocked")):
        return "blocked"
    if any(w in o for w in ("partial", "mixed")):
        return "in_progress"
    if any(w in o for w in ("ongoing", "phase", "in progress")):
        return "available"
    if any(w in o for w in ("success", "completed", "verified", "reproduced", "confirmed")):
        return "pass"
    return "listed"


def _parse(path: Path) -> dict | None:
    title = ""
    pairs: dict[str, str] = {}
    for line in path.read_text().splitlines()[:12]:
        if not title and line.startswith("# "):
            title = _clean(line[2:])
        elif "**" in line and ":**" in line:
            for key, val in PAIR_RE.findall(line):
                pairs.setdefault(key.strip().lower(), _clean(val))
    if not title:
        return None

    sys_raw = next((pairs[k] for k in SYSTEM_KEYS if k in pairs), "")
    systems = [s for s in SYSTEMS if re.search(rf"\b{s}\b", sys_raw, re.I)]
    outcome = next((pairs[k] for k in OUTCOME_KEYS if k in pairs), "")
    kind = next((pairs[k] for k in KIND_KEYS if k in pairs), "")

    cat = path.parent.name
    return {
        "title": title,
        "path": f"{cat}/{path.stem}/",
        "category": cat,
        "categoryLabel": CATEGORIES.get(cat, cat),
        "systems": systems,
        "systemsRaw": sys_raw,
        "kind": kind,
        "outcome": outcome,
        "outcomeClass": _classify(outcome),
    }


def main() -> int:
    entries = []
    for cat in CATEGORIES:
        d = CAMPAIGNS / cat
        for f in sorted(d.glob("*.md")):
            if f.name == "index.md":
                continue
            e = _parse(f)
            if e:
                entries.append(e)
            else:
                print(f"warning: no title found in {f.relative_to(ROOT)} — skipped")
    entries.sort(key=lambda e: (e["category"], e["path"]))

    OUT.write_text(json.dumps({"campaigns": entries}, indent=1) + "\n")
    print(f"wrote docs/campaigns/campaigns.json ({len(entries)} campaigns)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
