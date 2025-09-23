import os
from telegram.ext import Application
from handlers.start import start_handler
from handlers.ask import ask_handler
from handlers.search import search_handler
from handlers.file_transfer import file_handler

# Load keys from environment (set in Render)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    app.add_handler(start_handler)
    app.add_handler(ask_handler)
    app.add_handler(search_handler)
    app.add_handler(file_handler)

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
