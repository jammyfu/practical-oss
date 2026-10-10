---
name: Syncthing
slug: syncthing
category: selfhost
primary_repo: syncthing/syncthing
url: https://github.com/syncthing/syncthing
website: https://syncthing.net/
license: MPL-2.0
language: Go
stars: 89264
stars_at: 2026-10-10
summary: 在自己的几台设备之间连续同步文件夹，不经过别人的网盘。
tags: [同步, 设备]
---

## 它解决什么问题

把文件夹交给网盘，文件要先上别人的服务器，再从另一台设备拉下来。Syncthing 让你自己的电脑、手机和服务器互相认设备，文件夹直接在这些设备之间同步。没有必须经过的中心账号。

## 核心功能

- 设备互信。每台设备有自己的 ID，两边都同意之后才同步。
- 文件夹。选定目录持续同步，改动传到其他在线设备。
- 发现和穿透。设备不在同一网络时，可以用发现和中继帮它们连上，数据仍在你的设备之间传。
- 版本。可以保留若干旧版本，用来应付误删，保留策略要自己设。

## 通常怎么用

个人或小团队在几台自己的机器上同步文档、照片目录或配置，而不把这份数据放进公共网盘。每台设备都要安装并保持偶尔在线。需要对外分享链接、在线办公和账号体系时，用 Nextcloud 那一类产品。

## 它不负责什么

Syncthing 不是备份。两边同时改同一个文件会产生冲突副本，它不替你合并内容。一台设备损坏时，只有其他设备上已经同步到的数据还在。它也不提供给陌生人用的公开链接。

## 许可与热度

MPL-2.0。2026-10-10，`syncthing/syncthing` 有 89,264 星。
