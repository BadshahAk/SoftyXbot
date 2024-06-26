

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
import aiohttp

from SoftyXbot import pbot as Softy
from SoftyXbot.modules.disable import DisableAbleCommandHandler


async def ud(client: Client, message: Message):
    text = message.text[len("/ud "):]
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.urbandictionary.com/v0/define?term={text}") as resp:
            results = await resp.json()
            try:
                reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
            except (KeyError, IndexError):
                reply_text = "No results found."
            
            await message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


@Softy.on_message(filters.command("ud"))
async def ud_command(client: Client, message: Message):
    await ud(client, message)


__help__ = """
» /ud (text) *:* sᴇᴀʀᴄʜs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴜʀʙᴀɴ ᴅɪᴄᴛɪᴏɴᴀʀʏ ᴀɴᴅ sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
"""
__mod_name__ = "🦚Uʀʙᴀɴ🐣"


