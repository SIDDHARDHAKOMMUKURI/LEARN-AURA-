from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters
from utils.file_utils import convert_file

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    file_path = f"downloads/{update.message.document.file_name}"
    await file.download_to_drive(file_path)

    await update.message.reply_text("📂 File received. Converting...")

    converted_path = convert_file(file_path)

    if converted_path:
        await update.message.reply_document(document=open(converted_path, "rb"))
    else:
        await update.message.reply_text("❌ Conversion failed.")

file_handler = MessageHandler(filters.Document.ALL, handle_file)
