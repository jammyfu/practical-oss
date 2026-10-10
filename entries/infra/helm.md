---
name: Helm
slug: helm
category: infra
primary_repo: helm/helm
url: https://github.com/helm/helm
website: https://helm.sh/
license: Apache-2.0
language: Go
stars: 30306
stars_at: 2026-10-10
summary: 把一组 Kubernetes 资源配置打包成可版本化、可按环境改参数的图表。
tags: [Kubernetes, 发布]
---

## 它解决什么问题

一个应用在 Kubernetes 上往往同时需要部署、服务、配置和入站规则。这些文件复制到每个环境后，只改镜像版本和域名也会越来越难审。Helm 把这组文件收成图表，用一份值文件覆盖环境差异。

## 核心功能

- Chart。一组模板化的 Kubernetes 清单，加上默认值。
- 安装、升级和回滚。一次发布被记录成一个版本，失败时可以回到上一版。
- 仓库。图表可以像包一样发布和依赖别的图表。
- 模板只在安装时渲染成普通的 Kubernetes 对象，集群里运行的仍是那些对象。

## 通常怎么用

团队用它发布自己的服务，也用它安装 Prometheus、Ingress 控制器这类集群组件。环境差异放在值文件里，模板留在图表里。只有几个几乎不变的清单时，直接应用 YAML 更清楚。

## 它不负责什么

Helm 不创建集群，也不构建容器镜像。模板逻辑写复杂以后会难以阅读，它不阻止这件事。回滚恢复的是它提交过的 Kubernetes 对象，不自动恢复数据库里的数据。

## 许可与热度

Apache-2.0。2026-10-10，`helm/helm` 有 30,306 星。它是 Kubernetes 上最常见的打包和发布工具。
