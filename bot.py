from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Telegram bot tokeni
TOKEN = '8059853294:AAGiOrtO3qjuHrrr8LUlfMASoWlqSDsiVEM'

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Salom! Bu mening Telegram botim!')

# Application va handler yaratish
application = Application.builder().token(TOKEN).build()

# Handlerni qo'shish
application.add_handler(CommandHandler("start", start))

# Botni ishga tushurish
application.run_polling()