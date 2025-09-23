from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.search_utils import search_web

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please provide a search query. Example: /search Python basics")
        return

    query = " ".join(context.args)
    results = search_web(query)

    if not results:
        await update.message.reply_text("⚠️ No results found.")
        return

    reply = "🔎 Search Results:\n\n"
    for r in results[:5]:  # Top 5 results
        reply += f"• [{r['title']}]({r['link']})\n"

    await update.message.reply_text(reply, disable_web_page_preview=True)

search_handler = CommandHandler("search", search)
