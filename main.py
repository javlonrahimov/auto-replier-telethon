from telethon import TelegramClient, events

api_id = YOUR_API_ID
api_hash = 'your_api_hash'

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def my_event_handler(event):
    if 'general kenobi' == event.raw_text.lower().strip():
        await event.reply('You are a bold one')
    if "Back away, I'll deal with this jedi slime myself" == event.raw_text.strip():
        await event.reply('Your move')
        
client.start()
client.run_until_disconnected()
