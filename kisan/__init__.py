import asyncio
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if Config.STRING_SESSION:
   ass=Client(api_id=Config.API_ID,api_hash=Config.API_HASH,session_name=Config.STRING_SESSION)   

if Config.BOT_TOKEN:
   bot=Client(":memory:",api_id=Config.API_ID,api_hash=Config.API_HASH,bot_token=Config.BOT_TOKEN)

if Config.STRING_SESSION:
  @ass.on_message(filters.command("njbanall"))
  async def _(bot: ass, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,msg.chat.id))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")


if Config.STRING_SESSION:
  @ass.on_message(filters.command("mbjanall"))
  async def mban(bot: ass, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.send_message(msg.chat.id, f"/ban {i.user.id}")
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")


if Config.STRING_SESSION:
  @ass.on_message(filters.command(["start"]))
  async def hello(bot: ass, message):
    await message.reply("**- مرحبا بك مالكي بواسطتي يمكن حظر أعضاء الجروبات اول القنوات كل ماعليك رفعي مشرف فقط **\n\n \n\n قم بحظر جميع الاعضاء ما عاد المشرفين والبوتات\n\n حظر_الكل")

if Config.BOT_TOKEN:
  @bot.on_message(filters.command(["حظر_الكل"],""))
  async def _(bot, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,msg.chat.id))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")


if Config.BOT_TOKEN:
  @bot.on_message(filters.command("mbanall"))
  async def mban(bot, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.send_message(msg.chat.id, f"/ban {i.user.id}")
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")


if Config.BOT_TOKEN:
  @bot.on_message(filters.command(["start"]))
  async def hello(bot, message):
    await message.reply_photo(photo=f"https://telegra.ph/file/696aaf7c05b5e0a8aea3e.jpg",
                              caption=f"**اهلين عزيزي اختصاص البوت حظر جميع الأعضاء**!\n\n**لتنصيب بوت خاص بك تواصل مع المطور**\n\nامر الحظر ~ حظر_الكل ",

reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "نبض", url=f"https://t.me/momk03")
                ]
                
           ]
        ),
    )
