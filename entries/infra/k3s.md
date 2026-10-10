---
name: K3s
slug: k3s
category: infra
primary_repo: k3s-io/k3s
url: https://github.com/k3s-io/k3s
website: https://k3s.io
license: Apache-2.0
language: Go
stars: 34160
stars_at: 2026-10-10
summary: 用一个轻量发行版把 Kubernetes 跑在小集群、分支机构和边缘节点上。
tags: [Kubernetes, 边缘]
stars_note: "星标低于 kubernetes/kubernetes。小集群和边缘场景里它经常是默认发行版。"
---

## 它解决什么问题

完整的 Kubernetes 安装要自己凑控制平面、容器运行时和一堆附加组件，一台小机器或一批边缘节点扛不住这套手续。K3s 把经过认证的 Kubernetes 收成一个发行版，用较少的内存和一条安装路径把集群拉起来。

## 核心功能

- 单二进制发行。控制平面和常用组件打包在一起，少做一轮手工拼装。
- 小规模数据存储。小集群可以用内嵌的轻量数据库，需要高可用时再换到外部存储。
- 标准工作负载。Deployment、Service 这些 Kubernetes 对象仍然是那一套，清单大多可以直接用。
- 边缘和分支。在网络和机器都不大的地方保持和数据中心相同的部署方式。

## 通常怎么用

实验室、门店、边缘机房和只有几台机器的生产集群，会用 K3s 代替从零安装 Kubernetes。应用清单仍按 Kubernetes 来写。集群变大、需要云厂商托管控制平面时，再评估完整发行版或托管服务。

## 它不负责什么

K3s 不减少 Kubernetes 本身的对象和概念。备份、升级、入口、持久卷和权限仍然要设计。它也不是单机的 Docker Compose 替代品，只有一个容器时用它偏重。

## 许可与热度

Apache-2.0。2026-10-10，`k3s-io/k3s` 有 34,160 星。这个数字低于主仓库 `kubernetes/kubernetes`，不代表小集群里用得少。
