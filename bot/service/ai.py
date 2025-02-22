import os
from openai import OpenAI
from config import OPENAI_API_KEY
from bot.service.tools import get_tools

def get_openai_client():
    client = OpenAI()
    return client


client = get_openai_client()

def get_chat_completion(messages, model="gpt-4o-mini"):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        tools=get_tools(),
    )
    return chat_completion

