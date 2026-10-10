---
name: OpenTelemetry Collector
slug: opentelemetry-collector
category: observe
primary_repo: open-telemetry/opentelemetry-collector
url: https://github.com/open-telemetry/opentelemetry-collector
website: https://opentelemetry.io
license: Apache-2.0
language: Go
stars: 7647
stars_at: 2026-10-10
summary: 接收、加工并转发指标、日志和调用链，不绑定某一家存储。
tags: [遥测, 管道]
trending: yes
trending_why: 新系统的指标、日志和调用链越来越先进入这条与厂商无关的管道，再送到各自的存储。
stars_note: "星标只计收集器仓库。规范和各语言 SDK 在别的仓库，采用范围比这个数字大。"
---

## 它解决什么问题

指标、日志和调用链如果各自直连一家厂商的代理，换存储就要改每一台机器上的采集器。OpenTelemetry Collector 站在应用和存储中间：接收标准遥测，做过滤和批处理，再导出到 Prometheus、Loki 或其他后端。换后端时改的是导出配置，不是每一种语言的埋点。

## 核心功能

- 接收、处理和导出。一条管道把数据接进来，加工后再送出去，三种信号可以用不同的管道。
- 厂商中立。协议是 OpenTelemetry 的，存储可以是自建的，也可以是某家的后端。
- 核心组件有限。常用的接收器和导出器在这个仓库，更多后端连接在 `opentelemetry-collector-contrib`。

## 通常怎么用

新服务用 OpenTelemetry SDK 打点，旁边或节点上跑一个 Collector，统一做采样、批处理和转发。已有的 Prometheus 抓取可以继续，Collector 负责把新的追踪和日志接进同一条路。它不替代长期存储，后面仍要有 Prometheus、Loki、Tempo 或别的库。

## 它不负责什么

Collector 不保存长期历史，不画图，也不在业务代码里自动插桩。核心仓库没有每一种商业后端的导出器，缺的组件要看 contrib 发行版。管道配置错误时数据会丢，它不会替你保留一份本地全量档案。

## 许可与热度

Apache-2.0。2026-10-10，`open-telemetry/opentelemetry-collector` 有 7,647 星。这个仓库只是收集器，整个 OpenTelemetry 的采用远大于该数字。
