# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License


try:
    # >= 4.0.0
    from userbot.version import VERSION as hubot_version
except:
    # <= 3.0.4
    from userbot import VERSION as hubot_version


def isSupportedVersion(version: str) -> bool:
    try:
        bot_ver = tuple(map(int, hubot_version.split(".")))
        req_ver = tuple(map(int, version.split(".")))
        if bot_ver >= req_ver:
            return True
    except:
        pass
    return False


if not isSupportedVersion("5.0.1"):
    raise ValueError(f"Unsupported HyperUBot version ({hubot_version}). "
                      "Minimum required version is 5.0.1")

from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from telethon.tl.types import InputMediaDice  # noqa: E402
from logging import getLogger  # noqa: E402
import time  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)


@ehandler.on(command="fakedice", hasArgs=True, outgoing=True)
async def fake_dice(rolling):
    argums = rolling.text.split(" ")
    if len(argums) != 2:
        await rolling.edit("`Invalid arguments!`")
        return
    try:
        objective = int(argums[1])
    except ValueError:
        await rolling.edit("`Invalid destination value!`")
        return
    possible_vals = [1, 2, 3, 4, 5, 6]
    if objective not in possible_vals:
        await rolling.edit("`Invalid destination value!`")
        return
    await rolling.delete()
    while True:
        newdice = await rolling.client.send_message(rolling.to_id,
                                                    file=InputMediaDice("🎲"))
        rolled_val = newdice.media.value
        if rolled_val == objective:
            return
        else:
            await newdice.delete()
        time.sleep(0.25)
    return


DESC = (
    "This module allows you to launch a dice with any destination value you "
    "desire.\n**WARNING:** This module sends and deletes messages repeatedly, "
    "in order to get the correct value you want. Use at your own risk as you "
    "could be flagged for spam!"
)
register_cmd_usage(
    "fakedice",
    "<value>",
    ("Launches a fake dice with the specified value.\n\n"
     "**WARNING:** This module sends and deletes messages repeatedly, in "
     "order to get the correct value you want. Use at your own risk as you "
     "could be flagged for spam!")
)
register_module_desc(DESC)
register_module_info(
    name="Fake Dice",
    authors="nunopenim",
    version="1.2.3"
)
