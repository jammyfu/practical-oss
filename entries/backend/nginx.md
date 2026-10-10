---
name: nginx
slug: nginx
category: backend
primary_repo: nginx/nginx
url: https://github.com/nginx/nginx
website: https://nginx.org/
license: BSD-2-Clause
language: C
stars: 31832
stars_at: 2026-10-10
summary: 用事件驱动处理大量连接，做网站静态文件、反向代理和负载均衡。
tags: [代理, Web 服务器]
---

## 它解决什么问题

应用服务器擅长业务逻辑，不擅长同时接待大量慢连接、提供静态文件，或按路径把流量分给多个后端。nginx 站在外面：接收连接、终止 TLS、按规则转发，并把静态资源直接送出。

## 核心功能

- 静态文件服务和缓存相关的基础能力。
- 反向代理。按域名和路径把请求转到上游应用。
- 负载均衡。在多个上游之间分配连接，并做基本的健康判断。
- TLS 终结、压缩、限速和访问控制等网关层配置。

## 通常怎么用

一台机器上跑几个应用时，nginx 监听 80 和 443，再按域名转发。它也放在 Kubernetes Ingress 或传统虚拟机架构的最外层。配置是声明式的文本文件。非常动态的服务发现和细粒度流量策略，有时会改用专门的服务网格或 API 网关。

## 它不负责什么

nginx 不写业务，不保存用户会话的应用状态，也不替上游修复慢查询。开源版 nginx 和商业版 NGINX Plus 的功能范围不同，动态 API 和服务网格集成不要默认算进开源版。

## 许可与热度

BSD-2-Clause。2026-10-10，`nginx/nginx` 有 31,832 星。它在实际网站前的部署量远高于这个星标，很多系统把它当作默认的 Web 入口。
