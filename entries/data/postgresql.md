---
name: PostgreSQL
slug: postgresql
category: data
primary_repo: postgres/postgres
url: https://github.com/postgres/postgres
website: https://www.postgresql.org/
license: PostgreSQL
language: C
stars: 22323
stars_at: 2026-10-10
stars_note: "postgres/postgres 是官方镜像，不接受 GitHub 拉取请求。星标严重低估它作为默认关系数据库的地位。"
summary: 用事务保存业务数据，并用 SQL 同时完成约束、查询和不少分析。
tags: [数据库, SQL]
---

## 它解决什么问题

业务数据需要在失败时整笔回滚，需要外键和唯一约束，还需要能按条件查询。文件和电子表格做不到并发写入下的一致性。PostgreSQL 是一套功能完整的关系数据库，也是很多新系统在 MySQL 之外的默认选择。

## 核心功能

- ACID 事务、行级锁，以及可预期的约束检查。
- SQL 查询，包括连接、窗口函数和公共表表达式。
- 扩展类型。JSON、数组、全文检索、地理信息和自定义类型都在同一套表里。
- 扩展机制。PostGIS 等能力以扩展接入，而不必换成另一个数据库。

## 通常怎么用

Web 应用的主库、订单和账户系统、需要复杂查询的内部平台，都会把它当作唯一的事实来源。应用通过驱动或 ORM 连接它。只做嵌入式、单文件、无服务进程的本地分析时，SQLite 或 DuckDB 更合适。

## 它不负责什么

它不自动分片成全球多活系统，分布式拓扑要另选扩展或上层架构。它也不是缓存，高频临时计数通常仍会放进内存数据库。备份、故障转移和版本升级是运维流程，不属于「建一张表」的范围。

## 许可与热度

PostgreSQL License 是类似 BSD/MIT 的宽松许可。2026-10-10，镜像仓库只有 22,323 星。贡献走项目自己的邮件列表，不走这个 GitHub 仓库的拉取请求。
