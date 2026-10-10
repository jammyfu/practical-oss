---
name: Go
slug: go
category: lang
primary_repo: golang/go
url: https://github.com/golang/go
website: https://go.dev/
license: BSD-3-Clause
language: Go
stars: 139167
stars_at: 2026-10-10
summary: 以静态编译和显式并发著称的语言，大量基础设施工具用它写成单个可分发的程序。
tags: [语言, 基础设施]
---

## 它解决什么问题

写网络服务和运维工具时，人们希望编译出一个依赖很少的二进制文件，部署时不必先装一套运行时。Go 把这个目标放进语言设计：语法小、编译快、标准库自带 HTTP 和并发原语。

## 核心功能

- 编译成静态链接倾向明显的原生二进制，交叉编译直接由工具链完成。
- goroutine 和 channel。并发写在语言里，而不是靠一个外部框架。
- 完整标准库，覆盖 HTTP、JSON、加密、测试和性能剖析。
- `go mod` 管理依赖，构建结果对版本相对可复现。

## 通常怎么用

Docker 相关工具、Kubernetes、Prometheus、Grafana 的后端，以及大量 CLI，都用 Go 编写。它适合边界清楚的服务和工具。表达力要求很高的应用层业务、或者需要极细内存控制的系统内核，通常会选别的语言。

## 它不负责什么

Go 没有泛型之外的重型抽象市场可以替你组织大型领域模型，早期甚至没有泛型。错误处理是显式返回值，不是统一的异常体系。图形界面、数据科学笔记本也不是它的主场。

## 许可与热度

BSD-3-Clause。2026-10-10，`golang/go` 有 139,167 星。语言本身和用它写成的基础设施项目，是两层不同的热度，后者往往各自还有一个高星仓库。
