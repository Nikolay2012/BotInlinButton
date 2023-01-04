'''
    Файл create_button створює кнопку для клавіатури.
'''
import telebot

button = telebot.types.KeyboardButton("Get Message")

button_inlin_1 = telebot.types.InlineKeyboardButton("Перейти до сайту!", callback_data="bt1")

button_inlin_2 = telebot.types.InlineKeyboardButton("Купити!", callback_data= "bt2")
