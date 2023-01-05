import modules.create_bot as m_bot

@m_bot.bot.callback_query_handler(func= lambda callback: callback.data)

def check_callback(callback):
    if callback.data == "bt1":
        m_bot.bot.send_message(
            callback.message.chat.id,
            "Hello, user!"
        )