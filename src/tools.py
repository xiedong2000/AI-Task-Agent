from datetime import datetime
from pathlib import Path


def calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"


def read_document(filename: str) -> str:
    try:
        path = Path(filename).expanduser()

        if not path.exists():
            return f"Document error: File not found: {filename}"

        if path.suffix.lower() == ".pdf":
            try:
                from pypdf import PdfReader

                reader = PdfReader(str(path))
                pages = []

                for page in reader.pages:
                    text = page.extract_text() or ""
                    if text.strip():
                        pages.append(text.strip())

                if pages:
                    return "\n\n".join(pages)

                return "Document error: No readable text found in the PDF."
            except Exception as e:
                return f"Document error: Could not read PDF: {e}"

        raw = path.read_bytes()
        for encoding in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
            try:
                return raw.decode(encoding)
            except UnicodeDecodeError:
                continue
        return raw.decode("utf-8", errors="replace")
    except Exception as e:
        return f"Document error: {e}"


def get_current_datetime() -> str:
    return datetime.now().astimezone().isoformat()