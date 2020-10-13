# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from os.path import basename

@tgclient.on(NewMessage(pattern=r"^\.upper(?: |$)(.*)", outgoing=True))
async def upper_case(event):
    args = event.pattern_match.group(1)
    rply_msg = await event.get_reply_message()
    if args:
        text = args
    elif rply_msg:
        text = rply_msg.text
    else:
        await event.edit("`Please use this command as a reply or with arguments, so I have something to capitalize!`")
        return
    await event.edit(text.upper())
    return

@tgclient.on(NewMessage(pattern=r"^\.lower(?: |$)(.*)", outgoing=True))
async def lower_case(event):
    args = event.pattern_match.group(1)
    rply_msg = await event.get_reply_message()
    if args:
        text = args
    elif rply_msg:
        text = rply_msg.text
    else:
        await event.edit("`Please use this command as a reply or with arguments, so I have something to lowercase!`")
        return
    await event.edit(text.lower())
    return

@tgclient.on(NewMessage(pattern=r"^\.noformat(?: |$)(.*)", outgoing=True))
async def unformat(event):
    rply_msg = await event.get_reply_message()
    if rply_msg:
        text = rply_msg.raw_text
    else:
        await event.edit("`Please use this command as a reply, so I have something to unformat!`")
        return
    try:
        await event.edit(text)
    except MessageNotModifiedError:
        await event.edit("`Unspecifed error! Likely you are replying to an already non-formatted message by a Userbot, or to an userbot command.`")
    return

DESC = "The text_utils module offers utilities to edit text, such as convert a message to upper case, lower case or unformat it!"
USAGE = "`.upper` <text/reply>\nUsage: Converts the specified text to upper case.\n\n`.lower` <text/reply>\nUsage: Converts the specified text to lower case.\n\n`.noformat`\nUsage: Unformats the replied message (removes bold, italic, monospace, etc...)."

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})