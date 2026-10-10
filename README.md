# 实用开源项目志

按用途收集热度高、真正被广泛使用的开源软件。每一篇都单独说明：它解决什么问题、核心功能、通常放在工作流的哪一步、边界在哪里、许可证现在怎么算。

这不是星标排行榜。星标只作为热度旁证，统计日写在每篇开头。行业默认、但 GitHub 镜像星标不高的项目，例如 PostgreSQL，照样收录。许可证已经离开开源定义的著名项目也会收录，并写明替代分支，避免把「仓库还能看到源码」误写成「仍然是开源软件」。

## 怎么读

先看下面的分类表，选一个和你手头工作接近的类，再打开项目页。页内五节的顺序固定，方便对比两个同类项目。

机器可读目录在 [`catalog/index.json`](catalog/index.json)。分类定义在 [`catalog/categories.json`](catalog/categories.json)。新增一篇的规则在 [CONTRIBUTING.md](CONTRIBUTING.md)。

本仓库的文字使用 [CC BY 4.0](LICENSE)。项目名称和上游代码仍属于各自的所有者，许可以各篇正文为准。

<!-- catalog:start -->

## 命令行与版本控制

每天会打开的本地工具：找文件、搜代码、看 diff、管会话。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [bat](entries/cli/bat.md) | 在终端里分页查看文件，带行号和按语言着色的语法高亮。 | Apache-2.0 | 60,747 |
| [fd](entries/cli/fd.md) | 按名字找文件，默认跳过 Git 忽略的目录，并用颜色标出匹配的路径。 | Apache-2.0 | 44,736 |
| [fzf](entries/cli/fzf.md) | 对任意一行文本做模糊筛选，用来挑文件、历史命令、分支和提交。 | MIT | 83,509 |
| [Git](entries/cli/git.md) | 记录文件历史、分支和合并，让多人可以在同一份代码上分开工作再合回来。 | GPL-2.0 | 63,766（见正文） |
| [jq](entries/cli/jq.md) | 用一条表达式从 JSON 里取出、过滤和重写字段，结果仍是可继续管道处理的数据。 | MIT | 35,774（见正文） |
| [lazygit](entries/cli/lazygit.md) | 在终端里用面板完成暂存、提交、分支、变基和解决冲突。 | MIT | 83,061 |
| [ripgrep](entries/cli/ripgrep.md) | 在目录树里按正则搜索文本，并默认跳过 Git 忽略的文件。 | Unlicense | 68,980 |
| [tmux](entries/cli/tmux.md) | 在一个终端连接里切开多个窗口和窗格，断线后会话还留在服务器上。 | ISC | 49,868 |

## 编辑器

写代码和改配置时真正待着的环境。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Neovim](entries/editor/neovim.md) | 在 Vim 的编辑模型上重建可扩展性，用 Lua 配置，并把界面和编辑核心拆开。 | Apache-2.0 | 102,956 |
| [Visual Studio Code](entries/editor/vscode.md) | 带扩展市场的桌面代码编辑器，把编辑、调试、终端和远程开发放在一个窗口里。 | MIT | 193,498 |

## 语言与运行时

大量软件直接跑在这些语言之上，选型时先看运行时，再看框架。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [CPython](entries/lang/cpython.md) | Python 语言最常用的解释器，脚本、数据分析和大量后端服务都跑在它上面。 | PSF-2.0 | 77,602 |
| [Go](entries/lang/go.md) | 以静态编译和显式并发著称的语言，大量基础设施工具用它写成单个可分发的程序。 | BSD-3-Clause | 139,167 |
| [Node.js](entries/lang/node.md) | 在服务器和命令行里运行 JavaScript，并让前端工具链有一个统一的运行时。 | MIT | 122,261 |
| [Rust](entries/lang/rust.md) | 在编译期约束内存所有权，用来写既要性能、又要避免一整类内存错误的程序。 | MIT OR Apache-2.0 | 119,613 |
| [TypeScript](entries/lang/typescript.md) | 在 JavaScript 上增加可擦除的类型，让编辑器和编译器在运行前指出一类错误。 | Apache-2.0 | 111,371（见正文） |

## 界面与前端

做网页界面时最常见的库、框架和构建工具。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
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
| [DuckDB](entries/data/duckdb.md) | 嵌在进程里的分析型数据库，直接对本地文件和表格数据跑 SQL。 | MIT | 42,053 |
| [JupyterLab](entries/data/jupyterlab.md) | 在浏览器里把代码、图表和说明放进同一本可反复运行的笔记本。 | BSD-3-Clause | 15,347（见正文） |
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
| [llama.cpp](entries/ai/llama-cpp.md) | 用纯 C/C++ 在本机 CPU 和 GPU 上运行量化后的大语言模型。 | MIT | 130,658 |
| [Ollama](entries/ai/ollama.md) | 用一条命令下载并运行本地大模型，再通过本机接口供其他程序调用。 | MIT | 182,543 |
| [PyTorch](entries/ai/pytorch.md) | 用 Python 写张量计算和神经网络，研究训练和模型实现大多从这里开始。 | BSD-3-Clause | 104,007（见正文） |
| [Transformers](entries/ai/transformers.md) | 用同一套 Python 接口加载、训练和运行大量文本、图像和语音模型。 | Apache-2.0 | 166,948 |

## 自托管应用

装在自己服务器上、给人或家庭直接用的完整产品。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Immich](entries/selfhost/immich.md) | 自建照片和视频库，在手机上备份，在浏览器里按时间线、人物和地点浏览。 | AGPL-3.0 | 115,876 |
| [Nextcloud](entries/selfhost/nextcloud.md) | 自建文件同步、日历、联系人和协作入口，用来替代一整套厂商云办公套件。 | AGPL-3.0 | 37,047 |
| [Paperless-ngx](entries/selfhost/paperless-ngx.md) | 把扫描件收成可搜索的文档库，用标签、通信方和日期代替一叠文件夹。 | GPL-3.0 | 46,447 |

## 创作

制作图像、三维和动画的专业工具。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Blender](entries/media/blender.md) | 在一个程序里完成三维建模、雕刻、绑定、动画、材质、渲染和视频剪辑。 | GPL-2.0-or-later | 20,791（见正文） |
| [GIMP](entries/media/gimp.md) | 用图层、选区和画笔编辑照片与位图，覆盖修图、合成和格式转换。 | GPL-3.0-or-later | 6,497（见正文） |
| [OBS Studio](entries/media/obs-studio.md) | 把摄像头、窗口和屏幕组合成一个画面，用来直播或录成视频。 | GPL-2.0 | 77,210 |

星标取自 GitHub API，统计日见各条目的 `stars_at`。星标只说明仓库被关注的程度，不代替采用率。PostgreSQL 这类镜像仓库星标偏低，仍然是行业默认选择。
<!-- catalog:end -->
