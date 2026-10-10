---
name: Podman
slug: podman
category: infra
primary_repo: podman-container-tools/podman
url: https://github.com/podman-container-tools/podman
website: https://podman.io
license: Apache-2.0
language: Go
stars: 33023
stars_at: 2026-10-10
summary: 在本机构建和运行容器，不依赖一个常驻的 Docker 守护进程。
tags: [容器, 根用户可选]
---

## 它解决什么问题

有的环境不想为了跑容器再放一个长期以根用户运行的守护进程。Podman 用普通命令构建、拉取和运行 OCI 容器，进程模型更接近「这条命令跑完这个容器」，也可以在没有根用户的情况下运行。

## 核心功能

- 镜像和容器。构建、拉取、运行、查看日志和进入容器，命令形状和 Docker 接近。
- 无守护进程。不需要为了单次运行先启动一个中心守护进程。
- 根用户可选。普通用户可以跑容器，权限边界和传统的根守护进程不同。
- Pod。可以把几个容器放进同一个 Pod，网络和生命周期更接近 Kubernetes 里的 Pod。

## 通常怎么用

Linux 服务器、CI 和希望少一个特权守护进程的团队，会用 Podman 跑和构建容器。macOS 上通常还要配一台 Linux 虚拟机，容器仍跑在 Linux 里。集群调度继续交给 Kubernetes，Podman 负责单机。

## 它不负责什么

Podman 不编排多台机器，也不等于 Docker Desktop 那套商业桌面产品。和 Docker 命令相近，不代表每一份 Compose 文件都能原样跑起来。镜像扫描、仓库权限和集群网络都在它外面。

## 许可与热度

Apache-2.0。2026-10-10，`podman-container-tools/podman` 有 33,023 星。
