# repo_basic_report

一个用于扫描 Python 项目结构的命令行工具。

输入一个本地项目目录，程序会递归扫描其中的 `.py` 文件，统计文件行数、函数名、类名和 import 信息，并生成 JSON 格式的项目结构报告。

项目还支持调用 DeepSeek API，根据 `report.json` 自动生成 Markdown 格式的中文项目分析报告。

## 功能

- 递归扫描指定目录下的 Python 文件
- 自动忽略 `.venv`、`__pycache__`、`.git` 等无关目录
- 统计每个 Python 文件的行数
- 提取函数名、类名和 import 信息
- 将扫描结果保存为 `report.json`
- 可选调用 DeepSeek API 生成 `analysis.md` 项目分析报告

## 技术栈

- Python
- pathlib
- JSON
- argparse
- OpenAI-compatible API
- DeepSeek API
- Git

## 项目结构

```text
repo_basic_report/
├─ main.py
├─ code_parser.py
├─ repo_scanner.py
├─ report_builder.py
├─ json_utils.py
├─ llm_client.py
├─ analyze_report.py
├─ config.py
├─ README.md
└─ output/
```

## 配置 DeepSeek API Key

AI 分析功能需要配置 DeepSeek API Key。

PowerShell：

```powershell
$env:DEEPSEEK_API_KEY="你的 API Key"
```

CMD：

```cmd
set DEEPSEEK_API_KEY=你的 API Key
```

注意：不要把 API Key 写进代码，也不要提交到 GitHub。

## 使用方式

只生成 JSON 结构报告：

```bash
python main.py . --output output/report.json
```

生成 JSON 结构报告，并调用大模型生成分析报告：

```bash
python main.py . --output output/report.json --analyze
```

## 输出结果

运行后会生成：

```text
output/report.json
output/analysis.md
```

其中：

- `report.json`：项目结构化扫描结果。
- `analysis.md`：DeepSeek 生成的中文项目分析报告。

## 当前阶段

这是 RepoInsight 项目的第三阶段基础版本。

当前版本已经完成：

- 本地 Python 项目扫描
- JSON 结构化报告生成
- DeepSeek API 调用
- AI 项目分析报告生成

后续计划继续优化 prompt，让模型输出更稳定，并加入代码检索和 issue 分析能力。