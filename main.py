from pyrogram import Client, filters
from environs import Env

env = Env()
env.read_env()

app = Client("my_account", api_id=env("API_ID"), api_hash=env("API_HASH"))


@app.on_message(filters.text & filters.incoming & filters.private)
async def echo(client, message):
    if message.text.lower() in ['Hello', 'hello', 'helo', 'Helo']:
        await message.reply_text("Hello")
        await app.read_chat_history(message.from_user.id, message.id)


app.run()
