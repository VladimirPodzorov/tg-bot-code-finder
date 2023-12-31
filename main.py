from os import getenv
from dotenv import load_dotenv

import telebot
from data_file import req
from count_check import check


load_dotenv()
token = getenv('TOKEN', None)

bot = telebot.TeleBot(getenv('TOKEN', None))

data = req()


@bot.message_handler(commands=['start'])
def bot_on(message):
    bot.send_message(message.chat.id, 'Привет, юзер!\nВведи код:')


@bot.message_handler(content_types=['text'])
def answer(message):
    code = message.text
    if all(code not in i_code for i_code in data):
        bot.send_message(message.chat.id, 'Нет на складе.')
    for _, value in enumerate(data):
        if code == value[0]:
            try:
                count = check(value[5])
                bot.send_message(message.chat.id, f'{code}=> {value[1]}({count}шт)')
            except IndexError:
                bot.send_message(message.chat.id, f'{code} => {value[1]}(0 шт)')


if __name__ == '__main__':
    bot.polling()
