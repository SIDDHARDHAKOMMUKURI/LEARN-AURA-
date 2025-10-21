from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
import requests, os

BOOK_LINKS = {
    "gita_english": "https://www.prabhupada-books.de/pdf/Bhagavad-gita-As-It-Is.pdf",
    "gita_telugu": "https://www.sgsgitafoundation.org/assets/resources/SrimadBhagawadGeeta_Telugu.pdf",
    "mahabharata_english": "https://www.holybooks.com/wp-content/uploads/The-Mahabharata-of-Vyasa-English-Prose-Translation.pdf",
    "mahabharata_telugu": "https://www.freegurukul.org/e-Books/06-MahaBharatham/MB003-SampoornaMahaBharatham.pdf"
}

async def books_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("📘 Bhagavad Gita (English)", callback_data="gita_english"),
         InlineKeyboardButton("📗 Bhagavad Gita (Telugu)", callback_data="gita_telugu")],
        [InlineKeyboardButton("📙 Mahabharata (English)", callback_data="mahabharata_english"),
         InlineKeyboardButton("📒 Mahabharata (Telugu)", callback_data="mahabharata_telugu")]
    ]
    await update.message.reply_text("📚 Choose a book to download:", reply_markup=InlineKeyboardMarkup(buttons))

async def book_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data
    url = BOOK_LINKS.get(key)
    await query.edit_message_text("📖 Preparing your download...")

    try:
        os.makedirs("temp_books", exist_ok=True)
        path = f"temp_books/{key}.pdf"
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)

        captions = {
            "gita_english": "📘 Bhagavad Gita (English)",
            "gita_telugu": "📗 భగవద్గీత (Telugu)",
            "mahabharata_english": "📙 Mahabharata (English)",
            "mahabharata_telugu": "📒 మహాభారతం (Telugu)"
        }
        await query.message.reply_document(open(path, "rb"), caption=captions[key])
        os.remove(path)
    except Exception as e:
        await query.message.reply_text(f"⚠️ Failed to download: {e}")
