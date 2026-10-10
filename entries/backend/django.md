---
name: Django
slug: django
category: backend
primary_repo: django/django
url: https://github.com/django/django
website: https://www.djangoproject.com/
license: BSD-3-Clause
language: Python
stars: 91357
stars_at: 2026-10-10
summary: 带数据模型、管理后台、表单和安全默认值的 Python Web 框架。
tags: [Web, Python]
---

## 它解决什么问题

内容站、内部系统和会员产品一上来就要用户、数据库、表单、后台和基本的安全防护。逐个挑选库可以更灵活，也更容易在认证和权限上留下缺口。Django 把这些做成一套约定，让一个团队能按同一种结构交付完整网站。

## 核心功能

- ORM 和迁移。用 Python 类描述表，再生成可审查的数据库变更。
- 自动管理后台。模型定义出来后，就能有一个可配置的增删改查界面。
- 认证、会话、表单和 CSRF 等安全默认值。
- 模板和视图。既可以渲染服务器端页面，也可以只做 API。

## 通常怎么用

新闻和内容产品、企业内部系统、需要后台的会员网站，是它的典型场合。Django REST framework 常用来补 JSON API。如果服务只是模型推理外面的薄薄一层，FastAPI 通常更轻。

## 它不负责什么

Django 不规定前端框架，也不替你做异步任务的完整运维，Celery 或其他队列要另外部署。它的约定能加快标准业务，也会在高度自定义的数据访问上显得厚。默认开发服务器不能当作生产服务器。

## 许可与热度

BSD-3-Clause。2026-10-10，`django/django` 有 91,357 星。项目从 2005 年前后就开始被广泛部署，星标只反映 GitHub 时代的关注。
