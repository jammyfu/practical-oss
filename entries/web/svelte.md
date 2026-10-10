---
name: Svelte
slug: svelte
category: web
primary_repo: sveltejs/svelte
url: https://github.com/sveltejs/svelte
website: https://svelte.dev/
license: MIT
language: JavaScript
stars: 88404
stars_at: 2026-10-10
summary: 把组件编译成更新 DOM 的 JavaScript，浏览器里不必再跑一套框架运行时。
tags: [界面, 编译]
---

## 它解决什么问题

React 和 Vue 在浏览器里保留一套运行时，用来比较状态和更新界面。Svelte 把组件当成一种要编译的语言：构建时知道哪个状态会影响哪一块 DOM，于是输出直接做这些更新的代码。

## 核心功能

- 单文件组件。标记、脚本和样式写在一起。
- 用普通赋值触发更新，状态不必逐个包进一套固定的调用约定。
- 编译产物小。没有使用的功能不会留在运行时里。
- SvelteKit 是官方的应用框架，负责路由、服务端渲染和项目结构。核心库本身只负责组件。

## 通常怎么用

交互页面、嵌入式小组件，以及希望少带框架代码的团队会选它。已有大量 React 或 Vue 代码的项目不必为了编译模型迁移。招人、组件库和第三方例子的数量，目前仍少于 React。

## 它不负责什么

Svelte 不包含后端和数据获取约定，那些在 SvelteKit 或其他服务里。编译模型变了，接口设计、无障碍和状态放错位置这些界面问题还在。它也不把现成的设计系统一并提供。

## 许可与热度

MIT。2026-10-10，`sveltejs/svelte` 有 88,404 星。热度已经足够把它当成主流选择，而不是实验框架。
