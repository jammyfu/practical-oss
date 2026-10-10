---
name: Neovim
slug: neovim
category: editor
primary_repo: neovim/neovim
url: https://github.com/neovim/neovim
website: https://neovim.io/
license: Apache-2.0
language: Vim Script
stars: 102956
stars_at: 2026-10-10
summary: 在 Vim 的编辑模型上重建可扩展性，用 Lua 配置，并把界面和编辑核心拆开。
tags: [编辑器, Vim]
---

## 它解决什么问题

Vim 的模式编辑很高效，但历史上扩展使用 Vimscript，异步和嵌入外部工具都很别扭。Neovim 保留「普通模式、操作符、动作」这套编辑语言，把扩展、界面和工作分配重新做了一遍，让它能承载现代语言服务。

## 核心功能

- 与 Vim 一致的核心编辑操作，大多数 Vim 肌肉记忆可以直接用。
- 内嵌 Lua，用来写配置和插件。插件可以异步运行任务。
- 语言服务、树形语法高亮、调试和模糊查找都通过插件接进来。
- 核心与界面分离。终端里可以用，也有独立的图形前端。

## 通常怎么用

愿意维护自己配置的工程师，用它在终端或远程服务器上编辑。一套配置放进 Git，换机器后克隆即可。它常和 ripgrep、tmux、lazygit 放在同一条终端工作流里。不想写配置的人，VS Code 这种开箱即用的编辑器更合适。

## 它不负责什么

上游 Neovim 几乎不带「开箱即用的 IDE」。补全、文件树、Git 标志和调试都要自己选插件，或者使用别人整理好的发行配置。插件组合会过时，升级后要自己看 breakage。它也不是一个协作编辑服务。

## 许可与热度

Apache-2.0。2026-10-10，`neovim/neovim` 有 102,956 星。GitHub 把仓库主语言标成 Vim Script，实际核心是 C，扩展生态则大量使用 Lua。
