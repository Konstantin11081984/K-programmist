import telebot

API_TOKEN = '7757258327:AAEfSZet5H3k6WJj9iY8wbqepPOUVyj003s'

bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я телеграм-бот. Чем могу помочь?")

# Ответ на любое другое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
