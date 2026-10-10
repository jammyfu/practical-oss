---
name: delta
slug: delta
category: cli
primary_repo: dandavison/delta
url: https://github.com/dandavison/delta
website: https://dandavison.github.io/delta/
license: MIT
language: Rust
stars: 32470
stars_at: 2026-10-10
summary: 把 Git 的 diff 显示成带语法高亮、能看清增删的页面。
tags: [diff, Git]
---

## 它解决什么问题

`git diff` 和 `git show` 的默认输出是一整片红绿文本，嵌套的括号和长行很难对上。delta 作为 Git 的分页器，把同一份 diff 排成并排或行内的语法高亮，并标出改动落在哪一行。

## 核心功能

- 语法高亮。按文件类型给 diff 上色，而不是只有整行的红绿。
- 排版。并排、行内和行号几种看法，用来对准改了什么。
- 接在 Git 上。通过 Git 配置成为 `diff`、`show` 和 `log -p` 的分页器，不替换 Git 本身。
- 也能单独读一份 diff 文本，不限于交互式的 `git` 命令。

## 通常怎么用

开发机把 Git 的分页器设成 delta 之后，日常的 diff、提交说明里的补丁和代码评审前的自查都走它。合并冲突的决策仍在编辑器或 `git merge` 里完成，delta 负责把差异看清楚。

## 它不负责什么

delta 不决定哪一边该留，不执行提交，也不替代代码评审系统。它只改显示。终端不支持颜色或语法定义缺失时，收益会小很多。

## 许可与热度

MIT。2026-10-10，`dandavison/delta` 有 32,470 星。
