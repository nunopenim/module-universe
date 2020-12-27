# Copyright 2020 githubcatw @github
# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from os.path import basename
import subprocess
from userbot import OS, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import event_log, module_info
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
import sys

VERSION = "1.1.0"
ehandler = EventHandler()
EMOJI_SUCCESS = "✔"
EMOJI_FAILURE = "❌"
EMOJI_INSTALLING = "⏳"

if " " not in sys.executable:
    EXECUTABLE = sys.executable
else:
    EXECUTABLE = '"' + sys.executable + '"'

if OS and OS.startswith("win"):
    PIP_COMMAND = "pip install {}"
else:
    PIP_COMMAND = EXECUTABLE + " -m pip install {}"

@ehandler.on(pattern=r"^\.req (.*)", outgoing=True)
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
            if f"Requirement already satisfied: {r}" in output:
                message = message.replace(f"{EMOJI_INSTALLING} {r}",f"{EMOJI_FAILURE} {r} "\
                                           "(package already installed)")
            else:
                message = message.replace(f"{EMOJI_INSTALLING} {r}",f"{EMOJI_SUCCESS} {r}")
                success = success + 1
        except subprocess.CalledProcessError:
            message = message.replace(f"{EMOJI_INSTALLING} {r}",f"{EMOJI_FAILURE} {r}")
        await event.edit(message.rstrip())
    message = message.replace("Installing ", f"Installed {success}/")
    if getConfig("LOGGING"):
        await event_log(event, "REQUIREMENT INSTALLER", custom_text="{} of {} python "\
                        "packages queued were installed successfully!".format(success, len(reqs)))
    await event.edit(message.rstrip())
    return

DESC = "This module allows you to install pip packages. Sometimes extra modules require "\
       "other pip packages that are not present in requirements.txt. If such happens, "\
       "the bot can be effectively bricked! It is your duty to read the README file avaliable "\
       "in the Repo of the module, in case it needs any module!"

USAGE = "`.req `<package names>"\
        "\nUsage: installs (or attempts to install) the specified pip package names."

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Requirements Installer", version=VERSION)})
