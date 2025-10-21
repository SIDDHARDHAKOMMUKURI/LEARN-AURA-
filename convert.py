from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
import os
from utils.convert_utils import convert_file

async def convert_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("📄 PDF→TXT", callback_data="pdf_to_txt"),
         InlineKeyboardButton("📝 TXT→PDF", callback_data="txt_to_pdf")],
        [InlineKeyboardButton("📘 PDF→Word", callback_data="pdf_to_docx"),
         InlineKeyboardButton("📗 Word→PDF", callback_data="docx_to_pdf")]
    ]
    await update.message.reply_text("Select conversion type:", reply_markup=InlineKeyboardMarkup(buttons))

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    context.user_data["convert_type"] = q.data
    await q.edit_message_text("📎 Upload your file now.")

async def file_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ctype = context.user_data.get("convert_type")
    if not ctype:
        await update.message.reply_text("Use /convert first to select conversion type.")
        return
    doc = await update.message.document.get_file()
    os.makedirs("input", exist_ok=True)
    path = f"input/{update.message.document.file_name}"
    await doc.download_to_drive(path)
    out = await convert_file(path, ctype)
    if out:
        await update.message.reply_document(open(out, "rb"))
        os.remove(out)
