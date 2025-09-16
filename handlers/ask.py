# handlers/ask.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.gemini_api import ask_gemini

async def ask_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args) if context.args else None
    if not question:
        await update.message.reply_text("Usage: /ask <your question>")
        return
    await update.message.reply_text("🤔 Thinking...")
    try:
        answer = ask_gemini(question)
    except Exception as e:
        answer = f"(AI error) {e}"
    await update.message.reply_text(answer)

