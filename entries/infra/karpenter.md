---
name: Karpenter
slug: karpenter
category: infra
primary_repo: kubernetes-sigs/karpenter
url: https://github.com/kubernetes-sigs/karpenter
website: https://karpenter.sh/
license: Apache-2.0
language: Go
stars: 2219
stars_at: 2026-10-11
summary: 按排不上的 Pod 直接申请和回收 Kubernetes 节点。
tags: [Kubernetes, 节点伸缩]
trending: yes
trending_why: 2024 年 1.0 之后，不少集群用它取代按节点组加减机器的做法，核心也交到了 Kubernetes 社区。
stars_note: "核心仓库星标低于 AWS 实现。很多人安装的是 aws/karpenter-provider-aws。"
---

## 它解决什么问题

Kubernetes 里 Pod 排不上去时，常见做法是事先划好几种节点组，再让自动伸缩在组内加减机器。组划小了，特殊规格的 Pod 没有去处；组划大了，机器空转。Karpenter 反过来看已经排不上的 Pod，按它们的资源、架构和容忍条件申请合适的节点，用完再收掉。

## 核心功能

- 盯着调度失败的 Pod。节点选择、亲和、资源请求和拓扑约束都参与计算。
- 按需求创建节点。容量类型、CPU 架构和实例规格写在节点池里，而不是先固定一组机型。
- 合并与回收。节点空出来或利用率过低时，可以把工作负载挪走并删掉机器。
- 云厂商分开实现。核心在 Kubernetes 社区，AWS、Azure、GCP 以及其他云各有自己的提供者。

## 通常怎么用

已经在用托管 Kubernetes、又嫌节点组种类越来越多的团队，会把节点伸缩从 Cluster Autoscaler 评估到 Karpenter。2024 年 1.0 稳定了 v1 接口之后，这种换法变常见。EKS 上很多人直接安装 AWS 那一份提供者。别的云要换对应的实现，不能把 AWS 的节点类原样拿过去。

## 它不负责什么

Karpenter 不调度 Pod，那仍是 kube-scheduler 的工作。它不创建控制平面，也不替你申请云账号里的配额和权限。节点上的系统镜像、入站流量和权限策略要另外声明。Cluster Autoscaler 还在维护，不是每个集群都必须换。核心仓库不含某一朵云的全部细节，对不上版本时要看提供者自己的发布说明。

## 许可与热度

Apache-2.0。2026-10-11，核心仓库 `kubernetes-sigs/karpenter` 有 2,219 星。同日 `aws/karpenter-provider-aws` 有 7,722 星，`aws/karpenter` 指向这份 AWS 实现。Azure 的提供者同日有 557 星。看热度时要把核心和实际安装的那一份分开，不能用核心仓库的星标判断它在 EKS 上少见。
