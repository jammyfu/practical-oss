---
name: CPython
slug: cpython
category: lang
primary_repo: python/cpython
url: https://github.com/python/cpython
website: https://www.python.org/
license: PSF-2.0
language: Python
stars: 77602
stars_at: 2026-10-10
summary: Python 语言最常用的解释器，脚本、数据分析和大量后端服务都跑在它上面。
tags: [Python, 运行时]
---

## 它解决什么问题

人们需要一种读起来接近英文、又能调用成熟科学计算和 Web 库的语言。CPython 是 Python 语言的参考实现，也是 python.org 上提供的那个解释器。说「装 Python」时，绝大多数情况指的就是它。

## 核心功能

- 解释执行 Python，并提供标准库：文件、网络、进程、测试、日期和数据格式都在里面。
- C 扩展接口。NumPy、数据库驱动和很多加速模块通过它接到底层库。
- 包生态的运行时。pip 安装的包最终由 CPython 加载。
- 多版本并存。系统、项目和虚拟环境可以各用一个解释器版本。

## 通常怎么用

自动化脚本、Django 和 FastAPI 服务、数据分析和机器学习训练脚本，默认都选 CPython。虚拟环境用来隔离项目依赖。需要更短的启动时间或更强的静态类型时，会改用 Go、Rust，或 Python 的其他实现，但库兼容性仍以 CPython 为准。

## 它不负责什么

它不规定依赖怎么锁定，那是 pip、uv 或 Poetry 的事。全局解释器锁使多线程不适合承担 CPU 密集的并行，这类工作通常用多进程或放到 C、Rust 扩展里。它也不把应用打包成单一可执行文件，那需要额外的打包工具。

## 许可与热度

以 Python Software Foundation License 2.0 发布，这是被 OSI 认可的宽松许可。2026-10-10，`python/cpython` 有 77,602 星。Python 的实际使用范围远大于这个仓库的星标。
