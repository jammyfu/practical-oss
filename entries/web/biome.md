---
name: Biome
slug: biome
category: web
primary_repo: biomejs/biome
url: https://github.com/biomejs/biome
website: https://biomejs.dev/
license: Apache-2.0 OR MIT
language: Rust
stars: 25915
stars_at: 2026-10-10
summary: 用同一个工具格式化并检查 JavaScript 和 TypeScript，命令行和编辑器都能调用。
trending: yes
trending_why: 格式化和 lint 合成一个工具，减少前端项目同时维护 Prettier 和 ESLint 的做法。
tags: [JavaScript, 格式化]
---

## 它解决什么问题

前端仓库要统一写法时，格式化常常交给 Prettier，错误写法交给 ESLint，两边各有一份配置和一串插件。改一个文件要等两轮工具跑完。Biome 用一个程序同时做格式化和 lint，通过命令行或语言服务接进编辑器，让保存时的检查少一层工具链。

## 核心功能

- 格式化 JavaScript 和 TypeScript，也处理 JSON 这类项目里的配套文件。
- 内置 lint 规则，指出常见的错误写法和可以简化的代码。
- 一部分问题可以自动改写，格式化则单独保证版式一致。
- 提供命令行和语言服务，编辑器不必再为格式化和 lint 各接一个进程。

## 通常怎么用

新的前端项目用它代替「Prettier 管格式、ESLint 管规则」的组合，在保存和提交前跑一遍。已经有大量自定义 ESLint 规则的仓库，会先拿它管格式和新代码，再逐项看旧规则有没有对应，而不是一天换完。它站在源码维护这一步，不负责把页面打包发布。

## 它不负责什么

Biome 不是打包器，也不是 JavaScript 运行时。它不做 TypeScript 那种类型检查，类型错误仍要交给类型检查器。它不运行测试，也不规定框架和目录结构。规则以它自带的集合为准，不能假设原来 ESLint 配置里的每条第三方规则都有同样的检查。

## 许可与热度

仓库同时提供 MIT 与 Apache-2.0，按其中任一许可使用即可。GitHub 的 SPDX 只标了 Apache-2.0。2026-10-10，`biomejs/biome` 有 25,915 星。它新在用一个工具接住格式化和 lint，而不是继续分着维护两套前端检查。
