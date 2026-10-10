---
name: Docker
slug: docker
category: infra
primary_repo: moby/moby
url: https://github.com/moby/moby
website: https://www.docker.com/
license: Apache-2.0
language: Go
stars: 72163
stars_at: 2026-10-10
stars_note: "星标是容器引擎上游 moby/moby。同日 docker/compose 为 38,339。Docker Desktop 安装包是另一套产品，不随这个 Apache-2.0 仓库整包授权。"
summary: 把应用和依赖打成镜像，在本机或服务器上以容器方式重复运行。
tags: [容器, 部署]
---

## 它解决什么问题

同一份代码在开发机、测试机和生产机上会因为系统库版本不同而失败。Docker 把应用、运行时和系统依赖封进镜像。镜像跑成容器后，环境差异被收进这份镜像，而不是散落在每台机器的手工安装记录里。

## 核心功能

- 镜像构建。Dockerfile 描述从基础系统到应用启动的步骤，结果可以版本化并推到仓库。
- 容器运行。一个进程及其文件系统视图被隔离启动，端口和卷再显式映射出来。
- Compose。用一份文件描述多个容器、网络和卷，适合本地的数据库加应用组合。
- 引擎上游在 Moby。日常使用的 `docker` 命令是这套能力的接口。

## 通常怎么用

本地开发用 Compose 拉起数据库和缓存。持续集成用镜像保证构建环境一致。生产环境可能直接跑容器，也可能把镜像交给 Kubernetes。镜像只解决打包和运行边界，不自动提供编排、密钥轮换和多机调度。

## 它不负责什么

Docker Desktop 的图形安装包、部分商业订阅功能，不等于 Moby 仓库的开源范围。容器也不是虚拟机，内核仍与宿主机共享，内核级隔离要求更高时要另看方案。把密钥写进镜像层是常见错误，镜像历史里的文件删掉仍可能留在旧层里。

## 许可与热度

Moby 与 Docker Compose 都以 Apache-2.0 发布。2026-10-10，`moby/moby` 有 72,163 星。讨论「Docker 是否开源」时，要先说清楚指的是引擎、Compose，还是 Desktop。
