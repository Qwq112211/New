      from telegram.ext import Updater, MessageHandler, Filters
   from telegram import ParseMode

   # Замените 'your_token' на ваш токен бота
   updater = Updater(token='6658334394:AAF8c4GXynHpPfiiWRQx2XaL_WbuzrW3vxU', use_context=True)
   dispatcher = updater.dispatcher

   # Функция для обработки входящих сообщений
   def copy_modify_send(update, context):
       # Здесь вы можете добавить логику для удаления части текста
       modified_message_text = update.message.text.replace('H.U.G.O PROJECT', '///')

       # Здесь замените 'destination_channel_id' на ID вашего канала, куда вы хотите отправить модифицированное сообщение
       context.bot.send_message(chat_id='-4043745865', text=modified_message_text, parse_mode=ParseMode.HTML)

   # Добавление обработчика входящих сообщений
   echo_handler = MessageHandler(Filters.chat('-4045914293') & Filters.text, copy_modify_send)
   dispatcher.add_handler(echo_handler)

   # Запуск бота
   updater.start_polling()
   
