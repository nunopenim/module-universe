# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from userbot.sysutils.event_handler import EventHandler
from telethon.tl.types import InputMediaDice
import time
from os.path import basename

VERSION = "1.1.0"
ehandler = EventHandler()

@ehandler.on(pattern=r"^\.fakedice(?: |$)(.*)", outgoing=True)
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
        newdice = await rolling.client.send_message(rolling.to_id, file=InputMediaDice("🎲"))
        rolled_val = newdice.media.value
        if rolled_val == objective:
            return
        else:
            await newdice.delete()
        time.sleep(0.25)

DESC = "This module allows you to launch a dice with any destination value you desire."\
       "\n**WARNING:** This module sends and deletes messages repeatedly, in order to get "\
       "the correct value you want. Use at your own risk as you could be flagged for spam!"
USG = "`.fakedice` <value>"\
      "\nUsage: Launches a fake dice with the specified value"\
      "\n\n**WARNING:** This module sends and deletes messages repeatedly, "\
      "in order to get the correct value you want. Use at your own risk as you could be flagged for spam!"

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USG})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Fake Dice", version=VERSION)})
