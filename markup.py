import telebot
from telebot import types

rub = 'Рубль'
usd = 'Доллар'
cancel = 'Назад'

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row(rub,usd)

buttonUzToRub = "Сум в рубль"
buttonRubToUz = "Рубль в сум"

menuRub = types.ReplyKeyboardMarkup(resize_keyboard=True)
menuRub.row(buttonUzToRub,buttonRubToUz)
menuRub.row(cancel)

buttonUzToUsd = "Сум в доллар"
buttonUsdToUz = "Доллар в сум"

menuUsd = types.ReplyKeyboardMarkup(resize_keyboard=True)
menuUsd.row(buttonUzToUsd,buttonUsdToUz)
menuUsd.row(cancel)

menuCancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
menuCancel.row(cencel)
