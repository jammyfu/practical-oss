---
name: Prometheus
slug: prometheus
category: observe
primary_repo: prometheus/prometheus
url: https://github.com/prometheus/prometheus
website: https://prometheus.io/
license: Apache-2.0
language: Go
stars: 66456
stars_at: 2026-10-10
summary: 定时拉取指标并保存在时序库里，用 PromQL 查询服务是否偏离正常范围。
tags: [监控, 指标]
---

## 它解决什么问题

服务出了问题，只看机器的 CPU 总平均值往往太晚，也看不出是哪一个接口变慢。Prometheus 让应用主动暴露请求数、延迟和错误率，再由监控系统周期性拉走，形成可以按时间查询的指标。

## 核心功能

- 拉取模型。应用提供一个指标端点，Prometheus 按间隔抓取。
- 本地时序存储，以及用 PromQL 做聚合、速率和告警表达式。
- 服务发现。在 Kubernetes 等环境里自动找到要抓的目标。
- Alertmanager 负责把告警分组、抑制并送到邮件或即时通讯。

## 通常怎么用

应用埋点后，Prometheus 抓取指标，Grafana 负责画图，告警规则负责喊人。它是云原生监控里最常见的指标层。日志和调用链不是它的主数据，那些通常交给 Loki、Elasticsearch 或专门的追踪系统。

## 它不负责什么

单机 Prometheus 不是无限期保存全部高基数指标的方案。每个用户一个时间序列这种标签用法会把存储打爆。长期存储和多集群全局查询需要额外组件。它也不绘制仪表板，图在 Grafana 或其他前端里。

## 许可与热度

Apache-2.0。2026-10-10，`prometheus/prometheus` 有 66,456 星。它是 Kubernetes 生态里指标监控的默认协议来源，很多云监控都兼容这个格式。
