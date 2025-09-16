# handlers/ocr.py
import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.ocr_utils import image_to_text

AWAIT_IMAGE = 1

async def ocr_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please send an image or photo. You can also send a PDF page as an image file.")
    return AWAIT_IMAGE

async def receive_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # handle photo (largest size) or document image
    photo = None
    if update.message.photo:
        photo = update.message.photo[-1]  # highest resolution
    elif update.message.document and update.message.document.mime_type and update.message.document.mime_type.startswith("image"):
        photo = update.message.document
    else:
        await update.message.reply_text("No image detected. Please send an image or photo.")
        return AWAIT_IMAGE

    os.makedirs("data/ocr", exist_ok=True)
    filename = photo.file_name if getattr(photo, "file_name", None) else f"img_{photo.file_unique_id}.jpg"
    local_path = os.path.join("data/ocr", filename)
    file_obj = await photo.get_file()
    await file_obj.download_to_drive(custom_path=local_path)

    await update.message.reply_text("🖨️ Running OCR, please wait...")
    text = image_to_text(local_path)
    if not text.strip():
        await update.message.reply_text("No text found in image.")
    else:
        limit = 4000
        for i in range(0, len(text), limit):
            await update.message.reply_text(text[i:i+limit])
    return -1

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("OCR cancelled.")
    return -1
