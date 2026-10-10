---
name: SQLite
slug: sqlite
category: data
primary_repo: sqlite/sqlite
url: https://github.com/sqlite/sqlite
website: https://www.sqlite.org/
license: Public Domain
language: C
stars: 10628
stars_at: 2026-10-10
stars_note: "sqlite/sqlite 是官方源码镜像。SQLite 的部署量远高于这个星标，发布渠道是 sqlite.org。"
summary: 把一个完整的 SQL 数据库放进单个库文件，由应用进程直接读写。
tags: [数据库, 嵌入式]
---

## 它解决什么问题

很多程序需要事务和查询，但用不起、也不该为一个本地应用单独跑数据库服务器。SQLite 把数据库引擎嵌进进程，数据落在一个文件里。复制这个文件，就是复制整库。

## 核心功能

- 进程内 SQL 引擎，支持事务、索引和常见查询。
- 单个数据库文件。备份和移动通常就是复制文件。
- 库可以被手机应用、桌面软件、浏览器和嵌入式设备直接链进去。
- 读多写少时表现稳定。多个读可以并发，写由库自己串行化。

## 通常怎么用

手机应用、桌面配置、测试夹具、边缘设备和本地工具用它保存结构化数据。它也常作为应用的默认存储，等并发写入真正变大再迁到 PostgreSQL。分析扫描大文件时，DuckDB 更合适；高并发的网络服务主库通常不是它。

## 它不负责什么

它没有独立的权限账户体系，也不负责多机复制。写入锁的粒度决定了它不适合大量客户端同时写入同一文件。官方镜像不接受把 GitHub 拉取请求当作贡献入口，开发流程在 SQLite 项目自己的站点上。

## 许可与热度

作者把 SQLite 放在公有领域。2026-10-10，`sqlite/sqlite` 有 10,628 星。它是世界上部署最广的数据库引擎之一，星标没有反映这件事。
