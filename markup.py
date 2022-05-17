import telebot
from telebot import types

buttonUzToRu = "Сум в рубль"
buttonRuToUz = "Рубль в сум"

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row(buttonUzToRu,buttonRuToUz)
