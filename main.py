import telebot

bot = telebot.TeleBot("5854397490:AAH498YCJuc1GEVvzLw9XC1NyGsU2AC1fV0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, "Bot by Milana Yergaliyeva")



bot.infinity_polling()