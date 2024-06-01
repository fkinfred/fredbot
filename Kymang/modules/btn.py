#Kymang


from pyrogram.types import InlineKeyboardButton

from Kymang.modules.data import *


async def button_pas_pertama(c):
    temp = []
    links = []
    new_keyboard = []
    for x in await get_subs(c.me.id):
        info = await c.get_chat(x["sub"])
        try:
            link = info.invite_link
        except:
            link = await c.export_chat_invite_link(x["sub"])
        links.append(link)
    keyboard = [InlineKeyboardButton("Channel", url=h) for h in links]
    for i, board in enumerate(keyboard, start=1):
        temp.append(board)
        if i % 2 == 0:
            new_keyboard.append(temp)
            temp = []
        if i == len(keyboard):
            new_keyboard.append(temp)
    try:
        new_keyboard.append(
            [  
                InlineKeyboardButton(
                        text="Help", callback_data="cb_help"
                ),
                InlineKeyboardButton(
                        text="Close", callback_data="close",
                )
            ]
        )
    except IndexError:
        pass
    return new_keyboard



async def force_button(c, m):
    temp = []
    new_keyboard = []
    links = []
    subs = await get_subs(c.me.id)
    if subs is None:
        return []
    for x in subs:
        info = await c.get_chat(x["sub"])
        try:
            link = info.invite_link
        except:
            link = await c.export_chat_invite_link(x["sub"])
        links.append(link)
    keyboard = [InlineKeyboardButton("Join Dulu", url=h) for h in links]
    for i, board in enumerate(keyboard, start=1):
        temp.append(board)
        if i % 2 == 0:
            new_keyboard.append(temp)
            temp = []
        if i == len(keyboard):
            new_keyboard.append(temp)
    try:
        new_keyboard.append(
            [
                InlineKeyboardButton(
                    "Coba Lagi",
                    url=f"https://t.me/{c.me.username}?start={m.command[1]}",
                )
            ]
        )
    except IndexError:
        pass
    return new_keyboard

