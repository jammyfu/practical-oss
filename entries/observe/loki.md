---
name: Loki
slug: loki
category: observe
primary_repo: grafana/loki
url: https://github.com/grafana/loki
website: https://grafana.com/oss/loki
license: AGPL-3.0
language: Go
stars: 29005
stars_at: 2026-10-10
summary: 按标签收集和查询日志，供 Grafana 和告警直接使用。
tags: [日志, Grafana]
---

## 它解决什么问题

日志散在每台机器的文件里，出了事故才登录去翻。把每行都送进全文搜索引擎又贵。Loki 按标签组织日志流，先用标签缩小到某一组服务，再在这组流里查内容，查询和存储的成本模型与全文索引不同。

## 核心功能

- 标签索引。服务名、环境和级别这类标签用来定位日志流。
- 收集与查询。采集端把日志推过来，查询语言在选定的流里过滤文本。
- 和 Grafana 配套。面板、探索视图和告警可以直接对着 Loki。
- 对象存储。日志块可以放到对象存储里，不必所有内容都留在本地磁盘。

## 通常怎么用

已经用 Prometheus 和 Grafana 的团队，会用 Loki 放同一套系统的日志。标签在采集时定好，和指标的标签尽量对齐，这样从一张图跳到对应日志时对得上。要全库随意做复杂全文检索时，它不是 Elasticsearch 那种搜索引擎。

## 它不负责什么

Loki 不采集主机指标，不保存调用链，也不负责把日志从应用里打出来。标签基数太高时，索引和查询都会变贵。它不保证日志里没有敏感字段，脱敏要在采集前做。

## 许可与热度

AGPL-3.0。自己改了以后如果通过网络提供服务，要按 AGPL 向用户提供对应源码。2026-10-10，`grafana/loki` 有 29,005 星。
