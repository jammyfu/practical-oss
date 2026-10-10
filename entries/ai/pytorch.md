---
name: PyTorch
slug: pytorch
category: ai
primary_repo: pytorch/pytorch
url: https://github.com/pytorch/pytorch
website: https://pytorch.org/
license: BSD-3-Clause
language: Python
stars: 104007
stars_at: 2026-10-10
stars_note: "GitHub 未给出 SPDX 标识。仓库 LICENSE 使用带三条条件的 BSD 文本。"
summary: 用 Python 写张量计算和神经网络，研究训练和模型实现大多从这里开始。
tags: [训练, 张量]
---

## 它解决什么问题

神经网络需要在 CPU 或 GPU 上做大量可求导的数值计算。研究者还要能随时改模型结构并看到结果。PyTorch 用接近普通 Python 的方式描述计算，需要梯度时再自动求导，因此试验模型和把它训练出来可以在同一套代码里完成。

## 核心功能

- 张量运算，以及在 NVIDIA 等 GPU 上执行这些运算。
- 自动求导。前向计算怎么写，反向梯度就怎么被记录。
- 神经网络模块、优化器和数据加载这些训练所需的基本零件。
- 可以从 Python 调用，性能敏感的算子在底层用 C++ 和 GPU 代码实现。

## 通常怎么用

研究论文、自定义模型和企业里的训练任务通常用它实现。训练好的模型再交给 Transformers、llama.cpp、Ollama 或专门的推理服务去运行。只想在笔记本上对话、不改模型结构时，不必从 PyTorch 开始。

## 它不负责什么

它不提供某个模型的权重和使用权，也不负责数据集的合法性。GPU 驱动、分布式训练和实验记录都在库之外。BSD 许可允许很多用法，但模型、数据和其他依赖的许可要分开看。

## 许可与热度

LICENSE 文件是 BSD 三句式许可。2026-10-10，`pytorch/pytorch` 有 104,007 星。它是当前深度学习和研究训练的默认框架。
