---
name: Elasticsearch
slug: elasticsearch
category: data
primary_repo: elastic/elasticsearch
url: https://github.com/elastic/elasticsearch
website: https://www.elastic.co/products/elasticsearch
license: AGPL-3.0-only OR SSPL-1.0 OR Elastic-2.0
language: Java
stars: 78223
stars_at: 2026-10-10
summary: 做全文检索和聚合分析。默认源码可在 AGPL、SSPL 和 Elastic License 里选一种。
tags: [搜索, 许可可选]
---

## 它解决什么问题

业务库不擅长「这段文字像什么」和「按条件聚合几亿条日志」。Elasticsearch 把文档放进倒排索引，做全文检索、过滤和聚合，也可以作为日志和指标分析的存储。它是搜索引擎，不是事务数据库。

## 核心功能

- 索引和查询。文档按映射写入，用查询语言做全文、过滤和聚合。
- 集群。索引分成片，副本分布到节点上，用来扩展和抗单点故障。
- 分析场景。日志、事件和站内搜索是最常见的用法，分析接口和搜索接口在同一套引擎上。
- 安全、机器学习和一部分观测功能在仓库的 x-pack 目录，许可和默认源码不同，见下一节。

## 通常怎么用

站内搜索、日志平台和需要聚合查询的事件流，会建 Elasticsearch 集群，由应用或采集器写入。选许可时要先决定用哪一种，再决定能不能改源码、能不能把它做成对外的托管服务。要求 Apache-2.0 时，看从 7.10.1 继续的 OpenSearch，而不是假设当前上游仍是 Apache-2.0。

## 它不负责什么

Elasticsearch 不承担需要事务和强一致约束的主账本。分片、映射和磁盘规划做错时，查询会慢或写会失败。它也不包含 Kibana 那个界面仓库。仓库简介里的 “Free and Open Source” 不能代替许可证文件。

## 许可与热度

`LICENSE.txt` 写明：除文件头另有说明外，默认源码是三选一，GNU Affero General Public License v3.0 only、Server Side Public License v1，或 Elastic License 2.0。选 AGPL-3.0-only 时，这是 OSI 开源许可，通过网络提供修改版要按 AGPL 提供对应源码。SSPL-1.0 和 Elastic License 2.0 都不是 OSI 开源定义下的许可。只出现在 x-pack 目录、且文件头写明单独适用 Elastic License 2.0 的代码，不能改按 AGPL 使用。2026-10-10，`elastic/elasticsearch` 有 78,223 星。
