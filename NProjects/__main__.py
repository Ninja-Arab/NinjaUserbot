# NProjecst
# Original Code By : @mrismanaziz (PyroMan-UserBot)
# Copyright (C) 2023 NK-Userbot

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from NProjects import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from NProjects.helpers.misc import create_botlog, heroku
from NProjects.modules import ALL_MODULES

MSG_ON = """
**NK-Userbot Telah Aktif!**
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"NProjects.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("Nakanisme")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("NProjects").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("NProjects").info(f"NK-Userbot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("NProjects").info("Starting NK-Userbot")
    install()
    heroku()
    LOOP.run_until_complete(main())
