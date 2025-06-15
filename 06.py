import telebot

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # вставь свой токен

bot = telebot.TeleBot(API_TOKEN)

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я телеграм-бот. Чем могу помочь?")

# Ответ на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск
