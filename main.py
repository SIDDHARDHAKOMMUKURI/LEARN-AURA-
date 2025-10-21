import os
from flask import Flask
from threading import Thread
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters
)
from handlers.start import start_handler, help_handler
from handlers.ask import ask_handler
from handlers.books import books_handler, book_callback
from handlers.convert import convert_handler, button_callback, file_upload
from handlers.search import search_handler

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Flask for uptime ping
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "LearnAuraBot is running!"

def run_flask():
    web_app.run(host="0.0.0.0", port=8080)

# Telegram bot setup
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start_handler))
app.add_handler(CommandHandler("help", help_handler))
app.add_handler(CommandHandler("ask", ask_handler))
app.add_handler(CommandHandler("books", books_handler))
app.add_handler(CommandHandler("convert", convert_handler))
app.add_handler(CommandHandler("search", search_handler))
app.add_handler(CallbackQueryHandler(button_callback))
app.add_handler(CallbackQueryHandler(book_callback))
app.add_handler(MessageHandler(filters.Document.ALL, file_upload))

if __name__ == "__main__":
    Thread(target=run_flask).start()
    print("🚀 LearnAuraBot is live.")
    app.run_polling()
