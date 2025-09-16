# utils/ocr_utils.py
from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path

# If Tesseract not on PATH, user may need to set pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract" (system-specific)

def image_to_text(image_path: str) -> str:
    try:
        # If PDF provided, convert first page to image
        if image_path.lower().endswith(".pdf"):
            images = convert_from_path(image_path, dpi=200, first_page=1, last_page=1)
            if not images:
                return ""
            img = images[0]
            return pytesseract.image_to_string(img, lang="eng")
        else:
            img = Image.open(image_path)
            return pytesseract.image_to_string(img, lang="eng")
    except Exception as e:
        return f"Error running OCR: {e}"
