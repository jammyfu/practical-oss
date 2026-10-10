---
name: TypeScript
slug: typescript
category: lang
primary_repo: microsoft/TypeScript
url: https://github.com/microsoft/TypeScript
website: https://www.typescriptlang.org/
license: Apache-2.0
language: TypeScript
stars: 111371
stars_at: 2026-10-10
stars_note: "2026-10-10，GitHub 按字节把仓库主语言标成 Go。使用者写的仍是 TypeScript，编译器实现里已经有大量 Go 代码。"
summary: 在 JavaScript 上增加可擦除的类型，让编辑器和编译器在运行前指出一类错误。
tags: [JavaScript, 类型]
---

## 它解决什么问题

JavaScript 要等到运行才知道一个字段是不是不存在、一个函数收到的是不是预期形状。项目一大，重命名和重构就靠搜索。TypeScript 让类型写在代码里，编辑器可以据此补全和报错，再把类型擦掉，输出普通 JavaScript。

## 核心功能

- 类型标注、接口、联合类型和泛型。类型不进入运行时的 JavaScript 值。
- 根据已有 JavaScript 和使用方式做类型推断，不必给每一行都手写类型。
- 编译成指定版本的 JavaScript，用来对齐目标浏览器或 Node 版本。
- 声明文件。没有类型的 JavaScript 库也可以被类型系统认识。

## 通常怎么用

新的 React、Vue、Node 和构建工具项目大多直接用它。它靠编辑器集成发挥作用，所以通常和 VS Code 或带语言服务的 Neovim 一起用。类型只覆盖写出来的契约，外部接口返回的真实数据仍要在边界上校验。

## 它不负责什么

TypeScript 不提供运行时框架，也不替代测试。`any` 和类型断言可以让检查失效。仓库里的 Go 代码是编译器实现的一部分，不表示用 TypeScript 的人要改去写 Go。

## 许可与热度

Apache-2.0。2026-10-10，`microsoft/TypeScript` 有 111,371 星。它是 JavaScript 生态里使用最广的类型层。
