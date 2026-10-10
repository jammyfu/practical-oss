---
name: PocketBase
slug: pocketbase
category: selfhost
primary_repo: pocketbase/pocketbase
url: https://github.com/pocketbase/pocketbase
website: https://pocketbase.io/
license: MIT
language: Go
stars: 61338
stars_at: 2026-10-10
summary: 一个可执行文件里带上数据库、用户鉴权和文件接口，给小应用当后端。
trending: yes
trending_why: 小产品不想自建一整套后端时，单文件加 SQLite 成了托管 BaaS 之外的常见选择。
tags: [后端, 自托管]
---

## 它解决什么问题

做原型或小产品时，只为了用户、几张表和上传文件就去搭配数据库、鉴权服务和对象存储，运维比功能还重。PocketBase 把这些收进一个 Go 程序，数据落在嵌入式 SQLite 上，打开管理界面就能建集合并得到对应接口。

## 核心功能

- 单文件部署，管理界面里定义集合、字段和访问规则。
- 用户注册、登录和令牌，以及基于规则的记录级权限。
- 文件上传存在本地，也可以接到对象存储。
- 记录变更可以实时推给客户端。扩展用 Go 嵌入，或用 JavaScript 钩子。

## 通常怎么用

个人项目、内部工具和早期产品用它当整个后端：前端直接调它的接口，管理员在网页里改数据。数据量还小、写入以单机为主时，这种形态最省事。应用变大以后，人们往往把同一套数据迁到独立数据库，而不是一直垂直放大这一台进程。

## 它不负责什么

它不提供多主写入、跨地域副本和企业级审计平台。SQLite 的写入并发有上限，不适合当成高冲突的交易主库。客户端框架、推送证书和业务里的支付对账也不在这个程序里。升级前仍要备份那一个数据目录，单文件不等于数据不会丢。

## 许可与热度

MIT。2026-10-10，`pocketbase/pocketbase` 有 61,338 星。它是自托管小型后端里关注度很高的项目，选型时仍要按写入量和备份要求看，而不是只看部署有多省事。
