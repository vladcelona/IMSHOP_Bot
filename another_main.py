import telebot
from telebot import types
import pandas
from datetime import date as month_day
from datetime import datetime
import time
import sys
import os


api_token = '6396588812:AAHZf43Ka83fTEp2oo2uyfLb5l0kmknIf_M'
bot = telebot.TeleBot(api_token)


# Handles /start command
@bot.message_handler(commands=['start'])
def start(message):
    print('/start', message.chat.id, message.chat.username, end=' ')
    msg = f'/start {message.chat.id} {message.chat.username}'
    bot.send_message(message.chat.id, f'Welcome, {message.chat.first_name} {message.chat.last_name}!')


# Handles /test_shop command
@bot.message_handler(commands=['test_shop'])
def test_shop(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(types.InlineKeyboardButton('Корзина', callback_data=f"Cart {message.chat.username}"),
               types.InlineKeyboardButton('Избранное', callback_data=f"Favorites {message.chat.username}"),
               types.InlineKeyboardButton('Профиль', callback_data=f"Profile {message.chat.username}"),
               types.InlineKeyboardButton('Каталог', callback_data=f"Catalog {message.chat.username}"))

    bot.send_message(message.chat.id, '*Выберите нужный раздел*\n\nНажмите на определённую кнопку '
                                      'чтобы открыть нужный Вам раздел', reply_markup=markup, parse_mode='markdownv2')


@bot.callback_query_handler(func=lambda callback: True)
def test_shop_data(callback):

    markup = types.InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(types.InlineKeyboardButton('Корзина', callback_data=f"Cart {callback.message.chat.username}"),
               types.InlineKeyboardButton('Избранное', callback_data=f"Favorites {callback.message.chat.username}"),
               types.InlineKeyboardButton('Профиль', callback_data=f"Profile {callback.message.chat.username}"),
               types.InlineKeyboardButton('Каталог', callback_data=f"Catalog {callback.message.chat.username}"))

    # print(callback.data.split())
    username = callback.data.split()[1]

    if callback.data.split()[0] == 'Catalog':
        pass


if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling(timeout=43200)