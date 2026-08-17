# Python 第二课：JSON 与文件读写

本课对应代码：`practice/study_log.py`。

## 为什么现在学 JSON

JSON 是 API 最常见的数据格式。以后调用大模型 API、保存 Agent 状态、准备 RAG 数据时，都会频繁遇到它。

下面是一条 JSON 学习记录：

```json
{
  "topic": "Python JSON",
  "minutes": 30,
  "completed": true
}
```

它包含文本、数字和布尔值，分别对应 Python 中的 `str`、`int` 和 `bool`。

## 本课代码做什么

- `save_entries`：把 Python 数据转换成 JSON 并写入文件。
- `load_entries`：读取 JSON，并转换回 Python 数据。
- `total_minutes`：使用循环式表达求出总学习时间。
- `StudyEntry`：声明每条记录应该有哪些字段。

## 自己运行

```powershell
python -m practice.study_log
```

程序会生成一个 `study_log.json`，再读取它并计算学习时间。该示例文件属于运行结果，不需要上传到 GitHub。

## 练习

1. 增加第三条学习记录，并观察总时间。
2. 把一条记录的 `completed` 改为 `False`，再写一个只统计已完成项目时间的函数。
3. 思考：为什么代码明确使用 `encoding="utf-8"`？删除它后，在不同电脑上可能发生什么？

