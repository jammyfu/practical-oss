---
name: Polars
slug: polars
category: data
primary_repo: pola-rs/polars
url: https://github.com/pola-rs/polars
website: https://docs.pola.rs/
license: MIT
language: Rust
stars: 40080
stars_at: 2026-10-10
summary: 用列式查询引擎在进程内变换和聚合表格，常用来替代逐行的 DataFrame 写法。
trending: yes
trending_why: 本地和管道里处理中等规模表格时，它已成为相对 pandas 的新默认对比。
tags: [DataFrame, 分析]
---

## 它解决什么问题

用惯了逐行 DataFrame 的人，一旦表变宽、行变多，过滤、分组和连接就会卡在内存拷贝和 Python 循环上。Polars 用 Rust 写的列式引擎处理同一类表格操作，让分析脚本和数据管道不必为了一次聚合就架起数据库服务。

## 核心功能

- DataFrame 和惰性查询。表达式先组成计划，再一起执行，而不是每一步都落成中间表。
- 列式内存布局，适合扫描、过滤、分组和连接。
- 能读常见的表格文件，也能通过 Apache Arrow 和别的工具交换数据。
- 核心在 Rust，Python、Node.js 和 R 有绑定，也可以写 SQL。

## 通常怎么用

分析师在笔记本里用它清洗导出文件。数据工程师在批处理作业里用惰性接口读 Parquet、做聚合，再写出结果。应用内嵌时，它充当进程里的表格引擎。交互式探索和可重复的批处理都能用，但数据仍由调用方决定放在哪里。

## 它不负责什么

它不是数据库服务器，没有账号、持久事务和多用户并发控制。表大过机器内存时，不能指望它自动变成数仓。查询快不快取决于是否走列式表达式，把逐行 Python 循环包一层并不会变快。结果的业务口径、调度和权限也不在这个库里。

## 许可与热度

MIT。2026-10-10，`pola-rs/polars` 有 40,080 星。它是目前最常被拿来替代传统 DataFrame 库的开源查询引擎之一。
