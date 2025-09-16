# handlers/sentiment.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.sentiment_utils import analyze_sentiment

async def sentiment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args) if context.args else None
    if not text:
        await update.message.reply_text("Usage: /sentiment <text>")
        return
    result = analyze_sentiment(text)
    await update.message.reply_text(f"Sentiment: {result['label']}\nScore: {result['score']:.3f}")
