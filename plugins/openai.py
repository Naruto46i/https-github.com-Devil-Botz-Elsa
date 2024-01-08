import asyncio
from pyrogram import Client, filters
import openai
from info import OPENAI_API

openai.api_key = OPENAI_API

@Client.on_message(filters.command('openai'))
async def openai_command(client, message):
    if not message.text:
        await client.send_message(message.chat.id, "ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜʀ ʀᴇǫᴜᴇsᴛ ")
        return

    try:
        user_message = message.content[8:]  # Remove the "openai" prefix    
        response = openai.ChatCompletion.create(
            messages=[
                {"role": "user", "content": user_message}
            ],
            model="gpt-3.5-turbo",
            max_tokens=1200,  # Increase the value of max_tokens to allow for longer responses
            temperature=0.6            
        )
        await message.reply_text(response["choices"][0]["text"])
