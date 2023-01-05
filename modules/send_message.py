'''
    Файл send_message відправляє текстове повідомлення.
'''
import modules.create_bot as m_bot
import modules.create_path_to_file as m_path_to_file
import modules.create_keyboard as m_keyboard

def send_message_user(message):
    if message.text.lower() == 'get message':
        path_file = m_path_to_file.path_to_file("images/1.jpeg")
        m_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Горнятко кави!",
            reply_markup= m_keyboard.keyboard_inlin
        )
    m_bot.bot.register_next_step_handler(message, send_message_user)