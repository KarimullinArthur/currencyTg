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

    if text == markup.rub:
        msg = bot.send_message(chat_id,getRate('RUB'),reply_markup=markup.menuRub)
        bot.register_next_step_handler(msg,menuRub)

    elif text == markup.usd:
        msg = bot.send_message(chat_id,getRate('USD'),reply_markup=markup.menuUsd)

        bot.register_next_step_handler(msg,menuUsd)

def menuRub(message):
    chat_id = message.chat.id
    text = message.text

    if text == markup.buttonUzToRub or text == markup.buttonUzToRub:
        pass

    elif text == markup.cancel:
        msg = bot.send_message(chat_id,text,reply_markup=markup.menu)
        bot.register_next_step_handler(msg,menu)

def menuUsd(message):
    chat_id = message.chat.id
    text = message.text

    if text == markup.buttonUzToUsd or text == markup.buttonUsdToUz:
        msg = bot.send_message(chat_id,"Введите сумму",reply_markup=markup.menuCencel)
        bot.register_next_step_handler(msg,amount) 

    elif text == markup.cancel:
        msg = bot.send_message(chat_id,text,reply_markup=markup.menuCencel)
        bot.register_next_step_handler(msg,menu)

def amount(message):
    chat_id = message.chat.id
    text = message.text

    

print('Run!')
bot.infinity_polling()
