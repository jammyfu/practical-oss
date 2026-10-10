---
name: NestJS
slug: nest
category: backend
primary_repo: nestjs/nest
url: https://github.com/nestjs/nest
website: https://nestjs.com
license: MIT
language: TypeScript
stars: 76806
stars_at: 2026-10-10
summary: 用模块和依赖注入组织 Node 服务的接口、配置和业务代码。
tags: [Node, TypeScript]
---

## 它解决什么问题

Node 服务一大，路由、配置和业务调用容易堆在同一批文件里，换一个人就不敢改。NestJS 用模块、控制器和依赖注入把这些边界定下来，让 TypeScript 服务有一套稳定的放代码的地方。

## 核心功能

- 模块。一个功能一块，依赖关系写在模块上，而不是靠文件之间互相引用碰运气。
- 控制器和提供者。HTTP 入口、业务类和外部客户端分开注册，测试时可以换掉实现。
- 平台适配。HTTP 层可以站在 Express 或 Fastify 上，框架管的是结构和装饰器，不把路由引擎写死成自己的。

## 通常怎么用

多人维护的 TypeScript 后端、管理接口和需要清晰分层的 Node 服务，会用 NestJS 当应用骨架。脚本、一次性函数和边缘上的小路由不必上这套结构。数据库、队列和具体的云服务通过提供者接进来。

## 它不负责什么

NestJS 不选择数据库，不负责进程如何部署，也不替你设计表结构。装饰器和模块变多以后，一个很小的接口也会显得重。它是应用的组织方式，不是运行时本身。

## 许可与热度

MIT。2026-10-10，`nestjs/nest` 有 76,806 星。
