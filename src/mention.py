# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.sysutils.event_handler import EventHandler
from userbot.include.aux_funcs import fetch_user, module_info
from os.path import basename

VERSION = "1.1.0"
ehandler = EventHandler()
STR_MENT = "[{}](tg://user?id={})"

@ehandler.on(pattern=r"^\.mention(?: |$)(.*)$", outgoing=True)
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
USAG = "`.mention` <tag> <text>\nUsage: Tags a user under a different text other than their tag text!"

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAG})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Mention", version=VERSION)})
