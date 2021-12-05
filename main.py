import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message
import os

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

bughunter0 = Client(
    "name",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

@bughunter0.on_message(filters.video & filters.private)
async def mp3(bot, message):
    chat_id=message.chat.id
    file_path = DOWNLOAD_LOCATION + f"{message.chat.id}.mp3"
    txt = await message.reply("Downloading to My server.....")
    await message.download(file_path)  
    await txt.edit("Downloaded File")
    await txt.edit("Converting to mp3")
    await bot.send_audio(chat_id=chat_id,audio=file_path, caption="@BugHunterBots")
    os.remove(file_path)

bughunter0.run()
