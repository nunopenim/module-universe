# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License


VERSION = "1.2.1"

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
from logging import getLogger  # noqa: E402
import random  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)

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
    ("If you were in a room with Hitler and Stalin and I had a gun, I would "
     "shoot you twice."),
    ("Your girlfriend could have picked a better man, like Saddam Hussein "
     "or an indonesian pimp with lice and bad breath."),
    "If stupidity was taxed, you would be all stamped.",
    ("Light travels faster than sound, which explains why you seemed bright "
     "until you speak."),
    "Your teeth are like stars, light years away and yellow.",
    "Your face is like a treasure, it needs to be buried very deep.",
    "Why don't you slip into something more comfortable, like a coma?",
    "I will never forget the first time we met, although I am trying.",
    "If you were a bit more intelligent, you would still be stupid.",
    "Not even your IQ test is positive.",
    ("I heard you are very kind to animals, so please return that face to the "
     "gorilla."),
    "You got your head so far up your ass, you can chew food twice."]


@ehandler.on(command="hi", outgoing=True)
async def hello(event):
    await event.edit(random.choice(GREETINGS))
    return


@ehandler.on(command="insult", outgoing=True)
async def insult(event):
    await event.edit(random.choice(INSULTS))
    return


DESC = ("The text replies module contains programmed sentences that are "
        "randomly chosen. Check the usage to see what sentences are these.")

register_cmd_usage("hi", None, "Greet people.")
register_cmd_usage("insult", None, "insults people.")

register_module_desc(DESC)
register_module_info(
    name="Text Replies",
    authors="nunopenim",
    version=VERSION
)
