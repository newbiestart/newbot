import telebot

TOKEN = '8059853294:AAGiOrtO3qjuHrrr8LUlfMASoWlqSDsiVEM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message, "Salom! Men sizning yangi botingizman!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message, message.text)

print("Bot ishga tushdi...")
bot.polling()
