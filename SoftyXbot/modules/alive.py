import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from SoftyXbot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

PHOTO = [
    "https://graph.org/file/eff568bdd6939e67e7f72.jpg",
    "https://graph.org/file/a6f730b2b3c8f82a8e387.jpg",
    "https://graph.org/file/c67295736df4a8d24c576.jpg",
    "https://graph.org/file/9202a1221c6b9755da520.jpg",
    "https://graph.org/file/de2bf742ce12d4ac49f86.jpg",
]

Softy = [
    [
        InlineKeyboardButton(text="ɴᴏᴏʙ", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="✿α∂∂ мє ιη уσυ ¢нαт✿",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker(
        "CAACAgUAAyEFAASCvXg4AAMdZmai16Kk9TqpsFeP3U2mXfWWspEAAsoMAAJVYCBXO8ubTkCCvIIeBA"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        START_IMG,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{BOT_NAME}](f"t.me/{BOT_USERNAME}")』**
   ╔━━❖❖🖤❖❖━━╗
◆💠◈ [Legend](https://t.me/King_X_Legend)◈💠◆
╚━━❖❖🖤❖❖━━╝""",
        reply_markup=InlineKeyboardMarkup(Softy)
    )
