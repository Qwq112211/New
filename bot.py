from telethon import TelegramClient, events, sync

api_id = '22928444'
api_hash = '972e1a6e4116dbb7964a0f1ed9dc39ed'
bot_token = '6658334394:AAF8c4GXynHpPfiiWRQx2XaL_WbuzrW3vxU'
source_channel = 'UAE1'
destination_channel = 'Отчет'
unwanted_text = 'H.U.G.O PROJECT'
replacement_text = 'TEXTtest'

# Установка соединения с Telegram
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_channel))
async def modify_and_forward(event):
    message_text = event.message.text
    if unwanted_text in message_text:
        modified_text = message_text.replace(unwanted_text, replacement_text)
        await client.send_message(destination_channel, modified_text)

with client:
    client.run_until_disconnected()
