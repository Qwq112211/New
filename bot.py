from telegram.ext import Updater, MessageHandler, Filters

# Функция-обработчик для пересылки сообщения во второй канал
def forward_message(update, context):
    # Получаем текст сообщения из первого канала
    original_text = update.message.text
    # Удаляем ненужный текст
    modified_text = original_text.replace("H.U.G.O", "")
    # Пересылаем модифицированный текст во второй канал
    context.bot.send_message(chat_id='-4043745865', text=modified_text)

def main():
    # Установка токена вашего бота
    updater = Updater("6658334394:AAF8c4GXynHpPfiiWRQx2XaL_WbuzrW3vxU", use_context=True)

    # Получаем диспетчер для зарегистрированных обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик для входящих сообщений из первого канала
    dp.add_handler(MessageHandler(Filters.chat("-4045914293") & Filters.text, forward_message))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
