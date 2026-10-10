---
name: Ollama
slug: ollama
category: ai
primary_repo: ollama/ollama
url: https://github.com/ollama/ollama
website: https://ollama.com/
license: MIT
language: Go
stars: 182543
stars_at: 2026-10-10
summary: 用一条命令下载并运行本地大模型，再通过本机接口供其他程序调用。
trending: yes
trending_why: 2023 年后成为在自己电脑上运行大模型的默认命令。
tags: [本地模型, 推理]
---

## 它解决什么问题

llama.cpp 已经能推理，但拉取模型、选择量化、启动 GPU 和暴露接口仍要自己拼。Ollama 把这些收成一个本地服务：拉取一个模型名，然后用命令行或 HTTP 跟它对话。

## 核心功能

- 模型库式的拉取和运行。常用开源权重有现成的打包方式。
- 本机 API。其他应用可以把 Ollama 当作一个只监听本地的模型服务。
- 自动处理一部分硬件加速和模型切换。
- 模型文件、提示模板和参数可以写成可复用的 Modelfile。

## 通常怎么用

个人和开发团队用它在笔记本上试 DeepSeek、Qwen、Gemma 等权重，或给编辑器插件提供本地补全。数据不必为了试验就送到外部 API。生产环境的多租户、配额和内容安全仍要在它外面另做。

## 它不负责什么

Ollama 不拥有模型权重的许可。一个模型能被 `pull` 下来，只说明打包流程存在，不说明你可以把它用在商业产品里。它也不是训练框架。界面、知识库和工具调用编排通常由别的应用完成。

## 许可与热度

MIT。2026-10-10，`ollama/ollama` 有 182,543 星。使用前分别核对工具许可和所拉模型的许可。
