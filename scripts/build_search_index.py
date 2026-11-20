#!/usr/bin/env python3
"""Build a compact Chinese/English search index from Sphinx HTML output."""
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path

SKIP_TAGS = {"script", "style", "noscript", "svg"}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0
        self.title_parts: list[str] = []
        self.in_title = False

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in SKIP_TAGS:
            self.skip_depth += 1
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        if tag in SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        if self.in_title:
            self.title_parts.append(text)
        if not self.skip_depth:
            self.parts.append(text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--html-dir", type=Path, required=True)
    args = parser.parse_args()
    root = args.html_dir.resolve()
    if not root.is_dir():
        raise SystemExit(f"HTML directory does not exist: {root}")

    entries = []
    for page in sorted(root.rglob("*.html")):
        relative = page.relative_to(root).as_posix()
        if relative in {"search.html", "search-zh.html", "genindex.html", "py-modindex.html"}:
            continue
        extractor = TextExtractor()
        try:
            extractor.feed(page.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        text = re.sub(r"\s+", " ", " ".join(extractor.parts)).strip()
        title = " ".join(extractor.title_parts).strip() or relative
        if not text:
            continue
        entries.append({"title": title, "url": relative, "text": text[:12000]})

    output = root / "search-index.json"
    output.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Search index written: {output} ({len(entries)} HTML pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
