import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**Hello, Welcome {message.from_user.mention()}\n
I am powerful easy to use TeleGram Super Bot. I can play high quality and unbreakable music in your group voice chat. Just add me and promote with needed powers.\n
Use Inline buttons for more !!
For Help : @StrayCoderSupport**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✚ Add me to your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("👤 Bot Owner", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("⚙️ Developer", url=f"https://t.me/Innocent_Gaurav01")
                ],[
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/Funtwenty_4"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/Funtwenty_4")
                ],[
                    InlineKeyboardButton("🔍 How To Use? Commands", callback_data="cb_cmd")
                ],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**× I am Alive ×**\n\n@Funtwenty_4 📡")


@Client.on_message(command(["repo"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("`Click on the Button given below to Get the Bot Source Code.`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Developer", url=f"https://t.me/Funtwenty_4")
                ]
            ]
        ),
    )
