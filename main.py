from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    # Run the bot script in a separate process
    os.system("python bot.py")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
