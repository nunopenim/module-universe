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
from telethon.errors.rpcerrorlist import MessageNotModifiedError  # noqa: E402
from logging import getLogger  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)


@ehandler.on(command="upper", hasArgs=True, outgoing=True)
async def upper_case(event):
    args = event.pattern_match.group(1)
    rply_msg = await event.get_reply_message()
    if args:
        text = args
    elif rply_msg:
        text = rply_msg.text
    else:
        await event.edit("`Please use this command as a reply or "
                         "with arguments, so I have something to capitalize!`")
        return
    await event.edit(text.upper())
    return


@ehandler.on(command="lower", hasArgs=True, outgoing=True)
async def lower_case(event):
    args = event.pattern_match.group(1)
    rply_msg = await event.get_reply_message()
    if args:
        text = args
    elif rply_msg:
        text = rply_msg.text
    else:
        await event.edit("`Please use this command as a reply or with "
                         "arguments, so I have something to lowercase!`")
        return
    await event.edit(text.lower())
    return


@ehandler.on(command="noformat", outgoing=True)
async def unformat(event):
    rply_msg = await event.get_reply_message()
    if rply_msg:
        text = rply_msg.raw_text
    else:
        await event.edit("`Please use this command as a reply, so I have "
                         "something to unformat!`")
        return
    try:
        await event.edit(text)
    except MessageNotModifiedError:
        await event.edit("`Unspecifed error! Likely you are replying to an "
                         "already non-formatted message by a Userbot, or to "
                         "an userbot command.`")
    return


DESC = (
    "The text_utils module offers utilities to edit text, such as convert a "
    "message to upper case, lower case or unformat it!"
)
register_cmd_usage(
    "upper",
    "<text/reply>",
    "Converts the specified text to upper case."
)
register_cmd_usage(
    "lower",
    "<text/reply>",
    "Decodes the given message from base64."
)
register_cmd_usage(
    "noformat",
    None,
    "Unformats the replied message (removes bold, italic, monospace, etc...)."
)
register_module_desc(DESC)
register_module_info(
    name="Text Utilities",
    authors="nunopenim",
    version="1.2.3"
)
