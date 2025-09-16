# handlers/file_transfer.py
import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.pdf_utils import extract_text_from_pdf

AWAIT_FILE = 1

async def file_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please upload a PDF file as a document. Or send /cancel to exit.")
    return AWAIT_FILE

async def receive_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    if not doc:
        await update.message.reply_text("No document found. Please send PDF as a document.")
        return AWAIT_FILE

    if not doc.file_name.lower().endswith(".pdf"):
        await update.message.reply_text("Only PDF files are supported in this flow. Send a PDF.")
        return AWAIT_FILE

    os.makedirs("data/uploads", exist_ok=True)
    local_path = os.path.join("data/uploads", doc.file_name)
    file_obj = await doc.get_file()
    await file_obj.download_to_drive(custom_path=local_path)
    await update.message.reply_text("✅ File saved. Extracting text (this may take a moment)...")
    text = extract_text_from_pdf(local_path)
    if not text.strip():
        await update.message.reply_text("No text extracted from PDF (maybe scanned images). Try /ocr with images.")
    else:
        # Telegram has message limit; send in chunks.
        limit = 4000
        for i in range(0, len(text), limit):
            await update.message.reply_text(text[i:i+limit])
    return -1  # end conversation

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Operation cancelled.")
    return -1
