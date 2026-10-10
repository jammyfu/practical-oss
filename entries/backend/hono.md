---
name: Hono
slug: hono
category: backend
primary_repo: honojs/hono
url: https://github.com/honojs/hono
website: https://hono.dev
license: MIT
language: TypeScript
stars: 32469
stars_at: 2026-10-10
summary: 用同一套路由写 HTTP 接口，跑在 Node、Bun、Deno 或边缘运行时上。
tags: [HTTP, 边缘]
trending: yes
trending_why: 同一份路由能直接跑在边缘节点和多种运行时上，很多新接口把它当成默认框架。
---

## 它解决什么问题

一个很小的 HTTP 接口，往往被框架的启动方式绑在某一种运行时上。换到边缘节点、Bun 或 Deno，路由和中间件就得重写。Hono 把路由写在 Web 标准的 Request 和 Response 上，同一份代码可以放在 Node、Bun、Deno 和 Cloudflare Workers 这类边缘运行时里。

## 核心功能

- 路由和中间件。路径、方法和中间件按顺序组合，返回标准的 Response。
- 多运行时适配。同一套应用接到不同平台的入口，而不是为每个平台重写路由。
- 常用的接口零件。请求校验、跨域、静态文件和简单的 RPC 助手都在这个生态里，需要时再加。

## 通常怎么用

新的 JSON 接口、Webhook 和边缘上的轻量服务，会先用 Hono 把路由定下来，再决定部署到哪一种运行时。已有的大型 Express 或 Nest 应用不必为了换框架而迁移。它适合接口本身不大、但运行的地方经常变的场景。

## 它不负责什么

Hono 不提供数据库、任务队列和登录产品。部署、证书和扩容仍由运行时或平台负责。中间件要自己挑选，它不会变成一套完整的后台管理系统。

## 许可与热度

MIT。2026-10-10，`honojs/hono` 有 32,469 星。
