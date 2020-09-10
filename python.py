# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
from subprocess import check_output, CalledProcessError
from os.path import basename
from sys import executable

@tgclient.on(NewMessage(pattern=r"^\.python(?: |$)(.*)", outgoing=True))
async def python(command):
    python_instruction = command.pattern_match.group(1).split(" ", 1)
    command_for_bash = executable + " -c " + '"' + python_instruction + '"'
    try:
        cmd_output = check_output(command_for_bash, shell=True).decode()
    except CalledProcessError:
        cmd_output = "Error executing instruction! Most likely you used \" instead of '. This is a known issue."
    output = "**Python instruction:** `" + python_instruction + "`\n\n"
    output +=  "**Result: **\n`" + cmd_output + "`"
    await command.edit(output)
    return

DESCRIPTION = "This official add-on module is a Python interpreter. You can run small instructions."
USAGE = "`.python` <instruction(s)>\nUsage: Runs the specified python instruction."

MODULE_DESC.update({basename(__file__)[:-3]: DESCRIPTION})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})
