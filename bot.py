import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 28179017
API_HASH = "3eccbcc092d1a95e5c633913bfe0d9e9"
BOT_TOKEN = "8194588818:AAEGAWr2Vqc8tZ_auzoEEjtS5BI4CEruGus"
CHANNEL_ID = -1002605317531  # numeric ID

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    args = message.command
    if len(args) < 2:
        await message.reply("⚠️ কোনো ভিডিও আইডি পাওয়া যায়নি!")
        return

    video_id = int(args[1])
    try:
        msg = await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=video_id,
            protect_content=True
        )
        await asyncio.sleep(20 * 60)
        await msg.delete()
    except Exception as e:
        await message.reply(f"⚠️ ভিডিও পাঠাতে সমস্যা হয়েছে:\n{e}")

@app.on_message(filters.command("genlink") & filters.private)
async def genlink(client, message):
    if len(message.command) < 2:
        await message.reply("❗ লিংক দিন এইভাবে:\n`/genlink https://t.me/c/2605317531/3`")
        return
    try:
        msg_id = int(message.command[1].split("/")[-1])
        link = f"https://t.me/{app.me.username}?start={msg_id}"
        await message.reply(f"🔗 বট লিংক:\n`{link}`")
    except Exception as e:
        await message.reply(f"⚠️ সমস্যা হয়েছে:\n{e}")

app.run()
