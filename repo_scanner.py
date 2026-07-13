from pathlib import Path
import config
def should_ignore(path):
    for part in path.parts:
        if part in config.IGNORE_DIRS:
            return True
    return False

def find_python_files(project_path):
    root = Path(project_path)
    python_files = []
    for file_path in root.rglob("*.py"):
        if should_ignore(file_path):
            continue
        python_files.append(file_path)
    return python_files