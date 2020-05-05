import telebot
import requests
from bs4 import BeautifulSoup as bs

bot = telebot.TeleBot('1064508466:AAG2oMd9ZyO4QOwEfNoHyZox98QH2rF5fSs')


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    global isRunning
    if not isRunning:
        chat_id = message.chat.id
        text = message.text
        msg = bot.send_message(chat_id, 'Сколько вам лет?')
        bot.register_next_step_handler(msg, askAge) #askSource
        isRunning = True

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите ещё раз.')
        bot.register_next_step_handler(msg, askAge) #askSource
        return
    msg = bot.send_message(chat_id, 'Спасибо, я запомнил что вам ' + text + ' лет.')
    isRunning = False

bot.polling(none_stop=True)