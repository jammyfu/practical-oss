# 实用开源项目志

按用途收集热度高、真正被广泛使用的开源软件。每一篇都单独说明：它解决什么问题、核心功能、通常放在工作流的哪一步、边界在哪里、许可证现在怎么算。

这不是星标排行榜。星标只作为热度旁证，统计日写在每篇开头。行业默认、但 GitHub 镜像星标不高的项目，例如 PostgreSQL，照样收录。许可证已经离开开源定义的著名项目也会收录，并写明替代分支，避免把「仓库还能看到源码」误写成「仍然是开源软件」。

## 怎么读

主文件只做目录。热度拆成两处：[历史最高](catalog/history.md) 是长期默认，[当前热度最高](catalog/trending/2026-10-10/index.md) 按日、周、月看趋势，文件夹名是抓取日。用途分类在 `catalog/categories/`，每种一页。项目说明仍在 `entries/`，五节顺序固定。

机器可读目录在 [`catalog/index.json`](catalog/index.json)。分类定义在 [`catalog/categories.json`](catalog/categories.json)。新增一篇的规则在 [CONTRIBUTING.md](CONTRIBUTING.md)。想用口语把项目讲清楚，看 [`notes/2026-10-10.md`](notes/2026-10-10.md)。

本仓库的文字使用 [CC BY 4.0](LICENSE)。项目名称和上游代码仍属于各自的所有者，许可以各篇正文为准。

<!-- catalog:start -->

## 热度

历史最高是长期默认。当前热度最高按日、周、月看 GitHub 趋势，不跟总星标混在一张表里。趋势页的目录名是抓取日。

| 名单 | 怎么分 | 篇数 |
| --- | --- | ---: |
| [历史最高](catalog/history.md) | 长期默认，按总星标 | 61 |
| [当前热度最高](catalog/trending/2026-10-10/index.md) | 日、周、月三档趋势，抓取日 2026-10-10 | 见该页 |

## 用途

每类一页，放在 `catalog/categories/`。页内分成近两年的新默认，和历史最高。

| 分类 | 这一类是什么 | 历史 | 近两年 |
| --- | --- | ---: | ---: |
| [命令行与版本控制](catalog/categories/cli.md) | 每天会打开的本地工具：找文件、搜代码、看 diff、管会话。 | 11 | 2 |
| [编辑器](catalog/categories/editor.md) | 写代码和改配置时真正待着的环境。 | 2 | 1 |
| [语言与运行时](catalog/categories/lang.md) | 大量软件直接跑在这些语言之上，选型时先看运行时，再看框架。 | 5 | 2 |
| [界面与前端](catalog/categories/web.md) | 做网页界面时最常见的库、框架和构建工具。 | 6 | 4 |
| [服务与接入](catalog/categories/backend.md) | 对外提供 HTTP 接口，或把请求转给后面的应用。 | 9 | 1 |
| [数据存储与分析](catalog/categories/data.md) | 事务、缓存和分析查询。热度不等于还是 OSI 开源，许可变更单独写明。 | 8 | 3 |
| [运行与基础设施](catalog/categories/infra.md) | 把应用送到机器上，并声明机器、网络和集群长什么样。 | 8 | 0 |
| [观测与安全](catalog/categories/observe.md) | 服务跑起来之后，看指标、看图、查已知漏洞。 | 4 | 2 |
| [人工智能](catalog/categories/ai.md) | 在自己的机器或集群上加载、运行和微调模型。 | 2 | 5 |
| [自托管应用](catalog/categories/selfhost.md) | 装在自己服务器上、给人或家庭直接用的完整产品。 | 3 | 5 |
| [创作](catalog/categories/media.md) | 制作图像、三维和动画的专业工具。 | 3 | 1 |
<!-- catalog:end -->
