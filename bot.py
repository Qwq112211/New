from telethon.sync import TelegramClient

# Ваши данные API
api_id = '22928444'
api_hash = '972e1a6e4116dbb7964a0f1ed9dc39ed'
phone = '+6283132117844'
session_file = '82K2'

source_channel_username = '-4045914293'
destination_channel_username = '-4043745865'

from telethon.sync import TelegramClient
import asyncio

async def main():
    client = TelegramClient(session_file, api_id, api_hash)
    await client.start()

    await client.send_message(destination_channel_username, "Бот запущен")

    async for message in client.iter_messages(source_channel_username, limit=10):
        # Обработка текста (удаление ненужной информации)
        processed_text = process_message(message.text)

        # Отправка обработанного текста во второй канал
        await client.send_message(destination_channel_username, processed_text)

    await client.disconnect()

def process_message(text):
   "H.U.G.O PROJEC"
    # Например, удалить ненужные фрагменты, заменить слова и т.д.
    return text

asyncio.run(main())
