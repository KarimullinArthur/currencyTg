import telebot
from func import * 
import markup
from config import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='start')
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'Дарова',reply_markup=markup.menu)

@bot.message_handler(content_types='text')
def menu(message):
    chat_id = message.chat.id
    text = message.text

    if text == markup.buttonRuToUz:
        bot.send_message(chat_id,message)

    elif text == markup.buttonUzToRu:
        bot.send_message(chat_id,message)

print('Run!')
bot.infinity_polling()
