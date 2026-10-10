---
name: Spring Boot
slug: spring-boot
category: backend
primary_repo: spring-projects/spring-boot
url: https://github.com/spring-projects/spring-boot
website: https://spring.io/projects/spring-boot
license: Apache-2.0
language: Java
stars: 81581
stars_at: 2026-10-10
summary: 用约定和起步依赖把 Spring 应用装成可运行的 Java 服务。
tags: [Java, 服务]
---

## 它解决什么问题

Spring 能组装企业应用里的对象、事务和 Web 层，但过去要写大量配置才能启动。Spring Boot 把常见组合收成起步依赖：选了 Web、数据库和安全，就得到一套能跑的默认配置，再只覆盖需要改的部分。

## 核心功能

- 可执行的应用入口。内嵌 Web 服务器，不必先在外部容器里部署。
- 起步依赖。一组依赖对应一条常见能力，版本由依赖管理对齐。
- 自动配置。类路径上出现什么库，就注册对应的默认对象。
- 生产端点、外部化配置和配置文件，用来区分环境。

## 通常怎么用

企业和政府项目里的 Java 服务、需要事务和复杂集成的业务系统，很多以它为标准骨架。HTTP 接口、消息消费和定时任务都可以放在同一个应用模型里。很小的无状态接口有时会改用 Go 或更轻的 Java 框架，以免带上整套约定。

## 它不负责什么

Spring Boot 不规定前端，也不等于全部 Spring 项目。自动配置会在不了解默认值时显得隐秘，出问题要会看它为什么启用了某个对象。业务正确性、数据库设计和权限模型仍要单独设计。

## 许可与热度

Apache-2.0。2026-10-10，`spring-projects/spring-boot` 有 81,581 星。Java 服务端里，它是目前最普遍的应用框架。
