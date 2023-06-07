# NProjecst
# Original Code By : @mrismanaziz (PyroMan-UserBot)
# Copyright (C) 2023 NK-Userbot

import os

from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import *

from config import CMD_HANDLER as cmd
from NProjects.helpers.tools import get_arg
from NProjects import *

from .help import add_command_help

@Client.on_message(filters.command("ambil", cmd) & filters.me)
async def colong_media(client: Client, message: Message):
    await message.edit("Processing...")
    link = get_arg(message)
    msg_id = int(link.split("/")[-1])
    if "t.me/c/" in link:
        try:
            chat = int("-100" + str(link.split("/")[-2]))
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Sepertinya terjadi kesalahan")
    else:
        try:
            chat = str(link.split("/")[-2])
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Sepertinya terjadi kesalahan")
    # if dia.caption == None:
        # anjing = dia.caption or None
        # anjing = "Uploaded by NK Userbot"
    # else:
        # anjing = dia.caption
    anjing = "Uploaded by NK Userbot"

    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Sepertinya terjadi kesalahan")

@Client.on_message(filters.command("copy", cmd) & filters.me)
async def copy_media(client: Client, message: Message):
    dia = message.reply_to_message
    user_id = client.me.id
    chatlog = BOTLOG_CHATID
    if not dia:
        await message.edit("Mohon balas ke media")
    anjing = dia.caption or None
    await message.edit("Processing...")
    if dia.text:
        await dia.copy(chatlog)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(chatlog, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(chatlog, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(chatlog, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(chatlog, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(chatlog, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Sepertinya terjadi kesalahan")
        

add_command_help(
    "copy",
    [
        [
            "ambil",
            "Mengambil Protected Media dari Channel/Grup.",
        ],
        [
            "copy",
            "Mengambil Protected/Timer Media.",
        ],
    ],
)
