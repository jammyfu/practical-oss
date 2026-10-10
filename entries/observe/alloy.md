---
name: Grafana Alloy
slug: alloy
category: observe
primary_repo: grafana/alloy
url: https://github.com/grafana/alloy
website: https://grafana.com/oss/alloy
license: Apache-2.0
language: Go
stars: 3593
stars_at: 2026-10-10
summary: 用一条流水线采集指标、日志和追踪，送到 Grafana 那一套后端。
tags: [采集, Grafana]
trending: yes
trending_why: 2024 年发布，用来接替 Grafana Agent，成为 Grafana 体系里新的采集端。
stars_note: "仓库 2024 年才建立，星标低于它要接上的 Grafana 和 Loki。"
---

## 它解决什么问题

Grafana 体系里，指标、日志和追踪以前往往各跑一个采集程序。Grafana Agent 停在旧的入口之后，官方用 Alloy 接替它。Alloy 用一种流水线配置把采集、转换和送出写在一起，减少每台机器上采集器的种类。

## 核心功能

- 流水线。组件接成一条链，从抓取或接收，到改写标签，再到送出。
- 多种信号。可以抓 Prometheus 指标、收日志，也接收 OpenTelemetry 的追踪。
- 送往原有后端。数据仍然进 Prometheus 兼容的存储、Loki 或其他导出目标，Alloy 自己不把它们存成查询库。

## 通常怎么用

已经在用 Grafana、Prometheus 和 Loki 的环境，把机器上的 Grafana Agent 换成 Alloy，让采集配置集中到一种写法。新集群也可以直接从 Alloy 开始。只暴露一个 `/metrics`、没有日志和追踪的小服务，继续让 Prometheus 来抓即可。

## 它不负责什么

Alloy 不替代 Grafana 的界面，不替代 Loki 或 Prometheus 的存储，也不负责告警规则怎么写。它是 2024 年开始的采集端，星标还低，不能用星标判断 Grafana 用户是否已经迁完。商业的 Grafana Cloud 采集和这个开源收集器不是同一份授权。

## 许可与热度

Apache-2.0。2026-10-10，`grafana/alloy` 有 3,593 星。仓库新，数字低于 Grafana 和 Loki。
