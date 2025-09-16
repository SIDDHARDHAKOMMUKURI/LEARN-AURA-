import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Import handlers
from handlers.start import start_handler
from handlers.ask import ask_handler
from handlers.search import search_handler
from handlers.file_transfer import file_handler
from handlers.sentiment import sentiment_handler

# MongoDB
from utils.db_utils import init_db

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    """Run LearnAuraBot"""

    # Telegram Bot Token
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("❌ BOT_TOKEN not found in .env file!")

    # Initialize MongoDB
    db = init_db()

    # Initialize bot application
    application = Application.builder().token(token).build()

    # Register command handlers
    application.add_handler(start_handler(db))
    application.add_handler(ask_handler(db))
    application.add_handler(search_handler(db))
    application.add_handler(file_handler(db))
    application.add_handler(sentiment_handler(db))

    # Handle text messages (optional fallback)
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, lambda u, c: u.message.reply_text("Use /ask, /search, or /file."))
    )

    # Start polling
    logger.info("🤖 LearnAuraBot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
