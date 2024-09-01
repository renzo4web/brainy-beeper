from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.decorators import log_command

@log_command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Telegram Bot Starter Kit!")