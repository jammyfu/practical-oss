---
name: bootc
slug: bootc
category: infra
primary_repo: bootc-dev/bootc
url: https://github.com/bootc-dev/bootc
website: https://bootc.dev/
license: MIT OR Apache-2.0
language: Rust
stars: 2305
stars_at: 2026-10-11
summary: 用 OCI 容器镜像安装、启动和事务式更新整台 Linux 主机。
tags: [镜像模式, 操作系统]
trending: yes
trending_why: 2024 年起被 RHEL 镜像模式和一批原子化发行版用来启动并更新整台机器。
stars_note: "命令行仓库星标不高。镜像模式已经进了 RHEL，以及 Fedora、CentOS 这条线上的 bootc 镜像。"
---

## 它解决什么问题

一批机器如果靠逐台安装软件包来追平，时间一长就会各自漂移，出了问题也难回到同一状态。bootc 把主机系统做成容器镜像：镜像里带内核，装到磁盘上之后按这个镜像启动，更新和回滚是整份替换，而不是在每台机器上累积零散补丁。

## 核心功能

- 用容器镜像交付操作系统。构建、推送和拉取沿用已有的镜像流程。
- 安装到本机。镜像写到磁盘后，由这台机器自己的 systemd 作为一号进程启动，外面不再套一层容器运行时。
- 事务式更新和切换。可以升到新镜像，也可以换到另一份镜像引用，失败时回到上一份。
- 不绑死某一种发行版。红帽镜像模式、Fedora 和 CentOS 的 bootc 镜像，以及一批原子化桌面，都把这个客户端放进系统。

## 通常怎么用

要让边缘节点、实验室或一组服务器保持同一份系统的人，会用 Containerfile 做出自己的 bootc 镜像，再让机器跟踪这份镜像。桌面这边，Bluefin、Bazzite、Aurora 一类发行版也从 2024 年起走这条路。只想在现有系统上加一个应用容器时，不必把整台机器改成镜像模式。

## 它不负责什么

bootc 不替代 Kubernetes，也不发布你的业务容器。软件包模式的发行版安装仍然存在，镜像模式不是唯一装机办法。`/etc` 和 `/var` 仍可能在本机变化，不是镜像里的每一个字节都不能改。镜像里的发行版如果带订阅或单独许可，那个许可不因为 bootc 本身可以自由使用就消失。它也不是 rpm-ostree 的历史数据本身，老的 ostree 系统要迁移时得按发行版的路径来。

## 许可与热度

GitHub 上的 SPDX 是 NOASSERTION。仓库里的 `LICENSE` 写明可以在 MIT 和 Apache-2.0 之间任选其一，标识是 `MIT OR Apache-2.0`。项目现为 CNCF Sandbox。2026-10-11，`bootc-dev/bootc` 有 2,305 星。`containers/bootc` 指向同一仓库。这个数字低于它已经进入的发行版使用面，不能用星标判断镜像模式是否只是实验。
