# handlers/register.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.db_utils import get_db_client
from datetime import datetime

async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not user:
        await update.message.reply_text("Could not detect your user. Try again.")
        return
    uid = user.id
    name = user.full_name
    timestamp = datetime.utcnow()

    client = get_db_client()
    db = client.get_database()  # default DB from URI or specified in get_db_client
    users = db.get_collection("users")

    existing = users.find_one({"telegram_id": uid})
    if existing:
        await update.message.reply_text("You are already registered. ✅")
        return

    users.insert_one({
        "telegram_id": uid,
        "name": name,
        "registered_at": timestamp
    })
    await update.message.reply_text("Registration successful! 🎉")
