from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.decorators import log_command
from bot.service.ai import get_chat_completion
from bot.utils.routing import call_fn_from_tool_response
from bot.service.database import db

@log_command
async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("processing message")
    # check if the user is in the db

    user = db.get_user(tg_id=update.effective_user.id)

    if not user:
        await update.message.reply_text("Please start by sending /start")
        return

    messages = [
        {"role": "system", "content": "You are an expert categorizing intentions of users. Do not ask for clarification, just return the intention. if the intention is not clear, ask for clarification."},
        {"role": "user", "content": update.message.text}
    ]
    completion = get_chat_completion(messages)
    print("completion", completion)
    result = call_fn_from_tool_response(completion, user)
    print("result", result)
    if result:
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("I'm sorry, I don't understand that. Please try again.")