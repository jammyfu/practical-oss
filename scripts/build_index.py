#!/usr/bin/env python3
"""Rebuild the README catalog and catalog/index.json from entry front matter."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "entries"
README = ROOT / "README.md"
CATEGORIES = ROOT / "catalog" / "categories.json"
INDEX = ROOT / "catalog" / "index.json"
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"


def parse_front_matter(text: str) -> dict:
    if not text.startswith("---\n"):
        raise SystemExit("entry is missing front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SystemExit("front matter is not closed")
    meta = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key.strip()] = [
                item.strip() for item in value[1:-1].split(",") if item.strip()
            ]
        elif value.startswith('"') and value.endswith('"'):
            meta[key.strip()] = value[1:-1]
        else:
            meta[key.strip()] = value
    for number_key in ("stars",):
        if number_key in meta:
            meta[number_key] = int(meta[number_key])
    return meta


def load_entries() -> list[dict]:
    found = []
    for path in sorted(ENTRIES.glob("*/*.md")):
        meta = parse_front_matter(path.read_text(encoding="utf-8"))
        meta["path"] = path.relative_to(ROOT).as_posix()
        found.append(meta)
    return found


def render_catalog(categories: list[dict], entries: list[dict]) -> str:
    by_category = {item["id"]: [] for item in categories}
    for entry in entries:
        by_category.setdefault(entry["category"], []).append(entry)
    lines = []
    for category in categories:
        rows = sorted(by_category.get(category["id"], []), key=lambda item: item["name"].lower())
        lines.append(f"## {category['name']}")
        lines.append("")
        lines.append(category["summary"])
        lines.append("")
        if not rows:
            lines.append("这一类还没有条目。")
            lines.append("")
            continue
        lines.append("| 项目 | 它做什么 | 许可 | 星标 |")
        lines.append("| --- | --- | --- | ---: |")
        for row in rows:
            note = row.get("stars_note", "")
            stars = f"{row['stars']:,}"
            if note:
                stars = f"{stars}（见正文）"
            name = f"[{row['name']}]({row['path']})"
            lines.append(
                f"| {name} | {row['summary']} | {row['license']} | {stars} |"
            )
        lines.append("")
    lines.append(
        "星标取自 GitHub API，统计日见各条目的 `stars_at`。星标只说明仓库被关注的程度，不代替采用率。PostgreSQL 这类镜像仓库星标偏低，仍然是行业默认选择。"
    )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    categories = json.loads(CATEGORIES.read_text(encoding="utf-8"))
    entries = load_entries()
    known = {item["id"] for item in categories}
    unknown = sorted({entry["category"] for entry in entries} - known)
    if unknown:
        raise SystemExit(f"unknown categories: {', '.join(unknown)}")
    catalog = render_catalog(categories, entries)
    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    replacement = f"{START}\n\n{catalog}{END}"
    updated, count = pattern.subn(replacement, readme, count=1)
    if count != 1:
        raise SystemExit("README is missing catalog markers")
    README.write_text(updated, encoding="utf-8")
    payload = {
        "stars_at": sorted({entry["stars_at"] for entry in entries}),
        "count": len(entries),
        "categories": categories,
        "projects": entries,
    }
    INDEX.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"indexed {len(entries)} projects")


if __name__ == "__main__":
    main()
