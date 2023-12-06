
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputChannel, ChannelParticipantsSearch
from telethon.tl.types import UserStatusRecently
import re

# Ваши данные API
api_id = '22928444'
api_hash = '972e1a6e4116dbb7964a0f1ed9dc39ed'
phone = '+6283132117844'
session_file = '82K2'

# Номер канала, откуда нужно брать текст
source_channel = '-4045914293'
# Номер канала, куда нужно отправлять текст
destination_channel = '-4043745865'

# Инициализация клиента
client = TelegramClient(session_file, api_id, api_hash)

async def main():
    await client.start(phone)
    source = await client.get_entity(source_channel)
    destination = await client.get_entity(destination_channel)

    # Получение последних сообщений из первого канала
    messages = await client.get_messages(source, limit=10)

    for message in messages:
        # Обработка текста (удаление ненужной информации)
        processed_text = re.sub('H.U.G.O PROJECT', '', message.text)
        
        # Пересылка обработанного текста во второй канал
        await client(ForwardMessagesRequest(
            from_peer=source,
            id=[message.id],
            to_peer=destination
        ))

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
