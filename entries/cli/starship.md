---
name: Starship
slug: starship
category: cli
primary_repo: starship/starship
url: https://github.com/starship/starship
website: https://starship.rs
license: ISC
language: Rust
stars: 60199
stars_at: 2026-10-10
summary: 在常见的几种 shell 里显示同一套提示符，带上目录和 Git 状态。
tags: [提示符, shell]
---

## 它解决什么问题

Bash、Zsh 和 Fish 的提示符各写各的，换一台机器就丢。Git 分支、最近一次命令是否失败、当前语言版本，都要自己拼进配置。Starship 用一个跨 shell 的提示符把这些信息按同一份配置显示出来。

## 核心功能

- 跨 shell。Bash、Zsh、Fish、PowerShell 等接的是同一个程序。
- 上下文模块。目录、Git 状态、语言工具链和命令耗时可以按需打开。
- 速度。提示符是单独的程序，配置里关掉慢的模块，避免每次回车都卡一下。

## 通常怎么用

个人电脑和开发机的 shell 启动文件里初始化 Starship，把提示符配置放进仓库，换机器时一起带走。服务器上的精简 shell 不一定需要语言版本和 Git 模块，可以只留路径。

## 它不负责什么

Starship 不替换 shell，不执行 Git 命令给你看完整 diff，也不管理终端模拟器。仓库特别大时，Git 模块仍可能变慢，要关掉或限制。它只影响提示符显示，不改变命令本身的行为。

## 许可与热度

ISC。2026-10-10，`starship/starship` 有 60,199 星。
