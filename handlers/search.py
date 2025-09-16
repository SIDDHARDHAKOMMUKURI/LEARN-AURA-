# handlers/search.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.serp_api import serp_search

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args) if context.args else None
    if not query:
        await update.message.reply_text("Usage: /search <query>")
        return
    await update.message.reply_text("🔎 Searching the web...")
    try:
        results = serp_search(query, num=5)
    except Exception as e:
        await update.message.reply_text(f"Search error: {e}")
        return
    if not results:
        await update.message.reply_text("No results found.")
        return
    text_lines = []
    for i, r in enumerate(results, 1):
        title = r.get("title") or r.get("snippet") or "No title"
        link = r.get("link") or r.get("url") or ""
        text_lines.append(f"{i}. {title}\n{link}")
    await update.message.reply_text("\n\n".join(text_lines))
