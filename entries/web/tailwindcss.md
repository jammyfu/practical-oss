---
name: Tailwind CSS
slug: tailwindcss
category: web
primary_repo: tailwindlabs/tailwindcss
url: https://github.com/tailwindlabs/tailwindcss
website: https://tailwindcss.com/
license: MIT
language: TypeScript
stars: 97848
stars_at: 2026-10-10
summary: 用一组预设的样式类直接在标记里排版，而不是先发明一套组件类名。
tags: [CSS, 界面]
---

## 它解决什么问题

手写 CSS 时，类名会越来越多，同样的间距和颜色在文件之间各写一遍。组件库又常常把视觉定死。Tailwind 提供间距、颜色、排版、布局和响应式的原子类，让样式跟标记走，同时用设计令牌把取值收拢到一份配置里。

## 核心功能

- 原子类。例如用类控制外边距、栅格、字号和颜色，而不是写自定义选择器。
- 响应式和状态变体。同一元素可以按断点、悬停和焦点改样式。
- 构建时扫描源码，只输出用到的类，避免把整本工具类都送到浏览器。
- 主题配置。颜色、字体和间距可以收成项目自己的尺度。

## 通常怎么用

它出现在营销页、管理后台和组件库的底层。React、Vue 和普通 HTML 都能用。团队需要先接受「类名写在标记里」这件事。已经有成熟设计系统、并且样式必须严格集中在 CSS 文件里的项目，不一定要迁过来。

## 它不负责什么

Tailwind 不提供现成的业务组件，按钮和对话框的结构还是要自己写，或者另选组件库。它也不做布局逻辑和无障碍行为。类名变长是这种方法的代价，不是工具坏了。

## 许可与热度

MIT。2026-10-10，`tailwindlabs/tailwindcss` 有 97,848 星。官方文档和播放器之外，还要注意 Tailwind 商标和付费 UI 套件并不属于这个 MIT 仓库。
