# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient
from telethon.events import NewMessage
import time

NHENTAI_URL = "https://nhentai.net/g/"

@tgclient.on(NewMessage(pattern=r"^\.nhentai?: |$)(.*)", outgoing=True))
async def text(msg):
	commandArray = command.text.split(" ")
	number = 0
	del(commandArray[0])
	if len(commandArray) != 1:
        await mgs.edit("`Please insert just a single number to generate the nHentai URL`")
        return
	await mgs.edit("`Finding the specific URL...`")
	try:
        number = int(commandArray[0])
    except ValueError:
		await mgs.edit("`Invalid Number!`")
        return
    time.sleep(1)
    await msg.edit("Here is your story: " + NHENTAI_URL + str(number) + "\nHave fun!")
    return
