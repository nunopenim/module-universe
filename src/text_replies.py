# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from userbot.sysutils.event_handler import EventHandler
import random
from os.path import basename

VERSION = "1.1.0"
ehandler = EventHandler()

GREETINGS = [
    "Top o' the morning!",
    "Good morning!",
    "Hi!",
    "Rise and shine!",
    "Greetings!",
    "Hey there!",
    "You know who this is.",
    "I come in peace!"]

INSULTS = [
    "When you were born, your mom thought she just had shit herself.",
    "Even a trained chimp does everything better than you.",
    "You know what is the difference between you and cancer? Cancer evolves.",
    "If you were in a room with Hitler and Stalin and I had a gun, I would shoot you twice.",
    "Your girlfriend could have picked a better man, like Saddam Hussein or an indonesian "\
    "pimp with lice and bad breath.",
    "If stupidity was taxed, you would be all stamped.",
    "Light travels faster than sound, which explains why you seemed bright until you speak.",
    "Your teeth are like stars, light years away and yellow.",
    "Your face is like a treasure, it needs to be buried very deep.",
    "Why don't you slip into something more comfortable, like a coma?",
    "I will never forget the first time we met, although I am trying.",
    "If you were a bit more intelligent, you would still be stupid.",
    "Not even your IQ test is positive.",
    "I heard you are very kind to animals, so please return that face to the gorilla.",
    "You got your head so far up your ass, you can chew food twice."]

@ehandler.on(pattern=r"^\.hi$", outgoing=True)
async def hello(event):
    await event.edit(random.choice(GREETINGS))
    return

@ehandler.on(pattern=r"^\.insult$", outgoing=True)
async def insult(event):
    await event.edit(random.choice(INSULTS))
    return

DESC = "The text replies module contains programmed sentences that are randomly chosen. "\
       "Check the usage to see what sentences are these."
USAGE = "`.hi`\nUsage: Greet people.\n\n`.insult`\nUsage: insults people."

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Text Replies", version=VERSION)})
