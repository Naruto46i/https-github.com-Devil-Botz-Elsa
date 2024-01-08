import asyncio
from pyrogram import Client, filters
import openai
from info import OPENAI_API

openai.api_key = OPENAI_API

@Client.on_message(filters.command("openai"))
async def message.content(client, message):
    # Ensure the user has provided a message after the command
    if len(message.content) < 8:  # "openai" is 7 characters long
        await message.channel.send("Please provide a message to send to the OpenAI API.")
        return

    # Extract the user's message
    user_message = message.content[8:]  # Remove the "openai" prefix

    # Generate response with OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=1200,  # Increase the value of max_tokens to allow for longer responses
        temperature=0.6
    )

    # Send the OpenAI response to the user
    await message.channel.send(response["choices"][0]["text"])
