'''
    Файл create_keyboard створює клавіатуру.
'''
import telebot
import modules.create_button as m_button

keyboard = telebot.types.ReplyKeyboardMarkup()

keyboard.add(m_button.button)

keyboard_inlin = telebot.types.InlineKeyboardMarkup()
# keyboard_inlin.add(m_button.button_inlin_1, m_button.button_inlin_2)
keyboard_inlin.add(m_button.button_inlin_1)
keyboard_inlin.add(m_button.button_inlin_2)