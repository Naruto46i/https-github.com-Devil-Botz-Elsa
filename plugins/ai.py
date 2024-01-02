from pyrogram import Client, filters
from pyrogram.types import Message
import openai 
from info import API_ID, API_HASH, BOT_TOKEN, OPENAI_API, PORT

openai.api_key = OPENAI_API

@Client.on_message(filters.command("ask"))
async def ask_question(client, message):
    if len(OPENAI_API) == 0:
        return await message.reply("OPENAI_API is empty")

    try:
        text = message.text.split(" ", 1)[1]

        response = ai_client.chat.completions.create(
            messages=[
                {"role": "user", "content": text}
            ],
            model="gpt-3.5-turbo"
        )
        await msg.edit(f"User: {message.from_user.mention}\nQuery: <code>{text}</code>\n\nResults:\n\n<code>{response.choices[0].message.content}</code>")
    except Exception as e:
        await msg.edit(f'Error - <code>{e}</code>')
