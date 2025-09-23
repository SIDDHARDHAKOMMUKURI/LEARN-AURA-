from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.ai_utils import ask_ai

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please provide a question. Example: /ask What is AI?")
        return

    query = " ".join(context.args)
    response = ask_ai(query)
    await update.message.reply_text(response)

ask_handler = CommandHandler("ask", ask)
