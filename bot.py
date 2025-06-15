
import os
import telebot
import time
from threading import Thread

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

users = set()

@bot.message_handler(commands=["start"])
def start_message(message):
    users.add(message.chat.id)
    bot.send_message(message.chat.id, "Привет! Я бот Box2Box. Жди прогнозы ежедневно :)")

def send_predictions():
    while True:
        for chat_id in users:
            try:
                bot.send_message(chat_id, "**⚽ Прогноз на футбол**\nМатч: Норвегия – Косово\nСтавка: Победа Норвегии с форой -1\nКоэффициент: 1.70\n\n📋 Анализ: Норвегия дома играет мощно. Косово слабее. Победа в 1-2 мяча — логично.")
            except Exception as e:
                print(f"Ошибка отправки в {chat_id}: {e}")
        time.sleep(43200)

Thread(target=send_predictions).start()
bot.polling()
