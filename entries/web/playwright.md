---
name: Playwright
slug: playwright
category: web
primary_repo: microsoft/playwright
url: https://github.com/microsoft/playwright
website: https://playwright.dev
license: Apache-2.0
language: TypeScript
stars: 97406
stars_at: 2026-10-10
summary: 用脚本驱动 Chromium、Firefox 和 WebKit，做浏览器里的端到端测试。
tags: [测试, 浏览器]
trending: yes
trending_why: 过去两年里，很多团队把浏览器端到端测试的默认工具换成了它。
---

## 它解决什么问题

页面改完只靠人点，路径一多就会漏。早期的浏览器自动化要自己管驱动和等待，脚本经常在元素还没出来时就失败。Playwright 用同一套 API 驱动 Chromium、Firefox 和 WebKit，把等待、定位和失败时的现场收进测试里。

## 核心功能

- 三种浏览器引擎。同一条脚本可以在 Chromium、Firefox 和 WebKit 上跑。
- 自动等待。点击和输入会等到元素可操作，少写固定的睡眠。
- 现场。失败时可以留下追踪、截图和录像，回头看是哪一步偏了。
- 测试运行器。自带并行、重试和报告，也可以只把它当作浏览器驱动嵌进别的框架。

## 通常怎么用

前端和全栈项目把关键路径写成 Playwright 测试：打开页面、登录、完成一次真正会改数据的操作、再核对结果。接口的单元测试和负载测试仍用别的工具。浏览器二进制由它的安装步骤准备，脚本仓库本身不含浏览器。

## 它不负责什么

Playwright 不代替接口测试，不做压力测试，也不判断视觉是不是好看。它驱动的是测试用的浏览器，不是用户已经打开的那个日常窗口。登录态、测试数据和环境地址要由项目自己准备。

## 许可与热度

Apache-2.0。2026-10-10，`microsoft/playwright` 有 97,406 星。
