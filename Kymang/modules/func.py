#Kymang

import asyncio
import base64
import re

from pyrogram import enums, filters
from pyrogram.errors import FloodWait, UserNotParticipant

from Kymang.config import *
from Kymang.modules.data import *


async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    return (base64_bytes.decode("ascii")).strip("=")


async def decode(base64_string):
    base64_string = base64_string.strip("=")
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes)
    return string_bytes.decode("ascii")


async def is_subscribed(filter, c, m):
    if c.me.id == BOT_ID:
        return True
    for ix in await cek_owner(c.me.id):
        admin = ix["owner"]
    links = [x["sub"] for x in await get_subs(c.me.id)] if await get_subs(c.me.id) else []
    if not links:
        return False
    user_id = m.from_user.id
    adm = await admin_info(c.me.id, user_id)
    if user_id == int(admin):
        return True
    if adm:
        return True
    try:
        for link in links:
            member = await c.get_chat_member(link, user_id)
    except UserNotParticipant:
        return False

    return member.status in [
        enums.ChatMemberStatus.OWNER,
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.MEMBER,
    ]


async def get_messages(c, message_ids):
    messages = []
    total_messages = 0
    for ix in await cek_owner(c.me.id):
        db = ix["channel"]
    while total_messages != len(message_ids):
        temb_ids = message_ids[total_messages : total_messages + 200]
        try:
            msgs = await c.get_messages(db, temb_ids)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await c.get_messages(db, temb_ids)
        except BaseException:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages


async def get_message_id(c, m):
    for ix in await cek_owner(c.me.id):
        db = ix["channel"]
    if m.forward_from_chat and m.forward_from_chat.id == db:
        return m.forward_from_message_id
    elif m.forward_from_chat or m.forward_sender_name or not m.text:
        return 0
    else:
        pattern = "https://t.me/(?:c/)?(.*)/(\\d+)"
        matches = re.match(pattern, m.text)
        if not matches:
            return 0
        channel_id = matches[1]
        msg_id = int(matches[2])
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(db):
                return msg_id


subcribe = filters.create(is_subscribed)
