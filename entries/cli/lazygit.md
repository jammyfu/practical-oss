---
name: lazygit
slug: lazygit
category: cli
primary_repo: jesseduffield/lazygit
url: https://github.com/jesseduffield/lazygit
website: https://github.com/jesseduffield/lazygit
license: MIT
language: Go
stars: 83061
stars_at: 2026-10-10
summary: 在终端里用面板完成暂存、提交、分支、变基和解决冲突。
tags: [Git, 终端界面]
---

## 它解决什么问题

Git 的命令很完整，但看状态、挑行暂存、比较分支和解决冲突时，要来回敲多条命令。图形客户端又能离开终端。lazygit 把这些高频动作放进一个键盘驱动的终端界面。

## 核心功能

- 分栏显示文件状态、差异、提交历史、分支和储藏。
- 按文件甚至按行暂存，再写提交说明。
- 检出、合并、变基、拣选提交，以及常见的撤销操作。
- 冲突出现时，在界面里选择保留哪一侧，而不必先记住冲突标记的语法。

## 通常怎么用

已经熟悉 Git 概念、但希望少打命令的人，会在仓库里直接运行 `lazygit`。它也常被嵌进 Neovim 或 tmux 的工作流。它是 Git 的界面，不是另一套版本控制系统，仓库格式仍然由 Git 决定。

## 它不负责什么

它不替代对 Git 模型的理解。强制推送、改写已经公开的历史这些破坏性动作，界面方便了，风险还在。代码审查、议题和持续集成仍在 GitHub 或 GitLab 上完成。

## 许可与热度

MIT 许可。2026-10-10，`jesseduffield/lazygit` 有 83,061 星。在终端 Git 界面里，它是目前最常被推荐的一个。
