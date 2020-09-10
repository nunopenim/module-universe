# Copyright 2020 githubcatw @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

import time
import os
import subprocess

from userbot import tgclient, OS, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage

EMOJI_SUCCESS = "✔"
EMOJI_FAILURE = "❌"
EMOJI_INSTALLING = "⏳"
if OS and OS.startswith("win"):
    PIP_COMMAND = "pip install {}"
else:
    PIP_COMMAND = "python3 -m pip install {}"

@tgclient.on(NewMessage(pattern=r"^\.req (.*)", outgoing=True))
async def req(event):
    reqs = event.pattern_match.group(1).split()
    message = f"Installing {len(reqs)} package(s):\n"
    success = 0
    for r in reqs:
        message = message + f"{EMOJI_INSTALLING} {r}\n"
        await event.edit(message)
        try:
            bout = subprocess.check_output(PIP_COMMAND.format(r).split())
            output = bout.decode('ascii')
            message = message.replace(f"{EMOJI_INSTALLING} {r}",f"{EMOJI_SUCCESS} {r}")
            success = success + 1
        except subprocess.CalledProcessError:
            message = message.replace(f"{EMOJI_INSTALLING} {r}",f"{EMOJI_FAILURE} {r}")
        await event.edit(message.rstrip())
    message = message.replace("Installing ",f"Installed {success}/")
    await event.edit(message.rstrip())
