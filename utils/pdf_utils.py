# utils/pdf_utils.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(path: str) -> str:
    try:
        reader = PdfReader(path)
        text_parts = []
        for page in reader.pages:
            txt = page.extract_text() or ""
            text_parts.append(txt)
        return "\n".join(text_parts)
    except Exception as e:
        return f"Error extracting text: {e}"
