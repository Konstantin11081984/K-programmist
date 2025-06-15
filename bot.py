from flask import Flask, request
import telebot
import os

TOKEN = '7757258327:AAEfSZet5H3k6WJj9iY8wbqepPOUVyj003s'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Render даёт домен вроде: https://your-app-name.onrender.com
WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'your-app-name.onrender.com')}/{TOKEN}"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет с Render + webhook!")

@app.route('/' + TOKEN, methods=['POST'])
def receive_update():
    json_str = request.stream.read().decode("utf-8")
    print(f"Получен апдейт: {json_str}")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def index():
    return 'Бот работает на Render!'

# Устанавливаем вебхук при запуске
@app.before_first_request
def setup_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

# Старт сервера Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 10000)))
