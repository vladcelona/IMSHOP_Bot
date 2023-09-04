from additional_files import *


# Information necessary for the bot
token = sys.argv[1]
app_link = sys.argv[2]
contacts_link = sys.argv[3]
provider_token = sys.argv[4]

# The analog of code above
# token, app_link, contacts_link, provider_token = [elem for elem in sys.argv[1:5]]

# Creating bot
bot = telebot.TeleBot(token)


# Getting InlineKeyboardMarkup
def get_markup() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2

    markup.add(
        types.InlineKeyboardButton('Каталог', web_app=types.WebAppInfo(url=app_link)),
        types.InlineKeyboardButton('Контакты', web_app=types.WebAppInfo(url=contacts_link)),
        types.InlineKeyboardButton('Избранное', callback_data='favorites'),
        types.InlineKeyboardButton('Корзина', callback_data=f'cart'),
        types.InlineKeyboardButton('Заказы', callback_data=f'orders'),
        types.InlineKeyboardButton('Покупки', callback_data=f'purchases')
    )

    return markup


# Section of command handlers


# Handles /start command
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, f'Добро пожаловать в бета версию бота для IMSHOP IO, {message.chat.username}\n'
                                      '*Выберите одну из кнопок ниже, чтобы её протестировать*',
                     reply_markup=get_markup(), parse_mode='markdownv2')


# Handles /menu command
@bot.message_handler(commands=['menu'])
def menu(message: types.Message):
    bot.send_message(message.chat.id, '*Выберите одну из кнопок ниже, чтобы её протестировать*',
                     reply_markup=get_markup(), parse_mode='markdownv2')


# User's favorites callback query handler
@bot.callback_query_handler(func=lambda callback: True)
def callback_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    orders_data = get_orders(user_id=str(user_id))
    orders_status = get_orders_status(user_id=str(user_id))

    inline_orders_list = [types.InlineKeyboardButton(key, callback_data=f'order_0_{key}')
                          for key, value in orders_data.items() if orders_status[key]['status'] == '0']
    inline_purchases_list = [types.InlineKeyboardButton(key, callback_data=f'order_1_{key}')
                                   for key, value in orders_data.items() if orders_status[key]['status'] == '1']

    try:
        if callback.data == 'favorites':
            pass
        elif callback.data == 'cart':
            pass
        elif callback.data == 'orders':
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(*inline_orders_list)
            markup.row(
                types.InlineKeyboardButton('<<', callback_data='back'),
                types.InlineKeyboardButton('>>', callback_data='forward')
            )

            bot.edit_message_text('*Список ваших заказов*', chat_id, message_id, reply_markup=markup,
                                  parse_mode='markdownv2')
        elif callback.data == 'back':
            bot.edit_message_text('*Выберите одну из кнопок ниже, чтобы её протестировать*', chat_id,
                                  message_id, reply_markup=get_markup(), parse_mode='markdownv2')
        elif callback.data == 'forward':
            inline_buttons_list = [types.InlineKeyboardButton('<<', callback_data='back'),
                                   types.InlineKeyboardButton('>>', callback_data='forward')]

            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(*inline_buttons_list)

            bot.edit_message_text('Вы нажали на кнопку с callback data _forward_:',
                                  chat_id, message_id, reply_markup=markup, parse_mode='markdownv2')
        elif callback.data == 'purchases':
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(*inline_purchases_list)
            markup.row(
                types.InlineKeyboardButton('<<', callback_data='back'),
                types.InlineKeyboardButton('>>', callback_data='forward')
            )

            bot.edit_message_text('*Список ваших покупок*', chat_id, message_id, reply_markup=markup,
                                  parse_mode='markdownv2')
        elif 'order_0_' in callback.data:
            order_id = callback.data.replace("order_0_", "")
            order_data = get_orders(user_id=str(user_id))[order_id]
            label_prices = [types.LabeledPrice(f'{value["name"]} x{value["quantity"]}',
                                               int(value["price"]) * int(value["quantity"]))
                            for key, value in order_data.items()]

            bot.delete_message(chat_id, message_id)
            bot.send_invoice(chat_id, f'Заказ #{order_id}',
                             'Завершите процедуру покупки', order_id, provider_token, 'RUB',
                             label_prices, need_name=True, need_shipping_address=True, need_phone_number=True,
                             need_email=True,
                             photo_url='https://github.com/vladcelona/Imshop_main/blob/master/image.png?raw=true',
                             photo_width=200, photo_height=60, is_flexible=True,)
        elif 'order_1_' in callback.data:

            inline_buttons_list = [types.InlineKeyboardButton('<<', callback_data='back'),
                                   types.InlineKeyboardButton('>>', callback_data='forward')]

            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(*inline_buttons_list)

            bot.edit_message_text('Информация о покупке:', chat_id, message_id, reply_markup=markup,
                                  parse_mode='markdownv2')
        else:
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(types.InlineKeyboardButton('Повторить', callback_data='back'),)

            bot.edit_message_text('Что-то пошло не так при обработке запроса. Пожалуйста, повторите ваш запрос',
                                  chat_id, message_id, reply_markup=markup)

    except Exception:
        orders_data = get_orders(user_id=str(user_id))
        print(orders_data)
        bot.send_message(chat_id, 'Что-то пошло не так. Повторите Ваш запрос')


# Handles shipping query
@bot.shipping_query_handler(func=lambda query: True)
def shipping_handler(shipping_query: types.ShippingQuery):
    global moscow_options, regions_options

    orders_status = get_orders_status(str(shipping_query.from_user.id))[shipping_query.invoice_payload]

    if shipping_query.shipping_address.city.lower() in ['москва', 'moscow']:
        bot.answer_shipping_query(shipping_query.id, True, moscow_options,
                                  error_message='Ой! Мы не смогли получить данные о доступных вариантах получения '
                                                'вашего заказа! Просим извинения за временные неудобства!')
    elif shipping_query.shipping_address.city.lower() in orders_status['available'] \
            and shipping_query.shipping_address.city.lower() != '':
        bot.answer_shipping_query(shipping_query.id, True, regions_options,
                                  error_message='Ой! Мы не смогли получить данные о доступных вариантах получения '
                                                'вашего заказа! Просим извинения за временные неудобства!')
    else:
        bot.answer_shipping_query(shipping_query.id, False, error_message='В ваш населённый пункт доставка выбранных '
                                                                          'товаров не доступна! Просим извинения за '
                                                                          'доставленные неудобства!')


# Handles pre-checkout query. If something goes wrong, it shows error message
@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message='Мы не смогли произвести оплату! Пожалуйста, введите данные ещё раз!')


# Handles successful payment query. The function shows short information about completed payment
@bot.message_handler(content_types=['successful_payment'])
def got_payment(message: types.Message):
    bot.send_message(message.chat.id, f'Спасибо за оплату! Вот данные вашей покупки:\n'
                                      f'Сумма: {format(message.successful_payment.total_amount / 100, ".2f")} '
                                      f'{message.successful_payment.currency}\n'
                                      f'ID оплаты (Банк): {message.successful_payment.provider_payment_charge_id}\n'
                                      f'ID оплаты (Telegram): {message.successful_payment.telegram_payment_charge_id}')

                     # 'Спасибо за оплату! Вот данные покупки: `{} {}`'.format(
                     #     message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     # parse_mode='Markdown')


if __name__ == '__main__':
    bot.infinity_polling(timeout=43200)
