---
name: OpenSearch
slug: opensearch
category: data
primary_repo: opensearch-project/OpenSearch
url: https://github.com/opensearch-project/OpenSearch
website: https://opensearch.org/
license: Apache-2.0
language: Java
stars: 13833
stars_at: 2026-10-10
summary: Apache-2.0 的搜索和分析引擎，从 Elasticsearch 7.10.1 继续开发。
tags: [搜索, 分析]
stars_note: "星标低于 Elasticsearch。它是 2021 年起以 Apache-2.0 继续的分支，部署不一定反映在这个仓库的星标上。"
---

## 它解决什么问题

全文检索、日志聚合和面向搜索的分析，需要倒排索引和水平分片。Elasticsearch 在 7.10.1 之后改了上游许可。OpenSearch 从那一版的 Apache-2.0 代码继续做搜索引擎，给还要 OSI 开源许可的部署留一条主干。

## 核心功能

- 索引和搜索。文档写入索引，按全文、过滤和聚合查询。
- 分片和副本。索引拆到多个节点，用副本来扛节点故障。
- 分析负载。时间序列和日志可以放进来做聚合，但它的设计中心仍是搜索，不是事务库。
- 接口继承自分支起点。原有的索引和查询方式大多还能接上，版本差异要单独核对。

## 通常怎么用

需要自建搜索或日志分析、并且要求 Apache-2.0 的团队，会部署 OpenSearch 集群。控制台在另一个仓库 `OpenSearch-Dashboards`，不在这个引擎仓库里。已有的 Elastic 商业功能不要假设这里都有对应实现。

## 它不负责什么

OpenSearch 不替代 PostgreSQL 这类事务数据库，也不包含 Dashboards 的界面。从较新的 Elasticsearch 迁过来时，只有 Elastic License 的功能对不上。集群的磁盘、堆内存和分片规划仍然要自己做。

## 许可与热度

Apache-2.0。2026-10-10，`opensearch-project/OpenSearch` 有 13,833 星。星标低于 Elasticsearch，不代表这条 Apache-2.0 分支用得少。
