---
name: htmx
slug: htmx
category: web
primary_repo: bigskysoftware/htmx
url: https://github.com/bigskysoftware/htmx
website: https://htmx.org/
license: 0BSD
language: JavaScript
stars: 49545
stars_at: 2026-10-10
summary: 用 HTML 属性发起请求，把服务端返回的片段换进页面的一块，而不刷新整页。
trending: yes
trending_why: 2024 年的 2.0 去掉旧浏览器包袱并把扩展移出核心，成为服务端仍返回 HTML 时对照单页框架的常用库。
tags: [HTML, 局部更新]
---

## 它解决什么问题

多页网站每次点击都整页刷新，局部更新却要在浏览器里再写一套请求和 DOM 代码。单页框架把路由和界面状态都搬进客户端。htmx 留在中间：服务端继续渲染 HTML，页面用属性声明「向这个地址发请求，把响应换到这块元素上」。交互描述写在标记里，而不是写进一个前端应用。

## 核心功能

- 在元素上声明 HTTP 方法、地址和触发条件，由库代发请求。
- 用响应正文替换指定元素或它的一部分，而不是重新加载整页。
- 表单、按钮、历史记录和定时刷新走同一套属性，浏览器地址栏仍可以跟着变。
- 响应通常是 HTML 片段。扩展可以另接 WebSocket 或服务器推送，但不是页面更新的默认路径。

## 通常怎么用

后端已经用模板输出 HTML 时，给按钮或表单加上属性，让对应的服务端路由多返回一块标记，例如表格的筛选结果或一行的编辑表单。它和现有的服务端框架放在一起，不要求先引入打包器和客户端路由。小交互可以到此为止；复杂的本地状态仍可能需要少量别的脚本。

## 它不负责什么

它不选择后端语言，也不渲染服务端模板。它不规定 JSON API 的形状；服务端若只返回数据而不返回片段，局部替换就没有材料。它不做客户端路由和应用打包，也不提供界面组件。样式、权限和数据校验仍在原来的服务端应用里。

## 许可与热度

Zero-Clause BSD，SPDX 标识是 0BSD。仓库 LICENSE 原文使用这一名称；GitHub 的 SPDX 字段是 NOASSERTION。2026-10-10，`bigskysoftware/htmx` 有 49,545 星。`htmx-org/htmx` 当时不存在。2.0 于 2024 年 6 月发布。
