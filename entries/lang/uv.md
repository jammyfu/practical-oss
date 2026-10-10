---
name: uv
slug: uv
category: lang
primary_repo: astral-sh/uv
url: https://github.com/astral-sh/uv
website: https://docs.astral.sh/uv/
license: Apache-2.0 OR MIT
language: Rust
stars: 90557
stars_at: 2026-10-10
summary: 用一个工具安装 Python 包、管理虚拟环境，并安装要用的 Python 版本。
trending: yes
trending_why: 把装包、虚拟环境和 Python 版本收进同一个程序，正在取代 pip 加 venv 的旧默认。
tags: [Python, 包管理]
---

## 它解决什么问题

做一个 Python 项目，过去常常要分开处理三件事：用 pip 装包，用 venv 隔离环境，再用另一个工具安装或切换解释器。解析慢、锁文件不统一，换一台机器就容易对不齐。uv 把这几步收进一个用 Rust 写的程序，让新项目不必先拼一套 pip 和 venv。

## 核心功能

- 解析并安装 Python 依赖，速度通常明显高于传统 pip。
- 创建和使用虚拟环境，把项目依赖和系统 Python 隔开。
- 下载并选择 CPython 版本，不必另装一套解释器管理器。
- 既有接近 pip 的安装方式，也有自己的项目工作流和锁文件。
- 可以临时跑一个命令行工具，而不必先把它装进当前项目。

## 通常怎么用

新仓库或脚本在开始写代码前，先用 uv 备好解释器和虚拟环境，再装依赖。已有项目则用它替换原来的 pip 安装步骤，锁文件交给版本库，换机器时按锁恢复。教学和 CI 里也用它减少「本机 Python 和项目要的版本不一致」。科学计算里依赖 Conda 渠道的环境，它不是那条路径的替代品。

## 它不负责什么

uv 不检查类型，不格式化代码，也不运行测试。它不规定 Web 框架或项目目录怎么组织。它也不负责把进程守护在服务器上。包能否装上仍取决于发布到 Python 包索引的内容，以及有没有对应平台的轮子。

## 许可与热度

仓库同时提供 Apache-2.0 与 MIT，按其中任一许可使用即可。GitHub 的 SPDX 只标了 Apache-2.0。2026-10-10，`astral-sh/uv` 有 90,557 星。它的变化在于把装包、虚拟环境和解释器版本收成一步，成为 pip 加 venv 之外的新默认。
