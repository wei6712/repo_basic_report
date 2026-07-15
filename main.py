from report_builder import build_report
from json_utils import save_json
from analyze_report import analyze_report
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("project_path",help="项目路径")
parser.add_argument("--output","-o",help="输出路径",default="output/report.json")
parser.add_argument("--analyze",action="store_true",help="开启ai分析输出")
args = parser.parse_args()

report = build_report(args.project_path)
save_json(report, args.output)

print("报告已生成：", args.output)

if args.analyze:
    analyze_report_text = analyze_report(args.output, "output/analysis.md")
    print(analyze_report_text)
    print("AI 分析报告已生成：output/analysis.md")