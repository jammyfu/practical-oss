---
name: Vue
slug: vue
category: web
primary_repo: vuejs/core
url: https://github.com/vuejs/core
website: https://vuejs.org/
license: MIT
language: TypeScript
stars: 54603
stars_at: 2026-10-10
stars_note: "统计的是当前源码仓库 vuejs/core。Vue 2 时代的 vuejs/vue 是另一个历史仓库，星标不能相加。"
summary: 用模板、响应式状态和单文件组件构建界面，可以逐步嵌进已有页面。
tags: [界面, 组件]
---

## 它解决什么问题

有的团队希望界面结构仍然看起来像 HTML，而不是全部写成 JavaScript 函数。Vue 把模板、响应式数据和组件作用域样式放在一起，既能接管整个应用，也能只增强页面上的一块区域。

## 核心功能

- 模板语法。在 HTML 上绑定数据、事件和条件渲染。
- 响应式系统。改一个状态，依赖它的界面会更新。
- 单文件组件。模板、脚本和样式放在同一个 `.vue` 文件里。
- 组合式 API。复杂逻辑可以按功能拆开，而不是全堆在一个选项对象里。

## 通常怎么用

中文互联网里的管理后台、中小团队的 Web 应用，以及需要从旧页面逐步迁移的项目，经常使用 Vue。官方路由 Vue Router 和状态库 Pinia 是常见搭配。Nuxt 则在它之上提供应用框架。当前开发看 `vuejs/core`，不要把已经进入维护状态的 Vue 2 仓库当成新项目的起点。

## 它不负责什么

核心库不包含后端、数据库和构建部署。模板看起来简单，组件之间的数据流仍然要设计。和 React 相比，全球岗位和第三方组件的数量分布不同，招人和找库时要以自己的团队为准，而不是只看某一个仓库的星标。

## 许可与热度

MIT。2026-10-10，`vuejs/core` 有 54,603 星。这个数字低于 React 的主仓库，不能单独用来判断 Vue 在实际项目里的覆盖面。
