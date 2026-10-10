---
name: Redis
slug: redis
category: data
primary_repo: redis/redis
url: https://github.com/redis/redis
website: https://redis.io/
license: RSALv2 OR SSPL-1.0
language: C
stars: 76678
stars_at: 2026-10-10
summary: 把键值、集合和过期时间放在内存里，用来做缓存、计数、队列和短期状态。
tags: [缓存, 许可变更]
---

## 它解决什么问题

主数据库每次都从磁盘读热数据，会把延迟和连接数花在重复查询上。登录会话、验证码、排行榜和简单队列需要的是很快的读写和自动过期，不是复杂事务报表。Redis 用内存中的数据结构响应这类访问。

## 核心功能

- 字符串、哈希、列表、集合和有序集合等结构，每条数据可以设置过期。
- 单线程命令模型让单个命令的执行顺序容易理解，再用 I/O 多路复用承接连接。
- 发布订阅、流和简单的阻塞队列语义。
- 持久化可选。可以只当缓存，也可以把数据写回磁盘。

## 通常怎么用

Web 应用把它放在关系数据库前面做缓存，或用它保存会话和限流计数。队列系统会用列表或流做轻量工作分发。需要开源许可延续、并且要避开 2024 年后的许可证时，应看 Valkey，而不是默认使用当前 Redis 上游。

## 它不负责什么

Redis 不是分析仓库，也不适合当作唯一的财务账本。内存用满以后，淘汰策略会丢数据或让写入失败，这要在设计时定下来。集群分片后，跨槽的多键操作有限制。

## 许可与热度

2024 年起，Redis 上游新版本使用 Redis Source Available License 2.0 或 Server Side Public License 1.0，二者都不是 OSI 开源定义下的许可。更早版本曾使用 BSD。2026-10-10，`redis/redis` 有 76,678 星。要 OSI 开源许可时，选用从变更前代码继续开发的 Valkey。
