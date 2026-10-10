---
name: Gin
slug: gin
category: backend
primary_repo: gin-gonic/gin
url: https://github.com/gin-gonic/gin
website: https://gin-gonic.com/
license: MIT
language: Go
stars: 89305
stars_at: 2026-10-10
summary: 用很少的封装在 Go 里写 HTTP 路由、参数绑定和中间件。
tags: [API, Go]
---

## 它解决什么问题

Go 标准库可以写 HTTP 服务，但路由分组、JSON 绑定、中间件顺序这些每项目都会再写一遍。Gin 提供一层薄的 Web 框架，把这些重复结构固定下来，同时保持 Go 服务常见的显式写法。

## 核心功能

- 按路径和方法注册处理函数，支持路径参数和路由分组。
- 把请求体、查询和表单绑定到结构体，并做基本校验。
- 中间件。日志、恢复 panic、认证和跨域可以按组挂上。
- 渲染 JSON、XML 或模板。大多数使用者只用 JSON。

## 通常怎么用

Go 微服务、内部接口和网关旁边的小服务会选它。项目结构仍然由团队自己定，Gin 不生成完整的业务骨架。需要更厚的依赖注入、配置和模块体系时，有人会改用其他 Go 框架，或只使用标准库。

## 它不负责什么

它不包含数据库、迁移、用户系统和远程过程调用。性能优势依赖处理函数本身不做什么蠢事。校验失败的错误格式要自己统一，框架不会替一个组织规定接口规范。

## 许可与热度

MIT。2026-10-10，`gin-gonic/gin` 有 89,305 星。在 Go HTTP 框架里，它是最常出现在示例和现有服务中的一个。
