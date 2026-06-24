from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TOKEN")

categories = [
    "Аккаунты MEGANZ",
    "Аккаунты герack",
    "VPN Сервисы",
    "Spotify Premium",
    "Игровые аккаунты",
    "Кино-сервисы",
    "Ключи Windows",
    "Аккаунты Findclone",
    "Промокоды / Инвайты",
    "Вторичка",
    "Аккаунты Chat GPT",
    "Образование (Education)",
    "Аккаунты CapCut Pro",
    "Аккаунты Noping/Vpngame",
    "Нейросети",
    "Esim 2GB Интернета",
    "Аккаунты Office 365",
    "Аккаунты ExitLag",
    "Аккаунты Photoshop"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[x] for x in categories]
    await update.message.reply_text(
        "Добро пожаловать в Оптовик!",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in categories:
        await update.message.reply_text(
            f"📦 {text}\n\nСтатус: В наличии\n\nДля заказа напишите администратору."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, catalog))

app.run_polling()
