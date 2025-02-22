import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN, USE_DATABASE
from bot.handlers.start import start
from bot.handlers.list_todos import list_todos
from bot.handlers.process_message import process_message

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("list", list_todos))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    if USE_DATABASE:
        from database.models import init_db
        init_db()
        logging.info("Database initialized")
    else:
        logging.info("Running without database")

    application.run_polling()

if __name__ == '__main__':
    main()