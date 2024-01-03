from info import SUPPORT_CHAT_ID, SUPPORT_LINK, OPENAI_API
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai

openai.api_key = OPENAI_API

@Client.on_message(filters.command("openai"))
async def ask_question(client, message):
    if message.chat.id != SUPPORT_CHAT_ID:
        btn = [[
            InlineKeyboardButton('Support Group', url=SUPPORT_LINK)
        ]]
        return await message.reply("This command only working in support group.", reply_markup=InlineKeyboardMarkup(btn))
    try:
        text = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Give an input!")
    msg = await message.reply("Searching...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text}
            ],
            max_tokens=1200,
            temperature=0.6
        )
        await msg.edit(f"User: {message.from_user.mention}\nQuery: <code>{text}</code>\n\nResults:\n\n<code>{response.choices[0].message.content}</code>")
    except Exception as e:
        await msg.edit(f'Error - <code>{e}</code>')
