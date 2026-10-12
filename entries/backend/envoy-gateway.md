---
name: Envoy Gateway
slug: envoy-gateway
category: backend
primary_repo: envoyproxy/gateway
url: https://github.com/envoyproxy/gateway
website: https://gateway.envoyproxy.io
license: Apache-2.0
language: Go
stars: 3074
stars_at: 2026-10-12
summary: 用 Gateway API 管理 Envoy，把集群入口的路由和策略从 Ingress 注解里拆出来。
tags: [网关, Gateway API]
trending: yes
trending_why: 2024 年发布 1.0；Ingress NGINX 在 2026 年 3 月停止维护后，它成为迁到 Gateway API 的常见实现。
stars_note: "星标低于 Envoy 本体。它是 Gateway API 的实现之一，不是 Ingress NGINX 的唯一后继。"
---

## 它解决什么问题

Kubernetes 上对外的 HTTP 入口，很多年靠 Ingress 加上控制器自己的注解。注解各家不通用，换实现就要重写。Ingress NGINX 在 2026 年 3 月停止维护之后，这条默认路径断了。Envoy Gateway 用 Kubernetes Gateway API 描述入口，由它去配置真正转发流量的 Envoy。

## 核心功能

- Gateway API。用 Gateway、HTTPRoute 这些对象写主机、路径、权重和转发，而不是堆注解。
- 托管 Envoy。控制面负责把代理拉起来、升级，并按路由下发配置。
- 常见入口策略。限流、认证一类需求用它自己的策略对象补充，不必改业务进程。
- 也能离开 Kubernetes 单独跑，面向不是只在集群里暴露服务的场合。

## 通常怎么用

还在用 Ingress NGINX、又决定改到 Gateway API 的团队，会拿它做一个实现来试。新的集群如果本来就要 Envoy 的七层能力，又不想上一整套服务网格，也会直接从它开始。Cilium、云厂商网关和其他 Gateway API 实现仍然同时存在，选哪一个要看现有网络和要保留的注解。

## 它不负责什么

Envoy Gateway 不是 Envoy 本身，也不替代服务网格里的东西向流量。它不保存指标和日志，只把代理配好。Ingress 上的注解不会自动全部有对应物，迁的时候要逐条看。Ingress 这个 API 还在，停掉的是 Ingress NGINX 这个控制器。它也不签发你的业务证书的组织流程，证书对象仍要另接。

## 许可与热度

Apache-2.0。2026-10-12，`envoyproxy/gateway` 有 3,074 星。仓库从 2022 年起步，1.0 在 2024 年发布。这个数字低于 `envoyproxy/envoy`，不能据此判断入口已经没有人从 Ingress NGINX 迁出。
