# Python 第一课：从输入到输出

本课对应代码：`practice/progress.py`。

## 学习目标

- 用变量保存数据
- 用函数封装一项工作
- 用条件判断拒绝无效数据
- 用返回值把结果交给其他代码
- 用测试证明结果符合预期

## 读懂核心函数

```python
def progress_summary(completed: int, total: int) -> str:
```

- `def` 表示定义函数。
- `completed` 和 `total` 是函数接收的数据。
- `int` 表示预期传入整数。
- `-> str` 表示函数会返回文本。

```python
percentage = completed / total * 100
```

这一行依次完成除法、乘法，再把结果保存到 `percentage`。

```python
return f"已完成 {completed}/{total} 项（{percentage:.0f}%）"
```

`return` 返回结果；`f"..."` 可以把变量嵌入文本；`.0f` 表示显示为不带小数位的数字。

## 自己运行

```powershell
python -m practice.progress
```

预期结果：

```text
已完成 3/5 项（60%）
```

然后运行全部测试：

```powershell
python -m unittest discover -v
```

## 练习

先思考，再尝试修改：

1. 把示例改成完成 4 项、总共 8 项，预测输出。
2. 传入 `completed=9, total=8`，观察错误信息。
3. 尝试让百分比保留一位小数，并相应修改测试。

