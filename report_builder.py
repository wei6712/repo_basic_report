from code_parser import count_lines, extract_function_names, extract_class_names, extract_imports
from repo_scanner import find_python_files
def build_file_info(file_path):
    return {
        "path": str(file_path),
        "name": file_path.name,
        "line_count": count_lines(file_path),
        "functions": extract_function_names(file_path),
        "classes": extract_class_names(file_path),
        "imports": extract_imports(file_path),
    }

def build_report(project_path):
    python_files = find_python_files(project_path)
    files = []
    for file_path in python_files:
        file_info = build_file_info(file_path)
        files.append(file_info)

    return {
        "project_path": str(project_path),
        "python_file_count": len(files),
        "files": files
    }