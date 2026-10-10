---
name: ripgrep
slug: ripgrep
category: cli
primary_repo: BurntSushi/ripgrep
url: https://github.com/BurntSushi/ripgrep
website: https://github.com/BurntSushi/ripgrep
license: Unlicense
language: Rust
stars: 68980
stars_at: 2026-10-10
summary: 在目录树里按正则搜索文本，并默认跳过 Git 忽略的文件。
tags: [搜索, 命令行]
---

## 它解决什么问题

在一个仓库里找某个函数、配置项或报错字符串时，系统自带的 `grep -r` 经常会钻进 `node_modules`、构建产物和 `.git`。结果又慢又吵。ripgrep 把「只搜该搜的源码」当成默认行为。

## 核心功能

- 递归搜索，支持正则。命令名是 `rg`。
- 自动读取 `.gitignore`、`.ignore` 和隐藏文件规则。需要时可以显式关闭。
- 按文件类型过滤，例如只看 Rust 或 Markdown。
- 并行扫描，并在终端里把匹配行高亮出来。

## 通常怎么用

工程师在仓库根目录执行 `rg` 找符号、配置键或日志里的错误码。很多编辑器的「在工作区搜索」底层也会调用它，Visual Studio Code 就把它作为搜索后端之一。它适合源码和文本，不适合当全文检索引擎去检索百万份办公文档。

## 它不负责什么

它不建立持久索引，每次都是现扫。也不解析语言语义，所以找不到「这个函数的所有调用」这种需要语法树的结果。搜 PDF、Office 文档或数据库记录要换专门的工具。

## 许可与热度

以 Unlicense 发布，等于把版权限制尽可能拿掉。2026-10-10，`BurntSushi/ripgrep` 有 68,980 星。它的地位来自速度和默认规则，已经成为新一代命令行搜索的参照。
