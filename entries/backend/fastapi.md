---
name: FastAPI
slug: fastapi
category: backend
primary_repo: fastapi/fastapi
url: https://github.com/fastapi/fastapi
website: https://fastapi.tiangolo.com/
license: MIT
language: Python
stars: 102954
stars_at: 2026-10-10
summary: 用 Python 类型声明描述 HTTP 接口，并自动给出校验和可交互的接口文档。
tags: [API, Python]
---

## 它解决什么问题

写 JSON 接口时，参数校验、错误格式和文档经常各写一遍，三处还会不一致。FastAPI 让路径函数的类型注解同时承担三件事：运行时校验、编辑器提示，以及 OpenAPI 文档。

## 核心功能

- 路由和依赖注入。请求进来后，按声明解析路径、查询和请求体。
- 基于 Pydantic 的数据校验。不符合类型的输入会变成明确的错误响应。
- 自动生成 OpenAPI，并带一个可试调用的文档页。
- 异步视图。I/O 密集的接口可以和其他请求交错执行。

## 通常怎么用

机器学习模型服务、内部工具 API 和新的 Python 微服务常用它。一个接口函数加上类型，就能给前端一份实时文档。业务很大、需要管理后台、权限、表单和服务器端页面时，Django 那类全栈框架更完整。

## 它不负责什么

它不包含数据库迁移、用户系统和任务队列。这些通过 SQLAlchemy、Alembic 或其他库自己接。异步写错时，阻塞调用仍会堵住事件循环。类型注解也只检查接口边界，替不了业务测试。

## 许可与热度

MIT。2026-10-10，`fastapi/fastapi` 有 102,954 星。它是目前新 Python HTTP API 最常见的起点之一。
