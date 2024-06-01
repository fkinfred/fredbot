#Kymang

import asyncio
import sys

from pyrogram import Client
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.handlers.callback_query_handler import CallbackQueryHandler
from pyromod import listen
from .logging import LOGGER

from Kymang.config import API_HASH, API_ID, BOT_TOKEN, MONGO_URL, KITA

LOOP = asyncio.get_event_loop()

if not API_ID:
    print("API_ID Tidak ada")
    sys.exit()

if not API_HASH:
    print("API_HASH Tidak ada")
    sys.exit()

if not BOT_TOKEN:
    print("BOT_TOKEN Tidak ada")
    sys.exit()

if not MONGO_URL:
    print("MONGO_URL Tidak ada")
    sys.exit()


KITA = KITA

class Bot(Client):
    __module__ = "pyrogram.client"
    _bot = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=None):
        def decorator(func):
            for ub in self._bot:
                ub.add_handler(MessageHandler(func, filters))
            return func

        return decorator

    def on_callback_query(self, filters=None):
        def decorator(func):
            for ub in self._bot:
                ub.add_handler(CallbackQueryHandler(func, filters))
            return func

        return decorator

    async def start(self):
        await super().start()
        if self not in self._bot:
            self._bot.append(self)


bot = Bot(
    name="Botsub",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)
