from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌟 *Welcome to LearnAuraBot!*\n\n"
        "Your AI-powered learning assistant.\n\n"
        "🧠 `/ask` – Ask any question (Gemini AI)\n"
        "📚 `/books` – Download Bhagavad Gita or Mahabharata\n"
        "🧾 `/convert` – Convert PDF, Word, or Text files\n"
        "🔍 `/search` – Search topics (via Google)\n"
        "❓ `/help` – View all commands\n"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 *Command Manual*\n"
        "/start – Welcome menu\n"
        "/ask – Ask AI any question\n"
        "/books – Get sacred books (Eng & Telugu)\n"
        "/convert – Convert files\n"
        "/search – Web search\n",
        parse_mode="Markdown"
    )
