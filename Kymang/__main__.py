#Kymang

import importlib
from sys import version as pyver

import asyncio
import os
import sys

from atexit import register

from pyrogram import __version__ as pyrover
from pyrogram import idle
from pyrogram.errors import RPCError
from pyrogram.types import BotCommand

from Kymang import LOOP, Bot, bot, LOGGER
from Kymang.config import LOG_GRP
from Kymang.modules import loadModule
from Kymang.modules.data import get_bot, remove_bot
from Kymang.modules.plernya import *

msg = """
**Berhasil Di Aktifkan**
**Python Version** `{}`
**Pyrogram Version** `{}`
"""

async def auto_restart():
    while not await asyncio.sleep(43200):
        def _():
            os.system(f"kill -9 {os.getpid()} && python3 -m Kymang")
        register(_)
        sys.exit(0)

async def main():
    await bot.start()
    
    for bt in await get_bot():
        b = Bot(**bt)
        try:
            await b.start()
            print(f"{b.me.first_name} [Berhasil Diaktifkan]")
        except RPCError:
            await remove_bot(bt["name"])
            LOGGER("Info").info(f"✅ {bt['name']} Berhasil Dihapus Dari Database")
    for mod in loadModule():
            importlib.reload(importlib.import_module(f"Kymang.modules.{mod}"))
    LOGGER("Info").info(f"[🤖 @{bot.me.first_name} 🤖] [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    await bot.send_message(LOG_GRP, msg.format(pyver.split()[0], pyrover))
    await plernya()
    await auto_restart()
    await idle()


if __name__ == "__main__":
    LOGGER("Info").info("JIKA BUTUH BANTUAN SILAHKAN HUBUNGI @OneWatchBokep")
    LOOP.run_until_complete(main())
