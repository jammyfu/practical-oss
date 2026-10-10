---
name: Valkey
slug: valkey
category: data
primary_repo: valkey-io/valkey
url: https://github.com/valkey-io/valkey
website: https://valkey.io/
license: BSD-3-Clause
language: C
stars: 27391
stars_at: 2026-10-10
summary: 在 Redis 改许可之前的代码上继续开发的内存数据结构服务。
tags: [缓存, 开源分支]
---

## 它解决什么问题

很多系统已经按 Redis 协议和命令写好了客户端。Redis 上游改变许可证之后，希望继续使用 OSI 认可许可的部署需要一条兼容的下游。Valkey 由这条需求产生，目标是保持原有的使用方式，同时留在 BSD 许可下。

## 核心功能

- 兼容 Redis 生态里常见的键值、集合、过期和持久化用法。
- 继续使用原有的客户端协议，多数 Redis 客户端可以连上来。
- 由 Linux 基金会托管，按开源项目的方式接收贡献。
- 面向缓存、计数、会话和轻量队列这些 Redis 已经覆盖的场景。

## 通常怎么用

新的基础设施如果要求依赖许可证清晰，会直接部署 Valkey。已有 Redis 7.2 一代部署、又不能接受新许可证的团队，会评估协议兼容之后迁移。客户端代码通常不用重写，要核对的是具体命令、持久化和集群行为是否与所用版本一致。

## 它不负责什么

它不是「所有 Redis 商业模块的开源替代」。Redis 公司后来加入的专有功能不要假设这里都有。迁移前仍要做版本对照和备份恢复演练。它同样不适合当分析数据库或唯一的持久业务账本。

## 许可与热度

BSD-3-Clause。2026-10-10，`valkey-io/valkey` 有 27,391 星。星标低于 Redis，因为它更年轻。收录它是因为许可连续性本身就是广泛部署时要解决的问题。
