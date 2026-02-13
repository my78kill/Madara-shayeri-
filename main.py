import os
import requests
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = "https://fast-dev-apis.vercel.app/shayari"

app = Flask(__name__)

telegram_app = Application.builder().token(BOT_TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌸 Welcome to Shayari Bot 🌸\n\n"
        "👉 /shayari likho aur ek nayi shayari pao 💖"
    )


async def shayari(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(API_URL, timeout=10)
        data = response.json()

        shayari_text = (
            data.get("shayari")
            or data.get("data")
            or data.get("quote")
            or "❌ Shayari nahi mil payi"
        )

        await update.message.reply_text(f"✨ Shayari ✨\n\n{shayari_text}")

    except Exception:
        await update.message.reply_text(
            "⚠️ API error aa gaya, baad me try karo."
        )


telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("shayari", shayari))


@app.route("/", methods=["GET"])
def home():
    return "Shayari Bot Running Successfully 🚀"


@app.route(f"/{BOT_TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    await telegram_app.process_update(update)
    return "ok"


if __name__ == "__main__":
    telegram_app.initialize()
    telegram_app.bot.set_webhook(
        url=f"https://madara-shayeri.onrender.com/{BOT_TOKEN}"
    )

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
