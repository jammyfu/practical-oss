---
name: Traefik
slug: traefik
category: backend
primary_repo: traefik/traefik
url: https://github.com/traefik/traefik
website: https://traefik.io
license: MIT
language: Go
stars: 65134
stars_at: 2026-10-10
summary: 看着容器和集群里的服务变化，自动改反向代理和入口。
tags: [反向代理, Ingress]
---

## 它解决什么问题

容器一起一停，反向代理后面的地址就变了。手工改配置容易漏，也赶不上服务扩容。Traefik 从 Docker、Kubernetes 或其他编排里读服务的变化，自己更新路由、入口和证书配置。

## 核心功能

- 自动发现。服务带上约定的标签或 Ingress 对象后，路由跟着出现或消失。
- 入口和中间件。域名、路径、转发、限流和转发头放在路由上。
- 证书。可以衔接自动签发，省掉为每个新服务单独改代理文件。
- Kubernetes Ingress。在集群里它常被当作入口控制器，而不是另一套业务框架。

## 通常怎么用

Docker 主机和 Kubernetes 集群的统一入口会用 Traefik。服务用标签声明自己的域名和路径，代理跟着编排变。只有一个长期不变的站点时，静态的 Nginx 或 Caddy 配置更省事。

## 它不负责什么

Traefik 不实现业务接口，不保存会话数据，也不编排容器。发现规则写错时，它会把流量送到错误的服务，配置仍然要审。仓库里的代理是 MIT；同名的商业控制和网关产品是另一套授权，不要把商业版的功能算进这个仓库。

## 许可与热度

MIT。2026-10-10，`traefik/traefik` 有 65,134 星。
