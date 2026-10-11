---
name: OpenBao
slug: openbao
category: infra
primary_repo: openbao/openbao
url: https://github.com/openbao/openbao
website: https://openbao.org/
license: MPL-2.0
language: Go
stars: 8378
stars_at: 2026-10-11
summary: 集中保管密钥、证书和加密能力，并作为 Vault 改许可后的开源延续。
tags: [密钥, 开源分支]
trending: yes
trending_why: 2024 年起作为 Vault 改成 Business Source License 之后的 MPL 延续，由 Linux 基金会托管。
---

## 它解决什么问题

数据库口令、云上的临时凭证和接口密钥如果散落在配置文件和聊天记录里，就很难轮换，也看不出是谁在什么时候读过。OpenBao 把这些敏感数据收进一个专门的服务：写入前加密，按租约发出，到期或出事时收回。它从 HashiCorp Vault 1.14 分出，那是改许可前的最后一版。

## 核心功能

- 静态密钥。键值在落盘前加密，拿到原始存储不等于拿到明文。
- 动态凭证。可以按需签发云账号或数据库账号，租约结束就收回。
- 加密服务。应用可以把数据交来加密或解密，密钥本身不必进业务库。
- 租约、续期和成批吊销。一个用户或一类密钥可以一起作废。

## 通常怎么用

需要开源许可、又要集中管密钥的团队，会用它接替仍停在 MPL 时代的 Vault，或直接当新的密钥服务。应用通过接口领取凭证，机器和人的登录方式分开配置。存储可以落在本机磁盘，也可以使用 PostgreSQL。解封密钥、备份和审计日志要按生产的要求单独留下。

## 它不负责什么

OpenBao 不是「把 Vault 商业版的功能逐项搬齐」。灾备复制、托管服务和企业支持仍可能只在 IBM 的付费产品里。它也不部署应用，不决定集群里哪台机器该扩容。业务系统自己的账号体系还在，它只保管这些系统要拿去用的秘密。

## 许可与热度

MPL-2.0，项目由 Linux 基金会下的社区维护。2026-10-11，`openbao/openbao` 有 8,378 星。同日 `hashicorp/vault` 有 36,381 星。Vault 仓库的许可证文件写明，1.15.0 及之后是 Business Source License，许可方是 IBM。内部自用通常允许，但做成与 IBM 付费版竞争的托管或嵌入服务会受到限制，因此不能把这一版称为开源软件。两个星标都要看，不能只留高的那一个。
