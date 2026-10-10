---
name: Bun
slug: bun
category: lang
primary_repo: oven-sh/bun
url: https://github.com/oven-sh/bun
website: https://bun.com/
license: "MIT（Bun 本体）；发行二进制静态链接 LGPL-2 的 JavaScriptCore"
language: Rust
stars: 96170
stars_at: 2026-10-10
summary: 运行、打包并测试 JavaScript，同时管理依赖，少装一整套分开的工具。
trending: yes
trending_why: 把运行时、打包、测试和包管理放进同一个程序，作为 Node 工具链之外的新入口。
tags: [JavaScript, 运行时]
---

## 它解决什么问题

写 JavaScript 时，运行脚本、装依赖、打包和跑测试往往是四套工具。Node 负责执行，包管理器负责安装，再另选打包器和测试框架。Bun 想用一个程序接住这几步，并缩短启动和安装时间，让脚本、服务和前端工具少绕一层。

## 核心功能

- JavaScript 和 TypeScript 运行时，可以直接跑脚本和服务。
- 打包器，把模块收成可分发的文件。
- 自带测试运行器，用来跑项目里的测试。
- 包管理器，安装 npm 生态里的依赖，并用锁文件固定版本。
- 实现了相当一部分 Node.js API，方便从现有 Node 项目迁一部分工作过来。

## 通常怎么用

新的命令行工具、小型服务和前端构建，会用 Bun 同时当运行时和包管理器。已有 Node 项目则先用它装依赖、跑脚本，确认用到的 API 和原生扩展都能工作，再决定要不要换掉生产环境里的 Node。它适合追求启动速度和少装工具的场景，不适合假设「和某个 Node 版本行为完全一致」。

## 它不负责什么

Bun 不是浏览器，也不规定 React、Vue 这类界面框架。它不是 Node 的规范实现：原生扩展和尚未覆盖的 Node API 仍可能不能跑。它不替你审查依赖的供应链，锁文件只保证版本，不保证包内容无害。

## 许可与热度

`LICENSE.md` 写明 Bun 本体是 MIT。GitHub 的 SPDX 为 NOASSERTION，因为发行二进制静态链接了 LGPL-2 的 JavaScriptCore，WebKit 的 WebCore 同样是 LGPL-2，另外还链入一批其他许可证的第三方库。静态链接 LGPL 库时，使用者需要能改库并重新链接；上游把使用的 WebKit 放在单独仓库里说明这件事。2026-10-10，`oven-sh/bun` 有 96,170 星。它新在把运行、打包、测试和装包收成一个程序。
