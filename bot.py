from telethon.sync import TelegramClient

# Ваши данные API
api_id = '22928444'
api_hash = '972e1a6e4116dbb7964a0f1ed9dc39ed'
phone = '+6283132117844'
session_file = '82K2'

source_channel_username = 'source_channel_username'
destination_channel_username = 'destination_channel_username'

with TelegramClient(session_file, api_id, api_hash) as client:
    client.send_message(destination_channel_username, "Бот запущен")

    async for message in client.iter_messages(source_channel_username, limit=10):
        # Обработка текста (удаление ненужной информации)
        processed_text = process_message(message.text)

        # Отправка обработанного текста во второй канал
        await client.send_message(destination_channel_username, processed_text)

def process_message(text):
    # Здесь вы можете добавить логику для обработки текста
    # Например, удалить ненужные фрагменты, заменить слова и т.д.
    return text
