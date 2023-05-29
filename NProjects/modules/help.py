# NProjecst
# Original Code By : @mrismanaziz (PyroMan-UserBot)
# Copyright (C) 2023 NK-Userbot

from prettytable import PrettyTable, NONE
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from NProjects import CMD_HELP
from NProjects.helpers.basic import edit_or_reply
from NProjects.helpers.utility import split_list


@Client.on_message(filters.command("help", CMD_HANDLER) & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        ac = PrettyTable()
        ac.header = False
        ac.align = "l"
        ac.vertical_char = "│"
        ac.hrules = NONE
        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])
        string = ""
        for x in CMD_HELP:
            string += "✰`" + str(x) +"`"
            string += " "
        texthelp = (
            f"⛑ **NK-Userbot Modules** ⛑\n\n"
            f"Creator : [Naka](https://t.me/RedflixHD)\n\n"
            f"Daftar Perintah :\n"
            f"```{ac}```\n\n"
            f"__© @Nakanisme__"
        )
        await edit_or_reply(message, texthelp, disable_web_page_preview=True)
        await message.reply(
            f"**Contoh Ketik** `{CMD_HANDLER}help afk` **Untuk Melihat Informasi Module**"
        )

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **Help For {str(help_arg).upper()}** 」──\n\n"
            for x in commands:
                this_command += f"  •  **Command:** `{CMD_HANDLER}{str(x)}`\n  •  **Function:** `{str(commands[x])}`\n\n"
            this_command += "© @Nakanisme"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **Bukan Nama Modul yang Valid.**",
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
