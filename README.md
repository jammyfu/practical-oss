# 实用开源项目志

按用途收集热度高、真正被广泛使用的开源软件。每一篇都单独说明：它解决什么问题、核心功能、通常放在工作流的哪一步、边界在哪里、许可证现在怎么算。

这不是星标排行榜。星标只作为热度旁证，统计日写在每篇开头。行业默认、但 GitHub 镜像星标不高的项目，例如 PostgreSQL，照样收录。许可证已经离开开源定义的著名项目也会收录，并写明替代分支，避免把「仓库还能看到源码」误写成「仍然是开源软件」。

## 怎么读

目录最前面是「最新最热」。这是横切分类：项目仍按用途归档，只是额外标成近两年的新默认或热度跃升。下面再按功能分类阅读。页内五节的顺序固定，方便对比两个同类项目。

机器可读目录在 [`catalog/index.json`](catalog/index.json)。分类定义在 [`catalog/categories.json`](catalog/categories.json)。新增一篇的规则在 [CONTRIBUTING.md](CONTRIBUTING.md)。想按短视频口播来讲这些项目能做成什么，看 [`口播/最新最热.md`](口播/最新最热.md)。

本仓库的文字使用 [CC BY 4.0](LICENSE)。项目名称和上游代码仍属于各自的所有者，许可以各篇正文为准。

<!-- catalog:start -->

## 最新最热

这一节是横切分类，不代替功能分类。条目仍放在原来的用途目录里，并额外标 `trending: yes`。
进入标准是大约 2024 年以来成为某类工作的新默认，或关注和实际采用明显跃升。Git、React、PostgreSQL 这类长期默认不因为总星标进入这里。

| 项目 | 新在哪里 | 功能分类 | 许可 | 星标 |
| --- | --- | --- | --- | ---: |
| [n8n](entries/selfhost/n8n.md) | 要把 SaaS、内部接口和模型调用接成一条自动化时，它是目前最常被拿来自托管的可视化产品。 | 自托管应用 | Sustainable Use License | 206,845 |
| [Ollama](entries/ai/ollama.md) | 2023 年后成为在自己电脑上运行大模型的默认命令。 | 人工智能 | MIT | 182,543 |
| [Dify](entries/ai/dify.md) | 团队要把知识库和工作流做成可上线的模型应用时，常把它当作自托管搭建台，但许可不是 Apache-2.0。 | 人工智能 | 修改版 Apache-2.0（含多租户与品牌附加条款，非 OSI） | 158,031 |
| [Open WebUI](entries/selfhost/open-webui.md) | 给 Ollama 或兼容接口补一个可登录的聊天入口时，它是目前被广泛部署的界面，但现行许可已不是 MIT。 | 自托管应用 | Open WebUI License（源码可用，非 OSI） | 154,158 |
| [ComfyUI](entries/ai/comfyui.md) | 本地图像生成从写死的脚本变成可保存的节点工作流之后，它成了这条路径上的常见界面。 | 人工智能 | GPL-3.0 | 136,649 |
| [llama.cpp](entries/ai/llama-cpp.md) | 让量化后的大模型在普通 CPU 和 GPU 上运行，是这轮本地推理的基础实现。 | 人工智能 | MIT | 130,658 |
| [Immich](entries/selfhost/immich.md) | 这两年自建相册时最常被拿来替代厂商云相册的产品。 | 自托管应用 | AGPL-3.0 | 115,876 |
| [Bun](entries/lang/bun.md) | 把运行时、打包、测试和包管理放进同一个程序，作为 Node 工具链之外的新入口。 | 语言与运行时 | MIT（Bun 本体）；发行二进制静态链接 LGPL-2 的 JavaScriptCore | 96,170 |
| [vLLM](entries/ai/vllm.md) | 自建大模型服务时，它把吞吐和显存利用率做成了可部署的推理引擎，而不只是一次对话脚本。 | 人工智能 | Apache-2.0 | 93,470 |
| [Zed](entries/editor/zed.md) | 2024 年开源后，多人协作做进编辑器本身，而不是在网页壳上再装一个协作插件。 | 编辑器 | GPL-3.0-or-later（标明的组件为 Apache-2.0） | 91,509 |
| [Home Assistant](entries/selfhost/home-assistant.md) | 厂商云各自为政之后，本地优先的家庭自动化几乎都围绕它来接设备和场景。 | 自托管应用 | Apache-2.0 | 91,344 |
| [uv](entries/lang/uv.md) | 把装包、虚拟环境和 Python 版本收进同一个程序，正在取代 pip 加 venv 的旧默认。 | 语言与运行时 | Apache-2.0 OR MIT | 90,557 |
| [Astro](entries/web/astro.md) | 2024 年的 5.0 补上内容层和服务端岛屿，静态页里可以只把需要个性化的那一块交给服务器。 | 界面与前端 | MIT | 63,141 |
| [Ghostty](entries/cli/ghostty.md) | 2024 年末以 1.0 公开，在 macOS 和 Linux 上提供新的原生 GPU 终端窗口，换的不是 shell。 | 命令行与版本控制 | MIT | 62,010 |
| [PocketBase](entries/selfhost/pocketbase.md) | 小产品不想自建一整套后端时，单文件加 SQLite 成了托管 BaaS 之外的常见选择。 | 自托管应用 | MIT | 61,338 |
| [Jellyfin](entries/media/jellyfin.md) | 不想把片库和观看记录交给厂商账号时，它是最常被拿来自建的自由软件媒体服务器。 | 创作 | GPL-2.0 | 57,951 |
| [ClickHouse](entries/data/clickhouse.md) | 日志和事件分析从行式库迁出时，它是生产里被选得最多的开源列式库之一。 | 数据存储与分析 | Apache-2.0 | 50,318 |
| [Ruff](entries/cli/ruff.md) | 同一个 Rust 程序同时做 lint 和格式化，用来换掉 Flake8、isort 和 Black 的组合。 | 命令行与版本控制 | MIT | 49,971 |
| [htmx](entries/web/htmx.md) | 2024 年的 2.0 去掉旧浏览器包袱并把扩展移出核心，成为服务端仍返回 HTML 时对照单页框架的常用库。 | 界面与前端 | 0BSD | 49,545 |
| [DuckDB](entries/data/duckdb.md) | 本地用 SQL 分析 CSV 和 Parquet 时，成为 SQLite 之外的新默认。 | 数据存储与分析 | MIT | 42,053 |
| [Polars](entries/data/polars.md) | 本地和管道里处理中等规模表格时，它已成为相对 pandas 的新默认对比。 | 数据存储与分析 | MIT | 40,080 |
| [Biome](entries/web/biome.md) | 格式化和 lint 合成一个工具，减少前端项目同时维护 Prettier 和 ESLint 的做法。 | 界面与前端 | Apache-2.0 OR MIT | 25,915 |

## 命令行与版本控制

每天会打开的本地工具：找文件、搜代码、看 diff、管会话。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [bat](entries/cli/bat.md) | 在终端里分页查看文件，带行号和按语言着色的语法高亮。 | Apache-2.0 | 60,747 |
| [fd](entries/cli/fd.md) | 按名字找文件，默认跳过 Git 忽略的目录，并用颜色标出匹配的路径。 | Apache-2.0 | 44,736 |
| [fzf](entries/cli/fzf.md) | 对任意一行文本做模糊筛选，用来挑文件、历史命令、分支和提交。 | MIT | 83,509 |
| [Ghostty](entries/cli/ghostty.md) | 用 GPU 绘制终端网格的模拟器，窗口里跑的仍是原来的 shell。 | MIT | 62,010 |
| [Git](entries/cli/git.md) | 记录文件历史、分支和合并，让多人可以在同一份代码上分开工作再合回来。 | GPL-2.0 | 63,766（见正文） |
| [jq](entries/cli/jq.md) | 用一条表达式从 JSON 里取出、过滤和重写字段，结果仍是可继续管道处理的数据。 | MIT | 35,774（见正文） |
| [lazygit](entries/cli/lazygit.md) | 在终端里用面板完成暂存、提交、分支、变基和解决冲突。 | MIT | 83,061 |
| [ripgrep](entries/cli/ripgrep.md) | 在目录树里按正则搜索文本，并默认跳过 Git 忽略的文件。 | Unlicense | 68,980 |
| [Ruff](entries/cli/ruff.md) | 用一个程序检查并格式化 Python，覆盖原来要靠多件 lint 工具才做的事。 | MIT | 49,971 |
| [tmux](entries/cli/tmux.md) | 在一个终端连接里切开多个窗口和窗格，断线后会话还留在服务器上。 | ISC | 49,868 |

## 编辑器

写代码和改配置时真正待着的环境。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Neovim](entries/editor/neovim.md) | 在 Vim 的编辑模型上重建可扩展性，用 Lua 配置，并把界面和编辑核心拆开。 | Apache-2.0 | 102,956 |
| [Visual Studio Code](entries/editor/vscode.md) | 带扩展市场的桌面代码编辑器，把编辑、调试、终端和远程开发放在一个窗口里。 | MIT | 193,498 |
| [Zed](entries/editor/zed.md) | 用原生界面写代码，并在同一编辑器里和别人实时改同一块缓冲区。 | GPL-3.0-or-later（标明的组件为 Apache-2.0） | 91,509 |

## 语言与运行时

大量软件直接跑在这些语言之上，选型时先看运行时，再看框架。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Bun](entries/lang/bun.md) | 运行、打包并测试 JavaScript，同时管理依赖，少装一整套分开的工具。 | MIT（Bun 本体）；发行二进制静态链接 LGPL-2 的 JavaScriptCore | 96,170 |
| [CPython](entries/lang/cpython.md) | Python 语言最常用的解释器，脚本、数据分析和大量后端服务都跑在它上面。 | PSF-2.0 | 77,602 |
| [Go](entries/lang/go.md) | 以静态编译和显式并发著称的语言，大量基础设施工具用它写成单个可分发的程序。 | BSD-3-Clause | 139,167 |
| [Node.js](entries/lang/node.md) | 在服务器和命令行里运行 JavaScript，并让前端工具链有一个统一的运行时。 | MIT | 122,261 |
| [Rust](entries/lang/rust.md) | 在编译期约束内存所有权，用来写既要性能、又要避免一整类内存错误的程序。 | MIT OR Apache-2.0 | 119,613 |
| [TypeScript](entries/lang/typescript.md) | 在 JavaScript 上增加可擦除的类型，让编辑器和编译器在运行前指出一类错误。 | Apache-2.0 | 111,371（见正文） |
| [uv](entries/lang/uv.md) | 用一个工具安装 Python 包、管理虚拟环境，并安装要用的 Python 版本。 | Apache-2.0 OR MIT | 90,557 |

## 界面与前端

做网页界面时最常见的库、框架和构建工具。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Astro](entries/web/astro.md) | 为文档、博客和营销站默认生成静态 HTML，只在交互组件上加载脚本。 | MIT | 63,141 |
| [Biome](entries/web/biome.md) | 用同一个工具格式化并检查 JavaScript 和 TypeScript，命令行和编辑器都能调用。 | Apache-2.0 OR MIT | 25,915 |
| [htmx](entries/web/htmx.md) | 用 HTML 属性发起请求，把服务端返回的片段换进页面的一块，而不刷新整页。 | 0BSD | 49,545 |
| [Next.js](entries/web/nextjs.md) | 在 React 之外补上路由、渲染方式和全栈接口，用来交付一个完整网站。 | MIT | 143,097 |
| [React](entries/web/react.md) | 用可组合的组件描述界面，数据变化时由库决定哪些部分需要重新渲染。 | MIT | 250,801 |
| [Svelte](entries/web/svelte.md) | 把组件编译成更新 DOM 的 JavaScript，浏览器里不必再跑一套框架运行时。 | MIT | 88,404 |
| [Tailwind CSS](entries/web/tailwindcss.md) | 用一组预设的样式类直接在标记里排版，而不是先发明一套组件类名。 | MIT | 97,848 |
| [Vite](entries/web/vite.md) | 开发时用浏览器原生模块快速启动，生产构建再交给打包器收成静态文件。 | MIT | 83,265 |
| [Vue](entries/web/vue.md) | 用模板、响应式状态和单文件组件构建界面，可以逐步嵌进已有页面。 | MIT | 54,603（见正文） |

## 服务与接入

对外提供 HTTP 接口，或把请求转给后面的应用。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Caddy](entries/backend/caddy.md) | 用简短配置提供网站和反向代理，并默认申请和续期 HTTPS 证书。 | Apache-2.0 | 77,648 |
| [Django](entries/backend/django.md) | 带数据模型、管理后台、表单和安全默认值的 Python Web 框架。 | BSD-3-Clause | 91,357 |
| [FastAPI](entries/backend/fastapi.md) | 用 Python 类型声明描述 HTTP 接口，并自动给出校验和可交互的接口文档。 | MIT | 102,954 |
| [Gin](entries/backend/gin.md) | 用很少的封装在 Go 里写 HTTP 路由、参数绑定和中间件。 | MIT | 89,305 |
| [nginx](entries/backend/nginx.md) | 用事件驱动处理大量连接，做网站静态文件、反向代理和负载均衡。 | BSD-2-Clause | 31,832 |
| [Spring Boot](entries/backend/spring-boot.md) | 用约定和起步依赖把 Spring 应用装成可运行的 Java 服务。 | Apache-2.0 | 81,581 |

## 数据存储与分析

事务、缓存和分析查询。热度不等于还是 OSI 开源，许可变更单独写明。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Apache Kafka](entries/data/kafka.md) | 用可保留的日志接收事件，让多个系统按自己的速度读取同一份流。 | Apache-2.0 | 33,921 |
| [ClickHouse](entries/data/clickhouse.md) | 面向扫描和聚合的列式分析数据库，用来做日志、指标和实时报表。 | Apache-2.0 | 50,318 |
| [DuckDB](entries/data/duckdb.md) | 嵌在进程里的分析型数据库，直接对本地文件和表格数据跑 SQL。 | MIT | 42,053 |
| [JupyterLab](entries/data/jupyterlab.md) | 在浏览器里把代码、图表和说明放进同一本可反复运行的笔记本。 | BSD-3-Clause | 15,347（见正文） |
| [Polars](entries/data/polars.md) | 用列式查询引擎在进程内变换和聚合表格，常用来替代逐行的 DataFrame 写法。 | MIT | 40,080 |
| [PostgreSQL](entries/data/postgresql.md) | 用事务保存业务数据，并用 SQL 同时完成约束、查询和不少分析。 | PostgreSQL | 22,323（见正文） |
| [Redis](entries/data/redis.md) | 把键值、集合和过期时间放在内存里，用来做缓存、计数、队列和短期状态。 | RSALv2 OR SSPL-1.0 | 76,678 |
| [SQLite](entries/data/sqlite.md) | 把一个完整的 SQL 数据库放进单个库文件，由应用进程直接读写。 | Public Domain | 10,628（见正文） |
| [Valkey](entries/data/valkey.md) | 在 Redis 改许可之前的代码上继续开发的内存数据结构服务。 | BSD-3-Clause | 27,391 |

## 运行与基础设施

把应用送到机器上，并声明机器、网络和集群长什么样。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Ansible](entries/infra/ansible.md) | 用 SSH 和任务清单把多台机器配成声明的样子，目标机器上不必先装代理。 | GPL-3.0 | 70,948 |
| [Docker](entries/infra/docker.md) | 把应用和依赖打成镜像，在本机或服务器上以容器方式重复运行。 | Apache-2.0 | 72,163（见正文） |
| [Helm](entries/infra/helm.md) | 把一组 Kubernetes 资源配置打包成可版本化、可按环境改参数的图表。 | Apache-2.0 | 30,306 |
| [Kubernetes](entries/infra/kubernetes.md) | 在多台机器上声明容器要跑几份、如何发现彼此，以及失败后如何拉回来。 | Apache-2.0 | 128,239 |
| [OpenTofu](entries/infra/opentofu.md) | 用声明式配置创建和变更云上资源，并作为 Terraform 改许可后的开源延续。 | MPL-2.0 | 30,440 |

## 观测与安全

服务跑起来之后，看指标、看图、查已知漏洞。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Grafana](entries/observe/grafana.md) | 把指标、日志和追踪查询画成仪表板，并挂上告警。 | AGPL-3.0 | 77,209 |
| [Prometheus](entries/observe/prometheus.md) | 定时拉取指标并保存在时序库里，用 PromQL 查询服务是否偏离正常范围。 | Apache-2.0 | 66,456 |
| [Trivy](entries/observe/trivy.md) | 扫描容器镜像、文件系统和配置，找出已知漏洞、密钥和错误配置。 | Apache-2.0 | 38,314 |

## 人工智能

在自己的机器或集群上加载、运行和微调模型。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [ComfyUI](entries/ai/comfyui.md) | 用节点图编排扩散模型的加载、采样和后处理，在本地生成图像等内容。 | GPL-3.0 | 136,649 |
| [Dify](entries/ai/dify.md) | 用可视化工作流、知识库和模型接入，把大模型做成可调用的应用。 | 修改版 Apache-2.0（含多租户与品牌附加条款，非 OSI） | 158,031 |
| [llama.cpp](entries/ai/llama-cpp.md) | 用纯 C/C++ 在本机 CPU 和 GPU 上运行量化后的大语言模型。 | MIT | 130,658 |
| [Ollama](entries/ai/ollama.md) | 用一条命令下载并运行本地大模型，再通过本机接口供其他程序调用。 | MIT | 182,543 |
| [PyTorch](entries/ai/pytorch.md) | 用 Python 写张量计算和神经网络，研究训练和模型实现大多从这里开始。 | BSD-3-Clause | 104,007（见正文） |
| [Transformers](entries/ai/transformers.md) | 用同一套 Python 接口加载、训练和运行大量文本、图像和语音模型。 | Apache-2.0 | 166,948 |
| [vLLM](entries/ai/vllm.md) | 在 GPU 上高吞吐地服务大语言模型，并对外提供可接入的推理接口。 | Apache-2.0 | 93,470 |

## 自托管应用

装在自己服务器上、给人或家庭直接用的完整产品。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Home Assistant](entries/selfhost/home-assistant.md) | 在自己的机器上把灯、传感器和开关接成可本地运行的家庭自动化。 | Apache-2.0 | 91,344 |
| [Immich](entries/selfhost/immich.md) | 自建照片和视频库，在手机上备份，在浏览器里按时间线、人物和地点浏览。 | AGPL-3.0 | 115,876 |
| [n8n](entries/selfhost/n8n.md) | 用可视化节点把接口、定时任务和常见应用串成可自托管的工作流。 | Sustainable Use License | 206,845 |
| [Nextcloud](entries/selfhost/nextcloud.md) | 自建文件同步、日历、联系人和协作入口，用来替代一整套厂商云办公套件。 | AGPL-3.0 | 37,047 |
| [Open WebUI](entries/selfhost/open-webui.md) | 自托管的网页聊天界面，用来连接本地或远程的模型接口。 | Open WebUI License（源码可用，非 OSI） | 154,158 |
| [Paperless-ngx](entries/selfhost/paperless-ngx.md) | 把扫描件收成可搜索的文档库，用标签、通信方和日期代替一叠文件夹。 | GPL-3.0 | 46,447 |
| [PocketBase](entries/selfhost/pocketbase.md) | 一个可执行文件里带上数据库、用户鉴权和文件接口，给小应用当后端。 | MIT | 61,338 |

## 创作

制作图像、三维和动画的专业工具。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Blender](entries/media/blender.md) | 在一个程序里完成三维建模、雕刻、绑定、动画、材质、渲染和视频剪辑。 | GPL-2.0-or-later | 20,791（见正文） |
| [GIMP](entries/media/gimp.md) | 用图层、选区和画笔编辑照片与位图，覆盖修图、合成和格式转换。 | GPL-3.0-or-later | 6,497（见正文） |
| [Jellyfin](entries/media/jellyfin.md) | 把自己的电影、剧集和音乐整理成可在浏览器和电视上播放的媒体服务。 | GPL-2.0 | 57,951 |
| [OBS Studio](entries/media/obs-studio.md) | 把摄像头、窗口和屏幕组合成一个画面，用来直播或录成视频。 | GPL-2.0 | 77,210 |

星标取自 GitHub API，统计日见各条目的 `stars_at`。星标只说明仓库被关注的程度，不代替采用率。PostgreSQL 这类镜像仓库星标偏低，仍然是行业默认选择。
<!-- catalog:end -->
