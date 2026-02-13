from flask import Flask
import threading
import bot
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Shayari Bot Running Successfully!"

def start_bot():
    bot.run_bot()

threading.Thread(target=start_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
