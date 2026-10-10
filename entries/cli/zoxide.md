---
name: zoxide
slug: zoxide
category: cli
primary_repo: ajeetdsouza/zoxide
url: https://github.com/ajeetdsouza/zoxide
website: https://github.com/ajeetdsouza/zoxide
license: MIT
language: Rust
stars: 40005
stars_at: 2026-10-10
summary: 记住去过的目录，用几个字母跳回去。
tags: [目录, shell]
---

## 它解决什么问题

项目目录一深，每天都在敲同一串路径。`cd` 的历史只在当前会话里好用，换一个窗口又要重找。zoxide 记住你成功进入过的目录，之后用一段关键词按使用频率跳回去。

## 核心功能

- 记录。每次进入目录都记一笔，常用的排在前面。
- 跳转。用目录名的一部分匹配，不必写出完整路径。
- 交互。可以接到 fzf，在几个候选目录里挑一个。
- shell 集成。Bash、Zsh、Fish 和 PowerShell 都能把跳转接到自己的命令上。

## 通常怎么用

开发机的 shell 配置里启用 zoxide，平时照常用 `cd`，它在旁边学习。目录去过几次之后，再用短关键词跳。新克隆下来、从未进入过的目录，它还不知道，第一次仍要走完整路径。

## 它不负责什么

zoxide 不搜索文件内容，那是 ripgrep 和 fzf 的事。它也不创建目录，不替代 shell。数据库只反映这台机器上的访问，不会凭空知道你没打开过的路径。

## 许可与热度

MIT。2026-10-10，`ajeetdsouza/zoxide` 有 40,005 星。
