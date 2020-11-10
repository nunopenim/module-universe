# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info, shell_runner
from telethon.events import NewMessage
from os.path import basename
from sys import executable

VERSION = "1.1.0"

@tgclient.on(NewMessage(pattern=r"^\.python(?: |$)(.*)", outgoing=True))
async def python(command):
    commandArray = command.text.split(" ")
    del (commandArray[0])
    python_instruction = ""
    for word in commandArray:
        python_instruction += word + " "
    command_for_bash = [executable, " -c ", '"' + python_instruction + '"']
    cmd_output = shell_runner(command_for_bash)
    if cmd_output is None:
        cmd_output = "Error executing instruction! Most likely you used \" instead of '. This is a known issue."
    output = "**Python instruction:** `" + python_instruction + "`\n\n"
    output +=  "**Result: **\n`" + cmd_output + "`"
    await command.edit(output)
    return

DESCRIPTION = "This official add-on module is a Python interpreter. You can run small instructions."
USAGE = "`.python` <instruction(s)>\nUsage: Runs the specified python instruction.\n\n**Notice:** Please use ' as the string delimiters instead of \", or errors could happen with the command processor."

MODULE_DESC.update({basename(__file__)[:-3]: DESCRIPTION})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Python Interpreter", version=VERSION)})
