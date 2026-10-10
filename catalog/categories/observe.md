# 观测与安全

服务跑起来之后，看指标、看图、查已知漏洞。

返回 [目录](../../README.md)。跨分类的名单在 [历史最高](../history.md) 和 [当前热度最高](../trending/2026-10-10/index.md)。

## 近两年的新默认

这一节只放本类里标了 `trending: yes` 的项目，按总星标从高到低。它不是今日、本周或本月的趋势榜。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [OpenTelemetry Collector](../../entries/observe/opentelemetry-collector.md) | 接收、加工并转发指标、日志和调用链，不绑定某一家存储。 | Apache-2.0 | 7,647（见正文） |
| [Grafana Alloy](../../entries/observe/alloy.md) | 用一条流水线采集指标、日志和追踪，送到 Grafana 那一套后端。 | Apache-2.0 | 3,593（见正文） |

## 历史最高

这一节是本类里的长期默认，按星标从高到低。星标不是采用率，镜像仓库尤其不能只看这个数字。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Grafana](../../entries/observe/grafana.md) | 把指标、日志和追踪查询画成仪表板，并挂上告警。 | AGPL-3.0 | 77,209 |
| [Prometheus](../../entries/observe/prometheus.md) | 定时拉取指标并保存在时序库里，用 PromQL 查询服务是否偏离正常范围。 | Apache-2.0 | 66,456 |
| [Trivy](../../entries/observe/trivy.md) | 扫描容器镜像、文件系统和配置，找出已知漏洞、密钥和错误配置。 | Apache-2.0 | 38,314 |
| [Loki](../../entries/observe/loki.md) | 按标签收集和查询日志，供 Grafana 和告警直接使用。 | AGPL-3.0 | 29,005 |

星标取自 GitHub API，统计日见各条目的 `stars_at`。星标只说明仓库被关注的程度，不代替采用率。PostgreSQL 这类镜像仓库星标偏低，仍然是行业默认选择。
