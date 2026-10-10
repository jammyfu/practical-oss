---
name: Open WebUI
slug: open-webui
category: selfhost
primary_repo: open-webui/open-webui
url: https://github.com/open-webui/open-webui
website: https://openwebui.com
license: Open WebUI License（源码可用，非 OSI）
language: Python
stars: 154158
stars_at: 2026-10-10
summary: 自托管的网页聊天界面，用来连接本地或远程的模型接口。
trending: yes
trending_why: 给 Ollama 或兼容接口补一个可登录的聊天入口时，它是目前被广泛部署的界面，但现行许可已不是 MIT。
tags: [聊天界面, 自托管, 许可]
---

## 它解决什么问题

Ollama、vLLM 或远程的兼容接口能生成文字，但通常不负责团队要用的登录、会话和权限。Open WebUI 放在这些接口前面，让人在浏览器里选模型、保留对话，而不必自己再做一套聊天产品。

## 核心功能

- 同时连接本地的 Ollama 和远程的 OpenAI 兼容接口。
- 多用户、分组和权限，把一个实例分给一组人使用。
- 把上传的文档放进对话做检索，用来带上自己的资料。
- 给模型保存预设，用来固定提示词、工具和谁可以使用。

## 通常怎么用

部署在自己的服务器上，把后端指到本机的 Ollama 或内网里的推理服务，再把地址发给需要用模型的人。它适合作为内部聊天入口。真正的生成发生在后面的模型服务里，这个界面负责账号、会话和调用。

## 它不负责什么

它不是推理引擎，也不附带可商用的模型权重。后面接哪家接口，仍要遵守那家的条款、额度和数据政策。它也不是可以随意去掉名称和标志、再包装成另一个产品的白标界面。品牌能不能改，由下面的许可门槛决定，而不是由源码公开本身决定。

## 许可与热度

GitHub 上的 SPDX 标识是 NOASSERTION。现行 LICENSE 的标题是 Open WebUI License：在保留版权声明、免责声明和名称使用限制之外，还禁止在部署或分发中更改、移除、遮挡或替换 Open WebUI 的名称、标志等品牌标识。例外只有三种：任意连续三十天内、能直接使用该应用的自然人不超过五十人；事先取得版权人的书面许可；或者企业许可明确允许这种修改。这项品牌限制使它不符合 OSI 开源定义。源码仍可在这些条件下再分发，但不能把它写成 MIT 或 BSD。

LICENSE_NOTICE 写明仓库里的材料按时期分许可：更早的提交先后适用 MIT 和 BSD-3-Clause，其后的新代码适用现行许可。旧材料仍按各自原文，不能把当前这棵代码树整体说成开源。2026-10-10，`open-webui/open-webui` 有 154,158 星。
