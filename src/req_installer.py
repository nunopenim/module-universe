# Copyright 2020 githubcatw @github
# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

VERSION = "1.2.2"

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

from userbot.include.aux_funcs import event_log  # noqa: E402
from userbot.sysutils.configuration import getConfig  # noqa: E402
from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from logging import getLogger  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)
EMOJI_SUCCESS = "✔"
EMOJI_FAILURE = "❌"
EMOJI_INSTALLING = "⏳"

if " " not in sys.executable:
    EXECUTABLE = sys.executable
else:
    EXECUTABLE = '"' + sys.executable + '"'

PIP_COMMAND = EXECUTABLE + " -m pip install {}"


@ehandler.on(command="req", hasArgs=True, outgoing=True)
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
                message = message.replace(f"{EMOJI_INSTALLING} {r}",
                                          f"{EMOJI_FAILURE} {r} "
                                          "(package already installed)")
            else:
                message = message.replace(f"{EMOJI_INSTALLING} {r}",
                                          f"{EMOJI_SUCCESS} {r}")
                success = success + 1
        except subprocess.CalledProcessError:
            message = message.replace(f"{EMOJI_INSTALLING} {r}",
                                      f"{EMOJI_FAILURE} {r}")
        await event.edit(message.rstrip())
    message = message.replace("Installing ", f"Installed {success}/")
    if getConfig("LOGGING"):
        await event_log(event, "REQUIREMENT INSTALLER",
                        custom_text="{} of {} python packages queued "
                        "were installed successfully!".format(success,
                                                              len(reqs)))
    await event.edit(message.rstrip())
    return


DESC = ("This module allows you to install pip packages. Sometimes extra "
        "modules require other pip packages that are not present in "
        "requirements.txt. If such happens, the bot can be effectively "
        "bricked! It is your duty to read the README file avaliable "
        "in the Repo of the module, in case it needs any module!")

register_cmd_usage("req", "<package names>",
                   ("installs (or attempts to install) the specified pip "
                    "package names."))

register_module_desc(DESC)
register_module_info(
    name="Requirements Installer",
    authors="githubcatw, nunopenim",
    version=VERSION
)
