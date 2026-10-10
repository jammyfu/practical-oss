---
name: Caddy
slug: caddy
category: backend
primary_repo: caddyserver/caddy
url: https://github.com/caddyserver/caddy
website: https://caddyserver.com/
license: Apache-2.0
language: Go
stars: 77648
stars_at: 2026-10-10
summary: 用简短配置提供网站和反向代理，并默认申请和续期 HTTPS 证书。
tags: [代理, HTTPS]
---

## 它解决什么问题

把一个服务暴露到公网时，证书申请、续期和基本的反向代理经常比应用本身还容易配错。Caddy 把 HTTPS 当成默认值：写明域名和上游，证书流程由服务器完成。

## 核心功能

- 静态站点、反向代理和负载均衡。
- 自动申请和续期证书，常用的是 ACME 协议。
- Caddyfile 用较少的行描述站点。需要精细控制时可以改用 JSON 配置。
- 模块可以扩展认证、缓存和不同的匹配规则。

## 通常怎么用

个人项目、小团队的公网服务，以及希望少维护证书脚本的部署，会把它放在应用前面。流量规则、路径改写和多上游已经很复杂的现有系统，往往继续使用 nginx，而不是为了证书功能迁移。

## 它不负责什么

它不编写业务接口，也不保存应用数据。自动证书要求机器能够被证书机构访问到验证域名，内网或特殊网络里这条默认路径会走不通。商业功能和托管服务不要算进这个 Apache-2.0 仓库。

## 许可与热度

Apache-2.0。2026-10-10，`caddyserver/caddy` 有 77,648 星。它和 nginx 解决的是同一层问题，差别主要在默认 HTTPS 和配置方式。
