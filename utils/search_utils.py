# handlers/search.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.search_utils import search_web

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = " ".join(context.args)
    if not q:
        await update.message.reply_text("Usage: /search <topic>")
        return
    await update.message.reply_text("🔍 Searching...")
    res = search_web(q)
    await update.message.reply_text(res or "❌ No results.")
