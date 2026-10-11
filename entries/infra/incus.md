---
name: Incus
slug: incus
category: infra
primary_repo: lxc/incus
url: https://github.com/lxc/incus
website: https://linuxcontainers.org/incus
license: Apache-2.0
language: Go
stars: 6367
stars_at: 2026-10-11
summary: 在一台或一组机器上管理完整的 Linux 系统容器和虚拟机。
tags: [系统容器, 虚拟机]
trending: yes
trending_why: LXD 在 2023 年底改成 AGPL 并加上贡献者协议后，社区用它继续以 Apache-2.0 管理完整系统。
---

## 它解决什么问题

有些工作负载要的是一整套 Linux，而不是一个只装着单个进程的应用容器。开发机要隔开的环境，小机房要几台互相独立的系统，用虚拟机又觉得太重。Incus 用同一套接口管理系统容器和虚拟机，从一台机器可以扩到一小柜服务器。

## 核心功能

- 系统容器和虚拟机。两种实例走同一套镜像、配置和生命周期。
- 镜像与配置档。常用发行版做成镜像，资源限制和设备用配置档复用。
- REST API。命令行和别的系统都通过这套接口操作，而不是只靠本机脚本。
- 多机。实例可以在集群里放置和迁移，不必每台机器各管各的。

## 通常怎么用

原来使用 LXD、又希望留在 Linux Containers 社区的人，会迁到 Incus。新的实验环境、内部云和轻量托管也会直接从它开始。应用如果只是一个容器镜像、要按副本扩缩，通常仍交给 Kubernetes 或单机的容器工具。系统镜像本身的许可，跟 Incus 这个管理器不是一回事。

## 它不负责什么

Incus 不调度无状态服务的副本，也不代替容器镜像的构建和发布。它和 Canonical 现在的 LXD 已经分叉，补丁、命令和远程协议不能默认为还能对上。集群的磁盘、网络和备份仍要单独设计。它不管你放进去的发行版是否允许你拿去对外提供服务。

## 许可与热度

Apache-2.0，由 Linux Containers 社区维护，不要求贡献者协议。2026-10-11，`lxc/incus` 有 6,367 星。同日 `canonical/lxd` 有 4,833 星，许可证是 AGPL-3.0。AGPL 仍是开源许可，但比 Apache-2.0 更要求提供对应源码，而且 Canonical 对新贡献要求签署贡献者协议。Incus 从 2023 年 10 月的首个版本起就留在 Apache-2.0，两边此后不再合并代码。
