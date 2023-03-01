import os
from dotenv import load_dotenv

import telebot
from telebot import types

from main import insert_table, check_user

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Зарегистрироваться', request_contact=True)
    item2 = types.KeyboardButton('Отправить геоданные', request_location=True)
    markup.add(item, item2)

    text = "Привет это Бот Мамина подруги 😄\n Для получения данных ЗАРЕГИСТРИРУЙТЕСЬ"
    bot.send_message(message.chat.id, text=text, reply_markup=markup)



@bot.message_handler(content_types=['location'])
def location(message: types.Message):
    if message.location is not None:
        print("Location", message.location)




@bot.message_handler(content_types=['contact'])
def contact(message: types.Message):
    if message.contact is not None:
        if check_user(message.chat.id):
            text = "Вы уже зарегистр"
            bot.send_message(message.chat.id, text=text)
        else:
            user = {
                'phone': message.contact.phone_number,
                'first_name': message.contact.first_name,
                'last_name': message.contact.last_name,
                'chat_id': message.chat.id
                }
            insert_table(**user)
            text = "Вы успешно зарегистр"
            bot.send_message(message.chat.id, text=text)


if __name__ == "__main__":
    print('Bot started')
    bot.polling(non_stop=True)









