# NProjecst
# Original Code By : @mrismanaziz (PyroMan-UserBot)
# Copyright (C) 2023 NK-Userbot

import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from NProjects import StartTime
from NProjects.helpers.basic import edit_or_reply
from NProjects.helpers.constants import WWW
from NProjects.helpers.PyroHelpers import SpeedConvert
from NProjects.utils.tools import get_readable_time

from .help import add_command_help


@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(filters.command("ping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "**0% ▒▒▒▒▒▒▒▒▒▒**")
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await xx.edit("**40% ████▒▒▒▒▒▒**")
    await xx.edit("**60% ██████▒▒▒▒**")
    await xx.edit("**80% ████████▒▒**")
    await xx.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"**NK USERBOT**\n"
        f"• `Ping    :` `%sms`\n"
        f"• `Uptime  :` `{uptime}` \n"
        f"• `Lord    :` {client.me.mention}" % (duration)
    )


@Client.on_message(filters.command("kping", cmd) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"**NK USERBOT**\n"
        f"• `Ping    :` `%sms`\n"
        f"• `Uptime  :` `{uptime}` \n"
        f"• `Lord    :` {client.me.mention}" % (duration)
    )


add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
        ["kping", "Untuk Menunjukkan Ping Bot Anda ( Beda animasi doang )."],
    ],
)
