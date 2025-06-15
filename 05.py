

import telebot

API_TOKEN = '7757258327:AAEfSZet5H3k6WJj9iY8wbqepPOUVyj003s'

bot = telebot.TeleBot(API_TOKEN)

@rent_property_3_bot(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я телеграм-бот. Чем могу помочь?")

@rent_property_3_bot(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)


