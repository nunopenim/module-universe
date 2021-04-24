# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.event_handler import EventHandler
import time

VERSION = "1.2.1"

try:
    # >= 4.0.0
    from userbot.version import VERSION as hubot_version
except:
    # <= 3.0.4
    from userbot import VERSION as hubot_version

#temp solution
def isSupportedVersion(version: str) -> bool:
    try:
        bot_ver = tuple(map(int, hubot_version.split(".")))
        req_ver = tuple(map(int, version.split(".")))
        if bot_ver >= req_ver:
            return True
    except:
        pass
    return False

if not isSupportedVersion("4.0.0"):
    # required version
    raise ValueError(f"Unsupported HyperUBot version ({hubot_version}). "\
                      "Minimum required version is 4.0.0")

from userbot.sysutils.registration import (register_cmd_usage, register_module_desc, register_module_info)

ehandler = EventHandler()

@ehandler.on(command="nhentai", hasArgs=True, outgoing=True)
async def text(msg):
    commandArray = msg.text.split(" ")
    number = 0
    del(commandArray[0])
    if len(commandArray) != 1:
        await msg.edit("`Please insert just a single number to generate the nHentai URL`")
        return
    await msg.edit("`Finding the specific URL...`")
    try:
        number = int(commandArray[0])
    except ValueError:
        await msg.edit("`Invalid Number!`")
        return
    time.sleep(1)
    await msg.edit(f"Here is your story: \nhttps://nhentai.net/g/{number}\n\nHave fun!", link_preview=True)
    return

DESC = "nHentai module allows you to search for a specific story. Given a number, "\
       "it will return a link to the story!\n\nBy Nuno Penim"

register_cmd_usage("nhentai", "<number>", "Replies with the URL to the given "\
                   "story number, if it exists.")

register_module_desc(DESC)
register_module_info(
    name="nHentai",
    authors="nunopenim",
    version=VERSION
)
