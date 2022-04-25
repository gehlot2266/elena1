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


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**Thanks for adding me in your Group ❤️ Now promote me as administrator In this Chat with needed powers otherwise I am not able to work properly !!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Developer", url=f"https://t.me/Innocent_Gaurav01")
                ],[
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/Funtwenty_4"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/Funtwenty_4")
                  ],
            ]
        ),
    )
