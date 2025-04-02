import os
import telebot

TOKEN = os.environ.get('TOKEN', '8059853294:AAGiOrtO3qjuHrrr8LUlfMASoWlqSDsiVEM')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sizning yangi botingizman!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot ishga tushdi...")
bot.infinity_polling()