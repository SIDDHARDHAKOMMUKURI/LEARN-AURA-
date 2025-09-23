from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌟 Welcome to LearnAuraBot 🌟\n\n"
        "📚 Features:\n"
        "/ask <question> – Ask AI (Gemini/OpenAI)\n"
        "/search <query> – Search the web (SerpAPI)\n"
        "📂 Send me a file – I’ll convert between PDF, DOCX, PPTX, TXT, Image/Text\n"
    )
    await update.message.reply_text(text)

start_handler = CommandHandler("start", start)
