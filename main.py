
'''
    Файл main запускає всі інші модулі з папки modules.
'''
import modules.command_start as m_start
import modules.create_bot as m_bot
import modules.callback as m_callback


m_bot.bot.polling(none_stop= True)