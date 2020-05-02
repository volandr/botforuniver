import telebot
import requests
from bs4 import BeautifulSoup as bs

bot = telebot.TeleBot('1064508466:AAG2oMd9ZyO4QOwEfNoHyZox98QH2rF5fSs')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')


bot.polling()