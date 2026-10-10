---
name: Ruff
slug: ruff
category: cli
primary_repo: astral-sh/ruff
url: https://github.com/astral-sh/ruff
website: https://docs.astral.sh/ruff/
license: MIT
language: Rust
stars: 49971
stars_at: 2026-10-10
summary: 用一个程序检查并格式化 Python，覆盖原来要靠多件 lint 工具才做的事。
trending: yes
trending_why: 同一个 Rust 程序同时做 lint 和格式化，用来换掉 Flake8、isort 和 Black 的组合。
tags: [Python, 代码检查]
---

## 它解决什么问题

Python 项目要管代码风格时，常常同时装 Flake8、若干插件、isort 和 Black。每件工具配置一份，跑一遍仓库要等很久。Ruff 用 Rust 实现检查和格式化，把这些步骤收成一次很快的扫描，让提交前和编辑器里都能即时看到问题。

## 核心功能

- 大量内置 lint 规则，覆盖未使用的导入、常见错误写法和导入顺序等。
- 许多规则可以直接改写源码，而不是只打印警告。
- 格式化器，风格目标接近 Black，用来统一空格、引号和换行。
- 单程序同时给出命令行和编辑器可用的检查，不必为每条规则再装一个 Python 插件。

## 通常怎么用

放在保存文件或提交前：先按项目配置跑检查，能自动修的就修，剩下的格式化交给它的 formatter。大型仓库用它替换原来串起来的 Flake8、isort 和 Black。规则集按项目打开，而不是默认把所有历史规则都打开。

## 它不负责什么

Ruff 不做类型检查，类型错误仍要靠类型检查器。它不运行测试，也不安装依赖或管理虚拟环境。它不执行代码，所以发现不了只有跑起来才出现的逻辑错误。旧配置里某个冷门插件的规则，不能假设这里一定有对应项。

## 许可与热度

MIT。2026-10-10，`astral-sh/ruff` 有 49,971 星。它新在把 lint 和格式化合成一个很快的程序，而不是再维护一套 Python 插件链。
