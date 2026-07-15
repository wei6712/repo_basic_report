from pathlib import Path
import json
from llm_client import call_llm


def analyze_report(report_path, output_path):
    report_path = Path(report_path)
    output_path = Path(output_path)
    with open(report_path,"r",encoding="utf-8") as f:
        report = json.load(f)
    report_text = json.dumps(report,ensure_ascii=False,indent=2)

    prompt = f"""
    你是一名专业的 Python 项目分析助手。
    
    请根据下面的 repo_basic_report 扫描结果，生成一份中文项目分析报告。
    
    要求：
    1. 总结项目整体用途
    2. 分析主要文件的职责
    3. 根据函数名推测项目处理流程
    4. 指出当前项目结构的优点
    5. 指出 2-3 个后续可以改进的方向
    
    以下是 report.json 内容：
    
    {report_text}
    """

    result = call_llm(prompt)
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(result,encoding="utf-8")
    return result