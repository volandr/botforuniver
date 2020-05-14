import telebot
import requests
from bs4 import BeautifulSoup as bs
from telebot import types


bot = telebot.TeleBot('1064508466:AAG2oMd9ZyO4QOwEfNoHyZox98QH2rF5fSs')

headers={'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
base_url = 'https://horoscopes.rambler.ru/'
horoscope=['aries/', 'taurus/', 'gemini/', 'cancer/', 'leo/', 'virgo/', 'libra/',
           'scorpio/', 'sagittarius/', 'capricorn/', 'aquarius/', 'pisces/']


def horoscope_parse(base_url, headers):
    session = requests
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('OK')
        soup = bs(request.content, 'html.parser')
        a_name = soup.find('div', attrs={'class': '_1dQ3'}).span.p.string
        return(a_name)
    else:
            print('Error')


source_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
source_markup.add("Овен","Телец","Близнецы","Рак","Лев","Дева","Весы","Скорпион","Стрелец","Козерог","Водолей","Рыбы")


@bot.message_handler(commands=['start'])  # крч старт это команда которую обрабатывает бот
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери свой знак зодиака внизу', reply_markup=source_markup)


@bot.message_handler(content_types=['text'])  # это он прнимает текст
def send_text(message):
    if message.text == 'Овен':
        urlhoro=base_url+horoscope[0]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Телец':
        urlhoro=base_url+horoscope[1]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Близнецы':
        urlhoro=base_url+horoscope[2]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Рак':
        urlhoro=base_url+horoscope[3]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Лев':
        urlhoro=base_url+horoscope[4]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Дева':
        urlhoro=base_url+horoscope[5]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Весы':
        urlhoro=base_url+horoscope[6]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Скорпион':
        urlhoro=base_url+horoscope[7]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Стрелец':
        urlhoro=base_url+horoscope[8]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Козерог':
        urlhoro=base_url+horoscope[9]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Водолей':
        urlhoro=base_url+horoscope[10]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    elif message.text == 'Рыбы':
        urlhoro=base_url+horoscope[11]
        arg = horoscope_parse(urlhoro,headers)
        bot.send_message(message.chat.id, arg)
    else:
        bot.send_message(message.chat.id, "Я все равно тебя не понимаю, просто тыкни на кнопку внизу")


bot.polling(none_stop=True)
