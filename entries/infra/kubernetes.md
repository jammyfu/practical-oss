---
name: Kubernetes
slug: kubernetes
category: infra
primary_repo: kubernetes/kubernetes
url: https://github.com/kubernetes/kubernetes
website: https://kubernetes.io/
license: Apache-2.0
language: Go
stars: 128239
stars_at: 2026-10-10
summary: 在多台机器上声明容器要跑几份、如何发现彼此，以及失败后如何拉回来。
tags: [编排, 集群]
---

## 它解决什么问题

一台机器上的 Docker Compose 解决不了多机调度。服务要扩容、滚动升级、一台节点宕机后自动重排，还要有统一的服务发现和配置入口。Kubernetes 用声明式 API 描述期望状态，再由控制器去逼近这个状态。

## 核心功能

- 工作负载。Deployment、StatefulSet 等对象描述副本数、升级方式和有状态应用。
- 服务发现和负载均衡。集群内用 Service 找到一组容器，外部流量再通过 Ingress 或网关进入。
- 配置和密钥以 API 对象下发，而不是登录每台机器改文件。
- 自愈和滚动更新。节点或容器失败时按声明重新调度。

## 通常怎么用

多个服务、多套环境和需要弹性伸缩的团队，会把容器镜像交到 Kubernetes 集群。云厂商提供托管控制平面，团队主要写清单和发布流程。只有一个应用、一台机器时，它的对象模型和运维面通常过重。

## 它不负责什么

Kubernetes 不构建镜像，不编写业务代码，也不保证应用本身无状态。持久数据、网络策略和权限要单独设计。控制平面健康、升级和成本都是平台工作。把开发环境的全部复杂度搬进集群，不会自动得到可靠性。

## 许可与热度

Apache-2.0。2026-10-10，`kubernetes/kubernetes` 有 128,239 星。它是容器编排的事实标准，学习成本也对应地高。
