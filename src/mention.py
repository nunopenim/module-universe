# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
from userbot.include.aux_funcs import fetch_user
from os.path import basename

STR_MENT = "[{}](tg://user?id={})"

@tgclient.on(NewMessage(pattern=r"^\.mention(?: |$)(.*)$", outgoing=True))
async def tag_someone(mention):
    user = await fetch_user(mention)
    if user is None:
        await mention.edit("`Invalid user specified!`")
        return
    args = mention.text.split()
    if len(args) != 3:
        await mention.edit("`Too few/many arguments specified!`")
        return
    uid = user.id # Now we know shit works
    uname = args[2]
    await mention.delete() # we need fresh message, editing doesnt work for mention
    await mention.respond(STR_MENT.format(uname, uid))
    return

DESC = "The Mention module allows you to mention users under different text!"
USAG = "`.mention` <tag> <text>\nUsage: Tags a user under a different text other than their tag text!"

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAG})