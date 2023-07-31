from aiogram import *
from aiogram.types.web_app_info import WebAppInfo

api_token = Bot('6396588812:AAHZf43Ka83fTEp2oo2uyfLb5l0kmknIf_M')
dispatcher = Dispatcher(api_token)


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web app (alpha)', web_app=WebAppInfo(url='https://htmlpreview.github.io/?https://github.com/vladcelona/Imshop_main/blob/master/web_files/landing.html')),
               types.KeyboardButton('Imshop.ai contacts', web_app=WebAppInfo(url='https://imshop.io/contacts')),)
    await message.answer('*Imshop Test bot*\n\nChoose the needed button to test the bot', reply_markup=markup, parse_mode="markdownv2")

executor.start_polling(dispatcher)
