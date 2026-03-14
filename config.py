# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from current directory

TOKEN = os.getenv("BOT_TOKEN")
AI_TOKEN = os.getenv("GEMINI_API_KEY")