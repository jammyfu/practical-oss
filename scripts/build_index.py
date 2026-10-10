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
HISTORY_PAGE = PAGES / "history.md"
CATEGORY_DIR = PAGES / "categories"
WINDOW_FILE = {"日": "day.md", "周": "week.md", "月": "month.md"}
STALE_PAGES = (
    "历史最高.md",
    "当前热度最高.md",
    "当前热度-日.md",
    "当前热度-周.md",
    "当前热度-月.md",
    "命令行与版本控制.md",
    "编辑器.md",
    "语言与运行时.md",
    "界面与前端.md",
    "服务与接入.md",
    "数据存储与分析.md",
    "运行与基础设施.md",
    "观测与安全.md",
    "人工智能.md",
    "自托管应用.md",
    "创作.md",
)
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


def trending_dir(captured_on: str) -> Path:
    return PAGES / "trending" / captured_on


def window_path(captured_on: str, window_id: str) -> Path:
    return trending_dir(captured_on) / WINDOW_FILE.get(window_id, f"{window_id}.md")


def render_category(category: dict, rows: list[dict], captured_on: str) -> str:
    page = CATEGORY_DIR / f"{category['id']}.md"
    current = by_stars([row for row in rows if row["trending"]])
    history = by_stars([row for row in rows if not row["trending"]])
    back = rel_link(page, README)
    history_link = rel_link(page, HISTORY_PAGE)
    current_link = rel_link(page, trending_dir(captured_on) / "index.md")
    lines = [
        f"# {category['name']}",
        "",
        category["summary"],
        "",
        f"返回 [目录]({back})。跨分类的名单在 [历史最高]({history_link}) 和 [当前热度最高]({current_link})。",
        "",
        "## 近两年的新默认",
        "",
        "这一节只放本类里标了 `trending: yes` 的项目，按总星标从高到低。它不是今日、本周或本月的趋势榜。",
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


def render_history(entries: list[dict], names: dict[str, str], captured_on: str) -> str:
    page = HISTORY_PAGE
    rows = by_stars([row for row in entries if not row["trending"]])
    back = rel_link(page, README)
    lines = [
        "# 历史最高",
        "",
        "长期默认，不含近两年才标成新默认的项目。按收录时的 GitHub 星标从高到低排列。各篇的统计日写在 `stars_at`。",
        "",
        f"返回 [目录]({back})。日、周、月趋势在 [当前热度最高]({rel_link(page, trending_dir(captured_on) / 'index.md')})。",
        "",
        *heat_table(rows, page, names, current=False),
        FOOTER,
        "",
    ]
    return "\n".join(lines)


def render_window_page(window: dict, captured_on: str) -> str:
    page = window_path(captured_on, window["id"])
    back = rel_link(page, trending_dir(captured_on) / "index.md")
    rows = sorted(window["repos"], key=lambda row: (-row["gain"], row["repo"].lower()))
    lines = [
        f"# 当前热度 · {window['title']}",
        "",
        f"抓取日 {captured_on}。",
        window["lead"],
        "表内按这一档新增星标从高到低排。",
        "",
        f"返回 [当前热度最高]({back})。",
        "",
        "| 顺序 | 项目 | 这一档新增 | 许可 | 它做什么 |",
        "| ---: | --- | ---: | --- | --- |",
    ]
    for index, row in enumerate(rows, start=1):
        url = row["url"]
        name = row["repo"]
        gain = f"{row['gain']:,}"
        license_name = row.get("license") or "未标明"
        summary = row["summary"].replace("|", " ")
        lines.append(f"| {index} | [{name}]({url}) | {gain} | {license_name} | {summary} |")
    lines.extend(["", window["note"], ""])
    return "\n".join(lines)


def render_current(captured_on: str, snapshot: dict) -> str:
    page = trending_dir(captured_on) / "index.md"
    lines = [
        "# 当前热度最高",
        "",
        f"按日、周、月分开。数据取自 {snapshot['source']}，抓取日 {captured_on}。目录名用的就是这一天。各档按该档新增星标从高到低排，新增星标是趋势页上的数字。",
        "",
        "近两年才成为新默认、但抓取当天没有出现在趋势页上的项目，仍留在各用途分类的「近两年的新默认」里，不混进这三档。",
        "",
        f"返回 [目录]({rel_link(page, README)})。长期默认在 [历史最高]({rel_link(page, HISTORY_PAGE)})。",
        "",
        "| 档 | 含义 | 项目数 |",
        "| --- | --- | ---: |",
    ]
    for window in snapshot["windows"]:
        href = rel_link(page, window_path(captured_on, window["id"]))
        lines.append(
            f"| [{window['title']}]({href}) | {window['meaning']} | {len(window['repos'])} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_readme(categories: list[dict], entries: list[dict], captured_on: str) -> str:
    history = [row for row in entries if not row["trending"]]
    lines = [
        "## 热度",
        "",
        "历史最高是长期默认。当前热度最高按日、周、月看 GitHub 趋势，不跟总星标混在一张表里。趋势页的目录名是抓取日。",
        "",
        "| 名单 | 怎么分 | 篇数 |",
        "| --- | --- | ---: |",
        f"| [历史最高](catalog/history.md) | 长期默认，按总星标 | {len(history)} |",
        f"| [当前热度最高](catalog/trending/{captured_on}/index.md) | 日、周、月三档趋势，抓取日 {captured_on} | 见该页 |",
        "",
        "## 用途",
        "",
        "每类一页，放在 `catalog/categories/`。页内分成近两年的新默认，和历史最高。",
        "",
        "| 分类 | 这一类是什么 | 历史 | 近两年 |",
        "| --- | --- | ---: | ---: |",
    ]
    for category in categories:
        rows = [row for row in entries if row["category"] == category["id"]]
        past = sum(1 for row in rows if not row["trending"])
        now = sum(1 for row in rows if row["trending"])
        href = f"catalog/categories/{category['id']}.md"
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

    snapshot = json.loads((PAGES / "trending-windows.json").read_text(encoding="utf-8"))
    captured_on = snapshot["captured_on"]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", captured_on):
        raise SystemExit(f"captured_on is not a date: {captured_on}")

    for category in categories:
        write_page(
            CATEGORY_DIR / f"{category['id']}.md",
            render_category(category, grouped[category["id"]], captured_on),
        )
    write_page(HISTORY_PAGE, render_history(entries, names, captured_on))
    write_page(trending_dir(captured_on) / "index.md", render_current(captured_on, snapshot))
    for window in snapshot["windows"]:
        write_page(
            window_path(captured_on, window["id"]),
            render_window_page(window, captured_on),
        )
    for name in STALE_PAGES:
        stale = PAGES / name
        if stale.exists():
            stale.unlink()

    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    replacement = f"{START}\n\n{render_readme(categories, entries, captured_on)}{END}"
    updated, count = pattern.subn(replacement, readme, count=1)
    if count != 1:
        raise SystemExit("README is missing catalog markers")
    README.write_text(updated, encoding="utf-8")

    payload = {
        "stars_at": sorted({entry["stars_at"] for entry in entries}),
        "trending_captured_on": captured_on,
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
