---
name: Ghostty
slug: ghostty
category: cli
primary_repo: ghostty-org/ghostty
url: https://github.com/ghostty-org/ghostty
website: https://ghostty.org/
license: MIT
language: Zig
stars: 62010
stars_at: 2026-10-10
summary: 用 GPU 绘制终端网格的模拟器，窗口里跑的仍是原来的 shell。
trending: yes
trending_why: 2024 年末以 1.0 公开，在 macOS 和 Linux 上提供新的原生 GPU 终端窗口，换的不是 shell。
tags: [终端, GPU]
---

## 它解决什么问题

终端里真正解释命令的是 shell。外面那一层窗口负责画字符、处理键盘和转义序列，系统自带的这一层往往在滚动、字形和分屏上不够快，或者和平台界面格格不入。Ghostty 做的是这一层：一个跨平台的终端模拟器，用 GPU 画网格，并尽量使用各平台自己的窗口控件。它不是 shell，也不替换 zsh、bash 或 fish。

## 核心功能

- 把终端网格画在 GPU 上，大量输出时少占 CPU。
- macOS 和 Linux 上使用平台原生界面，而不是一套自己画的统一皮肤。
- 标签和分屏，用来在一个窗口里并排看多个终端。
- 字体、主题和键位可以配置。转义序列尽量按现有终端习惯兼容，让已有的全屏程序能跑。

## 通常怎么用

用它换掉系统自带的终端窗口。打开之后，里面仍是用户原来的 shell、原来的提示符和原来的配置。tmux 可以在其中继续做会话保持。远程机器通过在里面运行 SSH 客户端到达，Ghostty 自己不实现登录协议。选择它的人通常是在挑「窗口好不好用」，不是在挑「用哪种 shell」。

## 它不负责什么

它不解析命令，不做补全，也不保存命令历史，这些属于 shell。它不在断线之后保住远程进程，那是 tmux 或系统服务的工作。它不是编辑器，也不是 SSH 服务器。换了 Ghostty，脚本、别名和登录环境都不会跟着变。

## 许可与热度

MIT。2026-10-10，`ghostty-org/ghostty` 有 62,010 星。公开的 1.0 在 2024 年 12 月发布，在此之前是长期的非公开测试。
