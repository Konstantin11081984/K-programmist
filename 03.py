

import telebot

API_TOKEN = '7757258327:AAEfSZet5H3k6WJj9iY8wbqepPOUVyj003s'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я телеграм-бот. Чем могу помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я простой бот.")

# Токен от BotFather
TOKEN = '7757258327:AAEfSZet5H3k6WJj9iY8wbqepPOUVyj003s'

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Бот запущен...")
app.run_polling()

python 03.py
