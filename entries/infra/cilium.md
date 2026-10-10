---
name: Cilium
slug: cilium
category: infra
primary_repo: cilium/cilium
url: https://github.com/cilium/cilium
website: https://cilium.io
license: Apache-2.0
language: Go
stars: 25625
stars_at: 2026-10-10
summary: 用 eBPF 给 Kubernetes 提供网络、网络策略和流量可观测性。
tags: [网络, eBPF]
---

## 它解决什么问题

集群里的网络策略如果只靠 iptables，规则一多就难查，也难看见到底是谁连了谁。Cilium 用 eBPF 在内核里做容器网络，承担 Pod 之间的连通、网络策略，以及 kube-proxy 那一层的服务转发。

## 核心功能

- 容器网络。作为 CNI 给 Pod 分配连通性，并执行网络策略。
- 服务转发。可以接过 kube-proxy 的工作，用 eBPF 做服务负载均衡。
- 流量观察。Hubble 看流经集群的访问，排「策略是不是把这条流量挡住了」。
- 网络加密和多集群连通在上游能力之内，要按集群版本和内核条件单独启用。

## 通常怎么用

新建的 Kubernetes 集群会把 Cilium 选成默认 CNI，尤其是需要网络策略和更清楚的流量记录时。已有的云厂商 CNI 不一定能直接替换，要先核对托管集群允许哪一种网络插件。

## 它不负责什么

Cilium 不代替 Kubernetes 控制平面，也不保存应用指标和日志。eBPF 依赖足够新的内核，老系统上有的能力不可用。应用自己的鉴权和业务限流仍然在服务里面。

## 许可与热度

Apache-2.0。2026-10-10，`cilium/cilium` 有 25,625 星。它是 CNCF 毕业项目，部署范围大于仓库星标。
