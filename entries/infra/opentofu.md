---
name: OpenTofu
slug: opentofu
category: infra
primary_repo: opentofu/opentofu
url: https://github.com/opentofu/opentofu
website: https://opentofu.org/
license: MPL-2.0
language: Go
stars: 30440
stars_at: 2026-10-10
summary: 用声明式配置创建和变更云上资源，并作为 Terraform 改许可后的开源延续。
tags: [基础设施即代码, 开源分支]
---

## 它解决什么问题

云上的网络、数据库和权限如果只在网页控制台里点，就无法审查、无法复现，也难以看出这次改动会影响什么。Terraform 用配置文件描述这些资源，再用计划预览差异。HashiCorp 在 2023 年把 Terraform 1.6 及之后的版本改成 Business Source License 之后，OpenTofu 在 Linux 基金会下继续维护开源分支。

## 核心功能

- 声明式配置。描述期望的资源，而不是写一串不可逆的创建脚本。
- 执行计划。应用前先列出要新增、修改和销毁的对象。
- 状态文件记录真实资源与配置的对应关系。
- 提供者和模块机制。不同云和 SaaS 的 API 由提供者接入。

## 通常怎么用

已有 Terraform 配置、又要求工具链保持 MPL 开源许可的团队，会评估后迁到 OpenTofu。新项目如果把许可证作为硬性条件，也会直接从它开始。状态里存着资源标识和可能的敏感输出，远程状态和锁定仍然必须单独安排。

## 它不负责什么

OpenTofu 不自动等于「所有 Terraform 商业功能和后来的专有变更」。提供者版本、状态锁和敏感变量的处理要按自己的云环境验证。它也不部署容器里的应用版本，那一层常常仍由 Kubernetes 或发布系统负责。BSL 许可的 Terraform 仍然广泛使用，但不能把它 1.6 之后的版本写成开源软件。

## 许可与热度

MPL-2.0。2026-10-10，`opentofu/opentofu` 有 30,440 星。同日 `hashicorp/terraform` 有 49,844 星，但那个仓库当前许可证不是 OSI 开源许可。两个数字都要看，不能只留高的那一个。
