# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
import time
from os.path import basename

NHENTAI_URL = "https://nhentai.net/g/"

@tgclient.on(NewMessage(pattern=r"^\.nhentai(?: |$)(.*)", outgoing=True))
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
    await msg.edit("Here is your story: \n" + NHENTAI_URL + str(number) + "\n\nHave fun!", link_preview=True)
    return

DESC = "nHentai module allows you to search for a specific story. Given a number, it will return a link to the story!\n\nBy Nuno Penim"
USAGE = "`.nhentai` <number>\nUsage: Replies with the URL to the given story number, if it exists."

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})