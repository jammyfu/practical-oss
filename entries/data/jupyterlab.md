---
name: JupyterLab
slug: jupyterlab
category: data
primary_repo: jupyterlab/jupyterlab
url: https://github.com/jupyterlab/jupyterlab
website: https://jupyter.org/
license: BSD-3-Clause
language: TypeScript
stars: 15347
stars_at: 2026-10-10
stars_note: "Jupyter 生态还包括 Notebook 格式和内核。这个星标只属于 JupyterLab 这个界面仓库。"
summary: 在浏览器里把代码、图表和说明放进同一本可反复运行的笔记本。
tags: [笔记本, 分析]
---

## 它解决什么问题

数据分析的过程往往是一小段代码、一张图、一句结论，然后再来一小段。普通脚本把这些过程藏进文件和输出日志里，别人很难按同样的顺序重看。Jupyter 用笔记本保存这个顺序。JupyterLab 是现在的主要界面。

## 核心功能

- 笔记本由单元格组成。代码单元格运行后，输出留在它下面。
- 支持多种内核。最常见的是 Python，也可以换 R 或其他语言。
- 文件浏览、终端、文本编辑和笔记本放在同一个工作区。
- 笔记本文件是开放格式，可以交给版本管理和别的界面打开。

## 通常怎么用

研究、教学、探索性数据分析和模型试验用它记录过程。结论稳定之后，再把要重复运行的部分收成脚本或服务。生产推理和定时报表通常不直接靠一个打开着的笔记本。

## 它不负责什么

JupyterLab 不提供数据本身，也不保证笔记本会被从上到下干净地重跑。单元格可以不按顺序执行，隐藏的状态是它最常见的坑。多人和调度要另加平台，界面只负责交互。

## 许可与热度

BSD-3-Clause。2026-10-10，`jupyterlab/jupyterlab` 有 15,347 星。笔记本这种方式在科学计算和数据工作里的采用范围，大于这个界面仓库的星标。
