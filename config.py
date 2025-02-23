import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
USE_DATABASE = os.getenv("USE_DATABASE", "False").lower() == "true"
DATABASE_URL = os.getenv("DATABASE_URL") if USE_DATABASE else None
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")