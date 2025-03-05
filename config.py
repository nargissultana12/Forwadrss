import os

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID", "-1002398179296"))  # Source channel/group ID
DEST_CHAT_ID = int(os.getenv("DEST_CHAT_ID", "-1002440398569"))  # Destination channel/group ID

TG_WORKERS = int(os.getenv("TG_WORKERS", "4"))  # Number of workers
