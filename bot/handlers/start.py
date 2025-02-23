from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.decorators import log_command
from bot.service.database import db

@log_command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = db.get_user(tg_id=update.effective_user.id)

    if not user:
        print("user not found, creating", update.effective_user.id)
        db.create_user(tg_id=update.effective_user.id)
        await update.message.reply_text("Welcome to the BrainyBeeper!, you are successfully registered.")
        return

    await update.message.reply_text("Welcome to the BrainyBeeper!")