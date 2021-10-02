# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

VERSION = "1.3.1"

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

from userbot.include.aux_funcs import shell_runner  # noqa: E402
from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from logging import getLogger  # noqa: E402
from sys import executable  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)


@ehandler.on(command="python", hasArgs=True, outgoing=True)
async def python(command):
    commandArray = command.text.split(" ")
    del (commandArray[0])
    python_instruction = ""
    for word in commandArray:
        python_instruction += word + " "
    command_for_bash = [executable, " -c ", '"' + python_instruction + '"']
    cmd_output = shell_runner(command_for_bash)
    if cmd_output is None:
        cmd_output = ("Error executing instruction! Most likely you "
                      "used \" instead of '. This is a known issue.")
    output = "**Python instruction:** `" + python_instruction + "`\n\n"
    output += "**Result: **\n`" + cmd_output + "`"
    await command.edit(output)
    return


DESCRIPTION = ("This official add-on module is a Python interpreter. You can "
               "run small instructions.")
register_cmd_usage("python",
                   "<instruction(s)>",
                   ("Runs the specified python instruction.\n\n"
                    "**Notice:** Please use ' as the string delimiters "
                    "instead of \", or errors "
                    "could happen with the command processor."))

register_module_desc(DESCRIPTION)
register_module_info(
    name="Python Interpreter",
    authors="nunopenim, prototype74",
    version=VERSION
)
