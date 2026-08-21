#!/usr/bin/env python3
"""Regenerate docs/feed.xml — an RSS 2.0 feed of the "What's new" page.

Each `## YYYY-MM-DD — Title` section of docs/whats-new.md becomes one feed
item, with its body rendered to HTML and a link to the section anchor on the
live page. Deterministic (the feed's lastBuildDate is the newest entry's date,
not the build time), so CI can assert the committed feed is fresh.

Run after editing whats-new.md:

    python scripts/build_whats_new_feed.py
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

try:
    import markdown
    from markdown.extensions.toc import slugify
except ImportError:
    sys.exit("Missing deps. Run:  pip install markdown")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "whats-new.md"
OUT = ROOT / "docs" / "feed.xml"

SITE = "https://docs.trinityscience.org"
PAGE = f"{SITE}/whats-new/"

HEAD_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2}) — (.+)$", re.M)


def main() -> int:
    text = SRC.read_text()
    matches = list(HEAD_RE.finditer(text))
    if not matches:
        sys.exit("no '## YYYY-MM-DD — Title' sections found in docs/whats-new.md")

    items = []
    for i, m in enumerate(matches):
        date_s, title = m.group(1), m.group(2).strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end():end]
        # The feed links to the live page; keep only the section body, stop at
        # any trailing horizontal rule / closing wrapper markup.
        body = re.sub(r"\n(---|</div>).*$", "", body, flags=re.S).strip()
        date = datetime.strptime(date_s, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        anchor = slugify(f"{date_s} — {title}", "-")
        items.append({
            "title": f"{date_s} — {title}",
            "link": f"{PAGE}#{anchor}",
            "date": date,
            "html": markdown.markdown(body),
        })

    items.sort(key=lambda it: it["date"], reverse=True)
    newest = items[0]["date"]

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "<channel>",
        "<title>Trinity Hub — What&#8217;s new</title>",
        f"<link>{PAGE}</link>",
        "<description>Feature announcements for Trinity, the multi-tenant agentic HPC workspace.</description>",
        "<language>en</language>",
        f"<lastBuildDate>{format_datetime(newest)}</lastBuildDate>",
        f'<atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>',
    ]
    for it in items:
        parts += [
            "<item>",
            f"<title>{escape(it['title'])}</title>",
            f"<link>{it['link']}</link>",
            f'<guid isPermaLink="true">{it["link"]}</guid>',
            f"<pubDate>{format_datetime(it['date'])}</pubDate>",
            f"<description>{escape(it['html'])}</description>",
            "</item>",
        ]
    parts += ["</channel>", "</rss>", ""]

    OUT.write_text("\n".join(parts))
    print(f"wrote docs/feed.xml ({len(items)} entries, newest {newest.date()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
