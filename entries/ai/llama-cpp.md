---
name: llama.cpp
slug: llama-cpp
category: ai
primary_repo: ggml-org/llama.cpp
url: https://github.com/ggml-org/llama.cpp
website: https://github.com/ggml-org/llama.cpp
license: MIT
language: C++
stars: 130658
stars_at: 2026-10-10
summary: 用纯 C/C++ 在本机 CPU 和 GPU 上运行量化后的大语言模型。
trending: yes
trending_why: 让量化后的大模型在普通 CPU 和 GPU 上运行，是这轮本地推理的基础实现。
tags: [推理, 本地模型]
---

## 它解决什么问题

大语言模型的原始权重既大又依赖一整套 Python 训练框架。很多人只想在自己的机器上回答问题，不想为每次推理装一套训练环境。llama.cpp 把推理做成可移植的 C/C++ 程序，并支持量化格式，让模型能放进普通工作站甚至笔记本。

## 核心功能

- 本地推理。不把提示词发到第三方服务，计算发生在运行它的机器上。
- GGUF 等量化模型格式，用较低的位数换内存占用。
- 多种硬件后端，覆盖 CPU 和常见 GPU 加速接口。
- 内置 HTTP 服务器示例，方便其他程序用本地接口调用。

## 通常怎么用

开发者下载一个允许使用的量化模型，用命令行或本地服务做试验、离线助手和编程辅助。Ollama 等更完整的产品在底层也会借鉴或使用同类 runtime。选模型时先看权重许可证和显存，再看工具本身。

## 它不负责什么

它不提供模型权重，也不证明某个模型可以商用。量化会损失效果，数字越小不一定越适合你的任务。它不是向量数据库、聊天产品或完整的智能体框架。训练和新模型结构的支持速度，取决于上游是否已经实现对应架构。

## 许可与热度

MIT。2026-10-10，`ggml-org/llama.cpp` 有 130,658 星。热度来自「在自己的机器上把模型跑起来」这件事，而不是来自某一个聊天应用的界面。
