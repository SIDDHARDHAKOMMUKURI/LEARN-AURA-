from telegram import Update
from telegram.ext import ContextTypes
from utils.db_utils import register_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command and register user in MongoDB"""
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Save user in MongoDB
    db = context.bot_data["db"]
    register_user(db, user.id, user.username)

    # Welcome message
    welcome_text = (
        f"👋 Hello {user.first_name}!\n\n"
        "Welcome to *LearnAuraBot* 🚀\n\n"
        "Here’s what I can do:\n"
        "• 🤖 `/ask` – Get AI-powered answers\n"
        "• 🔍 `/search` – Search topics online\n"
        "• 📂 File tools – Upload & convert files\n"
        "• 📘 Textbooks – (coming soon)\n\n"
        "Type a command to get started!"
    )

    await context.bot.send_message(
        chat_id=chat_id,
        text=welcome_text,
        parse_mode="Markdown"
    )
