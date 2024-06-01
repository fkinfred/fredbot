import logging
import os
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import *

from Kymang import bot
from Kymang.config import *
from Kymang.modules.data import *

from .start import restart

logs = logging.getLogger(__name__)


@bot.on_message(filters.command(["expired", "info"]))
async def cek_expired(c: Client, m: Message):
    if c.me.id == BOT_ID:
        iya = await seller_info(m.from_user.id)
        if not iya and m.from_user.id not in ADMINS:
            return await m.reply("Kamu Siapa?")
        anu = await cek_prem()
        msg = "**Daftar Bot Fsub Premium**\n\n"
        ang = 0
        for ex in anu:
            try:
                afa = f"`{ex['nama']}` » {ex['aktif']}"
                ang += 1
            except Exception:
                continue
            msg += f"{ang} › {afa}\n"
        await m.reply(msg)
        return
    cek = await cek_owner(c.me.id)
    adm = await admin_info(c.me.id, m.from_user.id)
    for i in cek:
        owner = i["owner"]
    if not adm and m.from_user.id != owner:
        return await m.reply("Kamu Siapa?")
    av = await timer_info(c.me.id)
    time = datetime.now().strftime("%d-%m-%Y")
    if av == time:
        print(f"@{c.me.username} Telah Habis Mohon Tunggu.. Sedang Restart Bot")
        await remove_bot(str(c.me.id))
        os.popen(f"rm {c.me.id}*")
        await restart()
    elif adm or m.from_user.id == owner:
        act = await timer_info(c.me.id)
        await c.send_message(
            m.chat.id,
            f"**Nama** : {c.me.first_name}\n**Id** : `{c.me.id}`\n**Expired** : {act}",
        )
