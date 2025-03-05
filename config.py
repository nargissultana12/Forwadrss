import os

API_ID = int(os.getenv("API_ID", "19977673"))
API_HASH = os.getenv("API_HASH", "f75386c7aab88e2ad9b5de220fc0ceb4")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7601241825:AAGM8N5ea6bh-2sEQRV-0NqtTJ6fvbE1b0g")

SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID", "-1002398179296"))  # Source channel/group ID
DEST_CHAT_ID = int(os.getenv("DEST_CHAT_ID", "-1002477240145"))  # Destination channel/group ID

TG_WORKERS = int(os.getenv("TG_WORKERS", "4"))  # Number of workers
