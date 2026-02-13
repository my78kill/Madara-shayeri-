from pyrogram import Client, filters
import requests
import threading

API_ID = int("36522229")
API_HASH = "7f27443617af60bcb0e23f7147d3eaf9"
BOT_TOKEN = "8564296670:AAH0DnZZXiA8i76OerGIGkdepYSHIAqSYXE"

app = Client(
    "shayari-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
def start(_, message):
    message.reply_text("💫 Shayari Bot Ready 💫\n\n👉 /shayari bhejo aur nayi shayari pao ❤️")

@app.on_message(filters.command("shayari"))
def shayari(_, message):
    try:
        r = requests.get("https://fast-dev-apis.vercel.app/shayari")
        data = r.json()
        message.reply_text(f"✨ Shayari ✨\n\n{data['shayari']}")
    except:
        message.reply_text("⚠️ API Error")

def run_bot():
    app.run()

if __name__ == "__main__":
    run_bot()
