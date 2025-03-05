from pyrogram import Client, filters
import re
import config
from pyrogram.enums import ParseMode
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Run Flask in a separate thread
threading.Thread(target=run_flask, daemon=True).start()

# Regex pattern for Gofile.io links
GOFILE_PATTERN = re.compile(r"https?://(?:www\.)?gofile\.io/\S+")

def start_forwarding(app: Client):
    @app.on_message(filters.chat(config.SOURCE_CHAT_ID))
    async def forward_links(client, message):
        text = message.text or message.caption
        if text:
            gofile_links = GOFILE_PATTERN.findall(text)

            # Send each Gofile link in a separate post
            for link in gofile_links:
                formatted_text = f"/l {link}\n<b>Tag:</b> <code>@Mr_official_300</code> <code>2142536515</code>"
                await client.send_message(config.DEST_CHAT_ID, formatted_text, parse_mode=ParseMode.HTML)

    print("Forwarding setup complete!")