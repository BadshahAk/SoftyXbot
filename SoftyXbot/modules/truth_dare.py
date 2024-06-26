
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from MukeshAPI import api 
from SoftyXbot import pbot as Softy
@Softy.on_message(filters.command("truth"))
async def truth_(client: Client, message: Message):

    truth =api.truth()
    await message.reply_text(truth)

@Softy.on_message(filters.command("dare"))
async def dare_(client: Client, message: Message):

    dare =api.dare()
    await message.reply_text(dare)


__help__ = """
*ᴛʀᴜᴛʜ & ᴅᴀʀᴇ*
 ❍ /truth  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
 ❍ /dare  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.
"""
__mod_name__ = "🦚Tʀᴜᴛʜ-Dᴀʀᴇ🐣"
