---
name: Transformers
slug: transformers
category: ai
primary_repo: huggingface/transformers
url: https://github.com/huggingface/transformers
website: https://huggingface.co/docs/transformers
license: Apache-2.0
language: Python
stars: 166948
stars_at: 2026-10-10
summary: 用同一套 Python 接口加载、训练和运行大量文本、图像和语音模型。
tags: [模型, 训练]
---

## 它解决什么问题

每个实验室的模型仓库都有自己的加载脚本、分词器和配置格式。研究者和工程师要把一个模型跑起来，先得读懂那一套约定。Transformers 把常见模型收成统一的配置、分词和前向接口，并和 Hugging Face 上的模型文件对应。

## 核心功能

- 按名称加载模型和分词器，处理文本、视觉、音频和多模态任务。
- 训练和微调循环所需的模型和处理器抽象。
- 与 PyTorch 等框架配合，而不是自己再实现一个张量库。
- 模型定义可追溯。权重文件和许可仍属于各个模型自己的发布者。

## 通常怎么用

研究原型、分类和抽取服务、以及微调一个已发布的模型时，会从这里加载结构。真正把大模型高效率地跑在笔记本上，常常改用 llama.cpp 或 Ollama。训练大模型还需要数据、算力和分布式策略，库只提供模型侧的接口。

## 它不负责什么

它不授予任何模型权重的使用权。模型卡上的许可证可能是 Apache-2.0，也可能限制商业使用。它也不负责推理速度的极致优化，量化、算子融合和本地 runtime 有专门项目。自动下载权重时要注意来源和体积。

## 许可与热度

代码以 Apache-2.0 发布。2026-10-10，`huggingface/transformers` 有 166,948 星。代码许可不能自动套到通过它下载的模型权重上。
