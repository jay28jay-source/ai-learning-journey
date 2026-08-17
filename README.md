# AI Learning Journey

[![Tests](https://github.com/jay28jay-source/ai-learning-journey/actions/workflows/tests.yml/badge.svg)](https://github.com/jay28jay-source/ai-learning-journey/actions/workflows/tests.yml)

这是我的第一个 GitHub 仓库，用来公开记录从零学习 Git、Python 和 AI 工程的过程。

## 当前目标

- 学会 Git 与 GitHub 的基本工作流
- 掌握项目需要的 Python 基础
- 完成 API、RAG、Agent、多模态和具身智能方向的项目
- 用公开、可运行的作品证明自己的能力

## 第一个程序

`hello.py` 是这个仓库里的第一个 Python 程序。安装 Python 后，在当前文件夹运行：

```powershell
python hello.py
```

预期输出：

```text
Hello, AI engineering journey!
今天完成一个小步骤，长期积累一个作品集。
```

## 自动测试

测试用于确认修改代码后，原来的功能仍然正常：

```powershell
python -m unittest discover -v
```

仓库还包含一项 GitHub Actions 自动检查。发布到 GitHub 后，每次推送和 Pull Request 都会自动运行同样的测试。

## Python 练习

第一组练习是一个学习进度计算器，代码位于 `practice/progress.py`。配套讲解见 `PYTHON_LESSON_1.md`。

第二组练习使用 JSON 保存学习记录，代码位于 `practice/study_log.py`。配套讲解见 `PYTHON_LESSON_2.md`。

## 学习记录

### 第 1 天

- 理解仓库：一个项目及其完整历史记录的容器
- 理解提交：给某一批修改拍下一张带说明的“快照”
- 创建第一个 README 和 Python 程序

## 下一步

- 安装 Python
- 配置 Git 用户名和邮箱
- 创建第一次提交
- 在 GitHub 创建公开仓库并推送
