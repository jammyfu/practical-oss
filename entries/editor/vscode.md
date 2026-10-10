---
name: Visual Studio Code
slug: vscode
category: editor
primary_repo: microsoft/vscode
url: https://github.com/microsoft/vscode
website: https://code.visualstudio.com/
license: MIT
language: TypeScript
stars: 193498
stars_at: 2026-10-10
summary: 带扩展市场的桌面代码编辑器，把编辑、调试、终端和远程开发放在一个窗口里。
tags: [编辑器, 扩展]
---

## 它解决什么问题

不同语言一度要装不同的 IDE，配置不能带走，远程机器上的项目还得再配一遍。VS Code 用一个相对轻的编辑器核心，加上扩展，覆盖多数语言的高亮、跳转、调试和格式化，并把远程 SSH、容器和浏览器开发做成同一套界面。

## 核心功能

- 文本编辑、多光标、集成终端和工作区搜索。
- 扩展 API。语言支持、主题、Lint、测试和 AI 助手大多是扩展，而不是核心里写死的功能。
- 调试适配器。同一种「打断点、看变量」的界面可以接到不同语言。
- 远程开发。界面在本地，语言服务可以跑在 SSH 主机、容器或浏览器里的 vscode.dev。

## 通常怎么用

学生、前端、Python 和大量企业团队把它当作默认编辑器。打开文件夹就能工作，语言能力靠安装对应扩展。需要完整的可视化设计和深度框架集成时，有些人仍会回到专用 IDE，例如完整的 Visual Studio、JetBrains 或 Xcode。

## 它不负责什么

仓库 `microsoft/vscode` 是 MIT 许可的 Code - OSS。微软发布的 Visual Studio Code 安装包还包含商标、市场接口和其他并不随这个仓库以同样方式授权的部分。基于 Code - OSS 的发行版，例如 VSCodium，扩展市场和远程功能可能与官方安装包不同。编辑器本身也不编译你的项目，编译仍由语言自己的工具链完成。

## 许可与热度

Code - OSS 为 MIT。2026-10-10，`microsoft/vscode` 有 193,498 星，是开发工具里最显眼的仓库之一。选用时要区分「源码仓库」和「微软分发的安装包」。
