# repo_basic_report

一个用于扫描 Python 项目结构的命令行工具。

输入一个本地项目目录，程序会递归扫描其中的 `.py` 文件，统计文件行数、函数名、类名和 import 信息，并生成 JSON 格式的项目结构报告。

## 功能

- 递归扫描指定目录下的 Python 文件
- 自动忽略 `.venv`、`__pycache__`、`.git` 等无关目录
- 统计每个 Python 文件的行数
- 提取函数名、类名和 import 信息
- 将扫描结果保存为 `report.json`

## 技术栈

- Python
- pathlib
- JSON
- argparse
- Git

## 项目结构

```text
repo_basic_report/
├─ main.py
├─ code_parser.py
├─ repo_scanner.py
├─ report_builder.py
├─ json_utils.py
├─ config.py
├─ README.md
└─ output/
