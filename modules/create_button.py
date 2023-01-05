'''
    Файл create_button створює кнопку для клавіатури.
'''
import telebot
import modules.send_message as m_mes

button = telebot.types.KeyboardButton("Get Message")

button_inlin_1 = telebot.types.InlineKeyboardButton(
    "Перейти до сайту!",
    callback_data = "bt1",
    # url= "https://github.com/Nikolay2012/BotInlinButton",
)

button_inlin_2 = telebot.types.InlineKeyboardButton("Купити!", callback_data= "bt2")
