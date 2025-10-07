import os
from telegram.ext import Application, CommandHandler
from handlers.start import start_handler
from handlers.ask import ask_handler
from handlers.search import search_handler
from handlers.file_transfer import file_handler
from handlers.motivate import motivate_handler

# --- Load environment variables ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN is missing in environment variables!")

# --- Main function ---
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # --- Register command handlers ---
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("ask", ask_handler))
    app.add_handler(CommandHandler("search", search_handler))
    app.add_handler(CommandHandler("file", file_handler))
    app.add_handler(CommandHandler("motivate", motivate_handler))

    print("✅ LearnAuraBot is running and connected to Telegram...")
    app.run_polling()

# --- Entry point ---
if __name__ == "__main__":
    main()
