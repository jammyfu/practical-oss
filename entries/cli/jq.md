---
name: jq
slug: jq
category: cli
primary_repo: jqlang/jq
url: https://github.com/jqlang/jq
website: https://jqlang.org/
license: MIT
language: C
stars: 35774
stars_at: 2026-10-10
stars_note: "GitHub 未标出 SPDX 标识。仓库 COPYING 是 MIT 许可文本。"
summary: 用一条表达式从 JSON 里取出、过滤和重写字段，结果仍是可继续管道处理的数据。
tags: [JSON, 命令行]
---

## 它解决什么问题

接口和日志越来越多地使用 JSON。用文本搜索可以找到一行，但取不出嵌套字段，也做不了「只要状态是失败的对象」。jq 把 JSON 当成数据，而不是当成一堆字符。

## 核心功能

- 选择字段、数组元素和嵌套路径。
- 按条件过滤，并映射成新的对象或数组。
- 做简单的计算、分组和字符串处理。
- 流式读入。大文件不必先在编辑器里打开。

## 通常怎么用

调试 API 时，curl 的输出直接接给 jq，只留下需要的字段。脚本里用它把一份配置改成另一份，而不必写一段完整的程序。它也是很多运维命令默认假设你会用的 JSON 工具。

## 它不负责什么

它不发 HTTP 请求，也不保存查询结果。表达式是它自己的语言，复杂转换写长了会难维护，那种情况更适合一段 Python 或专门的数据管道。它处理的是 JSON，不是 YAML 或任意日志格式；那些格式通常先转换再交给它。

## 许可与热度

COPYING 文件使用 MIT 许可。2026-10-10，`jqlang/jq` 有 35,774 星。命令行处理 JSON 时，它仍是最常被写进脚本的工具。
