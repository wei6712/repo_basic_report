def count_lines(file_path):
    count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            count += 1
    return count

def extract_function_names(file_path):
    function_names = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()

            if clean_line.startswith("def "):
                function_names.append(clean_line.split("def ")[1].split("(")[0])
            elif clean_line.startswith("async def "):
                function_names.append(clean_line.split("async def ")[1].split("(")[0])
    return function_names

def extract_class_names(file_path):
    class_names = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line.startswith("class "):
                class_names.append(clean_line.split("class ")[1].split("(")[0].split(":")[0])
    return class_names

def extract_imports(file_path):
    import_names = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()

            if clean_line.startswith("import "):
                import_names.append(clean_line)

            elif clean_line.startswith("from "):
                import_names.append(clean_line)

    return import_names
