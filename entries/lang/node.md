---
name: Node.js
slug: node
category: lang
primary_repo: nodejs/node
url: https://github.com/nodejs/node
website: https://nodejs.org/
license: MIT
language: JavaScript
stars: 122261
stars_at: 2026-10-10
summary: 在服务器和命令行里运行 JavaScript，并让前端工具链有一个统一的运行时。
tags: [JavaScript, 运行时]
---

## 它解决什么问题

JavaScript 原本只活在浏览器里。前后端要用同一种语言、同一批包，就需要一个浏览器之外的运行时。Node.js 用 V8 引擎执行 JavaScript，加上文件系统、网络和进程接口，使它能写服务、脚本和构建工具。

## 核心功能

- 事件循环驱动的网络和非阻塞 I/O，适合大量并发连接。
- npm 包生态。前端构建、测试、Lint 和大量 CLI 都作为 Node 包分发。
- 内置模块覆盖 HTTP、加密、流、测试运行器和单文件可执行实验能力。
- 长期支持版本。生产环境通常钉住一个 LTS 版本，而不是始终追最新主版本。

## 通常怎么用

网站前端的开发服务器、打包器和脚手架几乎都要求先安装 Node。服务端则用它写 API、实时连接和脚本。CPU 很重、需要稳定多线程数值计算的任务通常不放在这里，而会交给 Python 科学计算栈、Go 或原生代码。

## 它不负责什么

Node 不规定 Web 框架。Express、Fastify、Nest 都是上层选择。它也不负责浏览器兼容，浏览器里的 JavaScript 仍然由浏览器引擎执行。包的供应链风险要另加锁文件和审计，运行时本身不替你审查依赖。

## 许可与热度

MIT。2026-10-10，`nodejs/node` 有 122,261 星。它是 JavaScript 离开浏览器之后的默认运行时。
