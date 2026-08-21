#!/usr/bin/env python3
"""Check internal links and anchors in the built site.

`mkdocs build --strict` validates markdown-to-markdown links, but not links
written in raw HTML (the homepage hero, the registry catalog, the 404 page)
or anchor fragments. This walks every built page and verifies that each
internal href/src resolves to a real file — and, for fragments, a real id.

Usage:  python scripts/check_links.py [site-dir]     (default: site)
Exit code is non-zero if anything is broken.
"""
from __future__ import annotations

import posixpath
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

SKIP_SCHEMES = ("http:", "https:", "mailto:", "tel:", "javascript:", "data:")


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        for attr in ("href", "src"):
            v = a.get(attr)
            if v and not v.startswith(SKIP_SCHEMES) and not v.startswith("#"):
                self.links.append(v)
            elif v and v.startswith("#") and v != "#":
                self.links.append(v)


def target_file(site: Path, url_path: str) -> Path | None:
    """Map a site-relative URL path to the file that serves it."""
    p = url_path.lstrip("/")
    cand = site / p
    if p.endswith("/") or p == "":
        cand = site / p / "index.html"
    if cand.is_file():
        return cand
    if cand.is_dir() and (cand / "index.html").is_file():
        return cand / "index.html"
    return None


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    if not site.is_dir():
        sys.exit(f"{site}: not a directory — build the site first (make build/preview)")

    pages: dict[Path, Page] = {}
    for f in sorted(site.rglob("*.html")):
        page = Page()
        page.feed(f.read_text(errors="replace"))
        pages[f] = page

    broken: list[str] = []
    for f, page in pages.items():
        # URL of this page relative to the site root, as the browser sees it.
        rel = "/" + f.relative_to(site).as_posix()
        if rel.endswith("/index.html"):
            rel = rel[: -len("index.html")]
        for link in page.links:
            url, frag = urldefrag(link)
            parsed = urlparse(url)
            if parsed.scheme or parsed.netloc:
                continue  # external
            if url:
                resolved = urljoin(rel, url)
                resolved = posixpath.normpath(resolved) + ("/" if resolved.endswith("/") else "")
                tgt = target_file(site, resolved)
                if tgt is None:
                    broken.append(f"{f.relative_to(site)}: {link} -> {resolved} (missing)")
                    continue
            else:
                tgt = f  # same-page fragment
            if frag and not re.fullmatch(r"[\d:.]+", frag):  # skip line-anchor style frags
                if frag not in pages[tgt].ids:
                    broken.append(f"{f.relative_to(site)}: {link} (missing anchor #{frag})")

    if broken:
        print(f"✗ {len(broken)} broken link(s):")
        for b in broken:
            print("  " + b)
        return 1
    print(f"✓ all internal links OK across {len(pages)} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
