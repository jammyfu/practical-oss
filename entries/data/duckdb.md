---
name: DuckDB
slug: duckdb
category: data
primary_repo: duckdb/duckdb
url: https://github.com/duckdb/duckdb
website: https://duckdb.org/
license: MIT
language: C++
stars: 42053
stars_at: 2026-10-10
summary: 嵌在进程里的分析型数据库，直接对本地文件和表格数据跑 SQL。
trending: yes
trending_why: 本地用 SQL 分析 CSV 和 Parquet 时，成为 SQLite 之外的新默认。
tags: [分析, SQL]
---

## 它解决什么问题

分析一批 CSV、Parquet 或日志时，为了几条 SQL 去部署一套数据仓库太重。把数据全载进电子表格又会撞上体积和可重复性。DuckDB 像 SQLite 一样嵌进当前进程，但优化的是列式分析查询，而不是大量小事务。

## 核心功能

- 进程内 SQL 引擎，没有单独的服务器要启动。
- 直接查询 CSV、Parquet 和 JSON 等文件，也能连到一些远程对象存储上的表。
- 列式执行，适合聚合、扫描和连接分析。
- 给 Python、R、命令行和其他语言提供绑定。

## 通常怎么用

数据分析师在笔记本里用它探索文件。工程师用它在本地复现一段指标 SQL，再决定要不要搬到仓库。它也出现在应用内部，充当嵌入式分析引擎。高并发的在线交易写入不是它的目标。

## 它不负责什么

它不替代 PostgreSQL 做业务主库，也不负责多用户调度、权限平台和报表门户。查询快依赖于数据布局和文件格式，不是把任意 CSV 丢进去就一定适合交互分析。

## 许可与热度

MIT。2026-10-10，`duckdb/duckdb` 有 42,053 星。它在本地分析这条路上已经成为 SQLite 之外最常被拿来对比的名字。
