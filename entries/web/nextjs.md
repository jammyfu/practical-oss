---
name: Next.js
slug: nextjs
category: web
primary_repo: vercel/next.js
url: https://github.com/vercel/next.js
website: https://nextjs.org/
license: MIT
language: JavaScript
stars: 143097
stars_at: 2026-10-10
summary: 在 React 之外补上路由、渲染方式和全栈接口，用来交付一个完整网站。
tags: [React, 框架]
---

## 它解决什么问题

React 只负责界面。一个网站还要决定 URL 如何对应页面、哪些 HTML 在服务器上先生成、接口放在哪里，以及图片和字体怎么交付。Next.js 把这些收成一套 React 应用的默认结构。

## 核心功能

- 基于文件的路由。页面和布局放在约定目录里。
- 服务器渲染、静态生成和客户端渲染可以按页面选择。
- 服务端组件和服务器动作，用来把一部分数据获取留在服务器。
- 接口、图片和构建优化跟应用放在同一个项目里。

## 通常怎么用

新的 React 产品站、需要搜索引擎看到内容的网站，以及希望前后端在一个仓库里的团队，常从它开始。可以部署到 Vercel，也可以放到其他支持 Node 的环境。只做纯客户端管理后台时，Vite 加 React 往往更直接。

## 它不负责什么

它不替代 React，也不规定数据库和登录服务。版本之间的渲染模型变化较快，升级要看发布说明。框架能自托管，但有些配套功能和文档默认指向 Vercel 的平台，选型时要把「框架」和「托管平台」分开看。

## 许可与热度

MIT。2026-10-10，`vercel/next.js` 有 143,097 星。它是 React 应用框架里使用最广的一个。
