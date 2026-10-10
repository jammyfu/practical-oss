# 收录一条项目

这个仓库收录热度高、用处广的软件，并给每个项目写一篇独立说明。说明回答五件事：它解决什么问题，核心功能是什么，人们通常把它放在哪一步，它不负责什么，许可证现在是什么。

## 收录标准

同时满足下面三条再收录：

1. 用处广。它出现在生产环境、课程、操作系统发行版或某类工作的默认工具链里。只在一个小圈子里出名不够。
2. 能讲清功能。维护者写得出「人用它完成哪件具体的事」，而不是复述上游口号。
3. 来源可核。仓库地址、许可证、星标和统计日期写在条目开头。星标从 GitHub API 读取，不估计。

星标不是门槛。PostgreSQL 的 GitHub 镜像星标远低于许多框架，仍然应该收录。反过来，星标很高但主要是演示、课程模板或已经停更的仓库，不因为数字大就收录。

许可证改成源码可用、但不再符合开源定义的项目可以收录，正文必须写明变更和仍保持开源的分支。恶意软件、破解、未授权读取他人账号或聊天数据的工具不收录。

## 文件

在 `entries/<分类 id>/<slug>.md` 新建一篇。分类 id 以 `catalog/categories.json` 为准。新增分类时同时改这个文件，并在 README 的写法里说清这一类和其他类的边界。

条目开头使用这些字段：

```yaml
---
name: 显示名
slug: 文件名
category: cli
primary_repo: owner/name
url: https://github.com/owner/name
website: https://example.com/
license: SPDX 标识或一句准确的许可说明
language: 主要语言
stars: 12345
stars_at: 2026-10-10
summary: 一句话，说明人用它完成什么。不要用「强大、赋能、下一代」。
tags: [短标签, 另一个]
---
```

`summary` 保持一行。需要补充星标口径时，加一行 `stars_note: "..."`。

近两年才成为新默认、或关注和采用明显跃升的项目，再加两行：

```yaml
trending: yes
trending_why: 一句话说明新在哪里，不要只重复星标
```

`trending: yes` 的条目进入用途页里的「近两年的新默认」。未标的条目进入「历史最高」。日、周、月三档是 GitHub Trending 的快照，写在 `catalog/trending-windows.json`，不要用手改生成页。Git、React、PostgreSQL 这类长期默认不标 `trending`。

生成页都在英文目录里。长期默认是 `catalog/history.md`。用途页是 `catalog/categories/<分类 id>.md`。趋势页在 `catalog/trending/<抓取日>/`，抓取日来自 `captured_on`，里面有 `index.md`、`day.md`、`week.md`、`month.md`。口语稿放在 `notes/<日期>.md`，日期是这批稿子对应的统计日，脚本不改这个目录。

正文固定五节，标题不要改：

1. `## 它解决什么问题`
2. `## 核心功能`
3. `## 通常怎么用`
4. `## 它不负责什么`
5. `## 许可与热度`

用自己的话写。不粘贴上游 README，不搬教程里的命令清单，不把安装步骤写成正文主体。事实拿不准就查官方仓库或许可证文件，仍然拿不准就不要写。

## 更新目录

```bash
python3 scripts/build_index.py
```

脚本根据条目开头重建 README 目录、`catalog/history.md`、`catalog/categories/`、`catalog/trending/<抓取日>/`，以及 `catalog/index.json`。它不改 `entries/` 里的正文，也不改 `notes/`。

提交前看一遍生成结果。标了 `trending` 的项目出现在分类页的「近两年的新默认」，未标的出现在「历史最高」。日、周、月榜只随 `catalog/trending-windows.json` 变化。
