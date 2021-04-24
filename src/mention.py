# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.sysutils.event_handler import EventHandler
from userbot.include.aux_funcs import fetch_user

VERSION = "1.2.0"

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
STR_MENT = "[{}](tg://user?id={})"

@ehandler.on(command="mention", hasArgs=True, outgoing=True)
async def tag_someone(mention):
    user = await fetch_user(mention)
    if user is None:
        await mention.edit("`Invalid user specified!`")
        return
    args = mention.text.split()
    if len(args) < 3:
        await mention.edit("`Too few arguments specified!`")
        return
    args.pop(0)
    args.pop(0)
    uid = user.id # Now we know shit works
    uname = ""
    for i in args:
        uname += i + " "
    await mention.delete() # we need fresh message, editing doesnt work for mention
    await mention.respond(STR_MENT.format(uname, uid))
    return

DESC = "The Mention module allows you to mention users under different text!"
register_cmd_usage("mention", " <tag> <text>",
                   "Tags a user under a different text other than their tag text!")

register_module_desc(DESC)
register_module_info(
    name="Mention",
    authors="nunopenim",
    version=VERSION
)
