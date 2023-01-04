
'''
    Файл main запускає всі інші модулі з папки modules.
'''
import modules.command_start as m_start
import modules.create_bot as m_bot


m_bot.bot.polling(none_stop= True)