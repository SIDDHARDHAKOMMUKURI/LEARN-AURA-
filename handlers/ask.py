from telegram import Update
from telegram.ext import ContextTypes
from utils.ai_utils import gemini_answer

async def ask_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("❓ Type `/ask <your question>`.")
        return
    await update.message.reply_text("🤔 Thinking...")
    reply = await gemini_answer(question)
    await update.message.reply_text(reply or "⚠️ No response.")
