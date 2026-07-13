from report_builder import build_report
from json_utils import save_json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("project_path",help="项目路径")
parser.add_argument("--output","-o",help="输出路径",default="output/report.json")
args = parser.parse_args()

report = build_report(args.project_path)
save_json(report, args.output)

print("报告已生成：", args.output)