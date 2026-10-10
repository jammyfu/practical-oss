#!/usr/bin/env python3
"""Rebuild the README directory, per-category pages, and catalog/index.json."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "entries"
README = ROOT / "README.md"
CATEGORIES = ROOT / "catalog" / "categories.json"
INDEX = ROOT / "catalog" / "index.json"
PAGES = ROOT / "catalog"
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"
HISTORY_NAME = "历史最高.md"
CURRENT_NAME = "当前热度最高.md"
FOOTER = (
    "星标取自 GitHub API，统计日见各条目的 `stars_at`。"
    "星标只说明仓库被关注的程度，不代替采用率。"
    "PostgreSQL 这类镜像仓库星标偏低，仍然是行业默认选择。"
)


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
        meta["trending"] = meta.get("trending") == "yes"
        found.append(meta)
    return found


def rel_link(from_page: Path, target: Path) -> str:
    return Path(os.path.relpath(target, from_page.parent)).as_posix()


def stars_cell(row: dict) -> str:
    stars = f"{row['stars']:,}"
    if row.get("stars_note"):
        return f"{stars}（见正文）"
    return stars


def project_link(row: dict, page: Path) -> str:
    target = rel_link(page, ROOT / row["path"])
    return f"[{row['name']}]({target})"


def functional_table(rows: list[dict], page: Path) -> list[str]:
    if not rows:
        return ["这一档还没有条目。", ""]
    lines = [
        "| 项目 | 它做什么 | 许可 | 星标 |",
        "| --- | --- | --- | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {project_link(row, page)} | {row['summary']} | {row['license']} | {stars_cell(row)} |"
        )
    lines.append("")
    return lines


def heat_table(rows: list[dict], page: Path, names: dict[str, str], current: bool) -> list[str]:
    if not rows:
        return ["这一档还没有条目。", ""]
    if current:
        lines = [
            "| 项目 | 新在哪里 | 功能分类 | 许可 | 星标 |",
            "| --- | --- | --- | --- | ---: |",
        ]
    else:
        lines = [
            "| 项目 | 它做什么 | 功能分类 | 许可 | 星标 |",
            "| --- | --- | --- | --- | ---: |",
        ]
    for row in rows:
        detail = row.get("trending_why", row["summary"]) if current else row["summary"]
        category = names.get(row["category"], row["category"])
        lines.append(
            f"| {project_link(row, page)} | {detail} | {category} | {row['license']} | {stars_cell(row)} |"
        )
    lines.append("")
    return lines


def by_stars(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda item: (-item["stars"], item["name"].lower()))


def write_page(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def render_category(category: dict, rows: list[dict], names: dict[str, str]) -> str:
    page = PAGES / f"{category['name']}.md"
    current = by_stars([row for row in rows if row["trending"]])
    history = by_stars([row for row in rows if not row["trending"]])
    back = rel_link(page, README)
    history_link = rel_link(page, PAGES / HISTORY_NAME)
    current_link = rel_link(page, PAGES / CURRENT_NAME)
    lines = [
        f"# {category['name']}",
        "",
        category["summary"],
        "",
        f"返回 [目录]({back})。跨分类的名单在 [历史最高]({history_link}) 和 [当前热度最高]({current_link})。",
        "",
        "## 当前热度最高",
        "",
        "这一节只放本类里标了 `trending: yes` 的项目，按星标从高到低。标准是大约 2024 年以来成为新默认，或关注和采用明显跃升。",
        "",
        *functional_table(current, page),
        "## 历史最高",
        "",
        "这一节是本类里的长期默认，按星标从高到低。星标不是采用率，镜像仓库尤其不能只看这个数字。",
        "",
        *functional_table(history, page),
        FOOTER,
        "",
    ]
    return "\n".join(lines)


def render_history(entries: list[dict], names: dict[str, str]) -> str:
    page = PAGES / HISTORY_NAME
    rows = by_stars([row for row in entries if not row["trending"]])
    back = rel_link(page, README)
    lines = [
        "# 历史最高",
        "",
        "长期默认，不含近两年才标成当前热度的项目。按收录时的 GitHub 星标从高到低排列。",
        "",
        f"返回 [目录]({back})。当前这一波在 [当前热度最高]({rel_link(page, PAGES / CURRENT_NAME)})。",
        "",
        *heat_table(rows, page, names, current=False),
        FOOTER,
        "",
    ]
    return "\n".join(lines)


def render_current(entries: list[dict], names: dict[str, str]) -> str:
    page = PAGES / CURRENT_NAME
    rows = by_stars([row for row in entries if row["trending"]])
    back = rel_link(page, README)
    lines = [
        "# 当前热度最高",
        "",
        "大约 2024 年以来成为某类工作的新默认，或关注和实际采用明显跃升。按星标从高到低排列。Git、React、PostgreSQL 这类长期默认不进这一页。",
        "",
        f"返回 [目录]({back})。长期默认在 [历史最高]({rel_link(page, PAGES / HISTORY_NAME)})。",
        "",
        *heat_table(rows, page, names, current=True),
        FOOTER,
        "",
    ]
    return "\n".join(lines)


def render_readme(categories: list[dict], entries: list[dict]) -> str:
    history = [row for row in entries if not row["trending"]]
    current = [row for row in entries if row["trending"]]
    lines = [
        "## 热度",
        "",
        "两份名单分开。历史最高是长期默认，当前热度最高是近两年的新热。都按星标从高到低排。",
        "",
        "| 名单 | 怎么分 | 篇数 |",
        "| --- | --- | ---: |",
        f"| [历史最高](catalog/{HISTORY_NAME}) | 长期默认 | {len(history)} |",
        f"| [当前热度最高](catalog/{CURRENT_NAME}) | 2024 年以来的新默认或热度跃升 | {len(current)} |",
        "",
        "## 用途",
        "",
        "每类一页。页内再分成当前热度最高和历史最高。",
        "",
        "| 分类 | 这一类是什么 | 历史 | 当前 |",
        "| --- | --- | ---: | ---: |",
    ]
    for category in categories:
        rows = [row for row in entries if row["category"] == category["id"]]
        past = sum(1 for row in rows if not row["trending"])
        now = sum(1 for row in rows if row["trending"])
        href = f"catalog/{category['name']}.md"
        lines.append(f"| [{category['name']}]({href}) | {category['summary']} | {past} | {now} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    categories = json.loads(CATEGORIES.read_text(encoding="utf-8"))
    entries = load_entries()
    known = {item["id"] for item in categories}
    unknown = sorted({entry["category"] for entry in entries} - known)
    if unknown:
        raise SystemExit(f"unknown categories: {', '.join(unknown)}")
    names = {item["id"]: item["name"] for item in categories}
    grouped: dict[str, list[dict]] = {item["id"]: [] for item in categories}
    for entry in entries:
        grouped[entry["category"]].append(entry)

    generated = {HISTORY_NAME, CURRENT_NAME}
    for category in categories:
        filename = f"{category['name']}.md"
        generated.add(filename)
        write_page(PAGES / filename, render_category(category, grouped[category["id"]], names))
    write_page(PAGES / HISTORY_NAME, render_history(entries, names))
    write_page(PAGES / CURRENT_NAME, render_current(entries, names))

    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    replacement = f"{START}\n\n{render_readme(categories, entries)}{END}"
    updated, count = pattern.subn(replacement, readme, count=1)
    if count != 1:
        raise SystemExit("README is missing catalog markers")
    README.write_text(updated, encoding="utf-8")

    payload = {
        "stars_at": sorted({entry["stars_at"] for entry in entries}),
        "count": len(entries),
        "history_count": sum(1 for entry in entries if not entry["trending"]),
        "current_count": sum(1 for entry in entries if entry["trending"]),
        "categories": categories,
        "projects": entries,
    }
    INDEX.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"indexed {len(entries)} projects, "
        f"{payload['history_count']} historical, {payload['current_count']} current"
    )


if __name__ == "__main__":
    main()
