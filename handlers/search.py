from telegram import Update
from telegram.ext import ContextTypes
from utils.search_utils import search_web

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles /search command with fast async execution."""
    if not context.args:
        await update.message.reply_text("🔎 Please provide a topic to search.\nExample: /search Python basics")
        return

    query = " ".join(context.args)
    await update.message.reply_text("⏳ Searching the web, please wait...")

    # Run blocking web search in thread executor (avoids blocking async loop)
    from concurrent.futures import ThreadPoolExecutor
    import asyncio

    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, search_web, query)

    # Send formatted result
    await update.message.reply_text(result, disable_web_page_preview=True)
