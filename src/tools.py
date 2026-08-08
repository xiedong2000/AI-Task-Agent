from datetime import datetime

def calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"

def read_document(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Document error: {e}"


def get_current_datetime() -> str:
    return datetime.now().astimezone().isoformat()