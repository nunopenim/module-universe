# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License


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
from subprocess import Popen, PIPE  # noqa: E402
from sys import executable  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)


@ehandler.on(command="python", hasArgs=True, outgoing=True)
async def python(event):
    full_cmd_str = event.pattern_match.group(1)
    py_exec = executable if " " not in executable else '"' + executable + '"'
    cmd_output = None
    error_msg = ("Error executing giving instruction(s)! Make sure the code "
                 "is well-formed")
    try:
        quoted_cmd = full_cmd_str.replace("\"", "'")
        proc = Popen([py_exec, "-c", quoted_cmd], stdout=PIPE, stderr=PIPE)
        cmd_output, cmd_error = proc.communicate()
        if proc.returncode or cmd_error:
            cmd_output = cmd_error
        cmd_output = ("".join([chr(char) for char in cmd_output])
                      if cmd_output is not None else error_msg)
    except Exception as e:
        log.error(e, exc_info=True)
        cmd_output = error_msg
    output = (f"**Python instruction(s):**\n`{full_cmd_str}`\n\n"
              f"**Result: **\n`{cmd_output}`" )
    await event.edit(output)
    return


DESCRIPTION = (
    "This official add-on module is a Python interpreter. You can run small "
    "instructions."
)
register_cmd_usage(
    "python",
    "<instruction(s)>",
    ("Runs the specified python instruction(s).\n\n"
     "**Notice:** the command will automatically replace any double quotes "
     "to single quotes.")
)
register_module_desc(DESCRIPTION)
register_module_info(
    name="Python Interpreter",
    authors="nunopenim, prototype74",
    version="1.3.2"
)
