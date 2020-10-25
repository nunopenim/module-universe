# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, LOGGING, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info, event_log
from telethon.events import NewMessage
from os.path import basename
from asyncio import sleep

VERSION = "1.0.0"

@tgclient.on(NewMessage(pattern=r"^\.dspam(?: |$)(.*)", outgoing=True))
async def delay_spammer(msg):
    args = msg.text.split()
    if len(args) < 4:
        await msg.edit("Invalid arguments, make sure you use the command as `.dspam` <number> <delay> <message to spam>")
        return
    try:
        msg_counter = int(args[1])
        delay = float(args[2])
    except ValueError:
        await msg.edit("`Please insert a number of times and a delay time to spam! I cannot spam for word values (like spam banana times, idk)!`")
        return
    if msg_counter < 1 or delay <= 0:
        await msg.edit("`Please insert a number superior of 0, it doesn't make sense to spam {} times with a delay of {} seconds, does it?`".format(msg_counter, delay))
        return
    msg_to_spam = ""
    counter = 0
    for i in args:
        if counter < 3:
            pass
        else:
            msg_to_spam += " " + i # building the message itself
        counter += 1
    await msg.delete()
    for i in range(msg_counter):
        await msg.respond(msg_to_spam)
        await sleep(delay)
    if LOGGING:
        await event_log(msg, "DSPAM", custom_text="The .dspam command has been executed successfully. It spammed the message`{}` {} times, with a delay of {} seconds".format(msg_to_spam, msg_counter, delay))
    return

@tgclient.on(NewMessage(pattern=r"^\.spam(?: |$)(.*)", outgoing=True))
async def spammer(msg):
    args = msg.text.split()
    if len(args) < 3:
        await msg.edit("Invalid arguments, make sure you use the command as `.spam` <number> <message to spam>")
        return
    try:
        msg_counter = int(args[1])
    except ValueError:
        await msg.edit("`Please insert a number of times to spam! I cannot spam a word!`")
        return
    if msg_counter < 1:
        await msg.edit("`Please insert a number superior of 0, it doesn't make sense to spam {} times, does it?`".format(msg_counter))
        return
    msg_to_spam = ""
    counter = 0
    for i in args:
        if counter < 2:
            pass
        else:
            msg_to_spam += " " + i # building the message itself
        counter += 1
    await msg.delete()
    for i in range(msg_counter):
        await msg.respond(msg_to_spam)
    if LOGGING:
        await event_log(msg, "SPAM", custom_text="The .spam command has been executed successfully. It spammed the message`{}` {} times".format(msg_to_spam, msg_counter))
    return

DESC = "This module offers tools to spam faster. Although the name and infinite possibilities for evil this module can bring, it should not be used for evil. It's designed for purposes of joking.\n\n**WARNING**: Use it at your own risk. If you abuse this module, Telegram can (and will) restrict your account!"

USAGE = "`.spam` <number of times> <message>\nUsage: Spams a message the number of times specified\n\n`.dspam` <number of times> <delay> <message>\nUsage: Spams a message the number of times specified, with an interval of <delay> seconds\n\n**WARNING**: Use this module at your own risk. It can get you banned and restricted from Telegram!"

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Spam", version=VERSION)})
