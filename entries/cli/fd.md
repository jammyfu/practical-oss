---
name: fd
slug: fd
category: cli
primary_repo: sharkdp/fd
url: https://github.com/sharkdp/fd
website: https://github.com/sharkdp/fd
license: Apache-2.0
language: Rust
stars: 44736
stars_at: 2026-10-10
summary: 按名字找文件，默认跳过 Git 忽略的目录，并用颜色标出匹配的路径。
tags: [搜索, 命令行]
---

## 它解决什么问题

`find` 能做很多事，但日常只是「按文件名找一下」时，语法难记，还会钻进依赖目录和构建产物。fd 把这条最常见的路径做成默认行为：从当前目录往下找，尊重 `.gitignore`，结果可以直接交给别的命令。

## 核心功能

- 按文件名或正则过滤，命令名是 `fd`。
- 默认跳过隐藏文件和 Git 忽略的路径，需要时再显式打开。
- 按文件类型过滤，例如只要目录、只要可执行文件。
- 找到之后可以批量执行命令，用来替换一段 `find ... -exec`。

## 通常怎么用

在仓库里找配置、测试文件或某个模块的目录。它常和 fzf、ripgrep 放在同一套终端习惯里：ripgrep 搜文件内容，fd 搜文件名。全磁盘、包含被忽略目录的排查，仍然要用 `find` 或给 fd 加上相应开关。

## 它不负责什么

它不搜索文件里面的文字，也不建立系统级的持久索引。复杂的权限、时间和 inode 条件不是它的重点。它也不替代操作系统的文件索引服务。

## 许可与热度

Apache-2.0。2026-10-10，`sharkdp/fd` 有 44,736 星。它和同一作者的 bat、以及 ripgrep，构成了现在常见的 Rust 命令行工具组合。
