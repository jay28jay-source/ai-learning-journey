# 第一课：Git 与 GitHub 到底是什么

## 一句话区别

- **Git**：安装在电脑上的版本记录工具。
- **GitHub**：存放 Git 仓库、展示作品和协作的网站。

可以把项目文件看作一本书：Git 保存每次修订版本，GitHub 则把这本书和修订历史放到网上。

## 第一次发布会经历什么

1. `git status`：查看哪些文件发生了变化。
2. `git add`：选择要放进下一次快照的文件。
3. `git commit`：保存一次带说明的项目快照。
4. 在 GitHub 创建一个空的公开仓库。
5. `git push`：把本地提交上传到 GitHub。

## 三条重要原则

1. 一次提交只表达一个清楚的变化。
2. 提交说明要让别人一眼看懂做了什么。
3. 密码、API 密钥和 `.env` 文件永远不要提交到公开仓库。

## 本仓库计划中的前三次提交

1. `docs: add project introduction`
2. `feat: add first Python program`
3. `docs: record first learning milestone`

这三次提交会把 README、程序和学习记录分开，形成比“一次上传全部文件”更清晰的开发历史。

