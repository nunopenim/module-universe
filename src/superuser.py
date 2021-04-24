# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.aux_funcs import event_log
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from shutil import copyfile
import os
import time

VERSION = "1.2.1"

try:
    # >= 4.0.0
    from userbot.version import VERSION as hubot_version
except:
    # <= 3.0.4
    from userbot import VERSION as hubot_version

#temp solution
def isSupportedVersion(version: str) -> bool:
    try:
        bot_ver = tuple(map(int, hubot_version.split(".")))
        req_ver = tuple(map(int, version.split(".")))
        if bot_ver >= req_ver:
            return True
    except:
        pass
    return False

if not isSupportedVersion("4.0.0"):
    # required version
    raise ValueError(f"Unsupported HyperUBot version ({hubot_version}). "\
                      "Minimum required version is 4.0.0")

from userbot.sysutils.registration import (getAllModules, getUserModules, register_cmd_usage,
                                           register_module_desc, register_module_info)

ehandler = EventHandler()
DISCLAIMER = "**SUPERUSER MODULE DISCLAIMER**\n\nThis module allows you to make changes to "\
             "the system directory of the userbot. These changes will be permanent, and "\
             "cannot be revertible. They will also likely break the updating system! You have been warned!"

WARNING_SHOWN = os.path.isfile(os.join.path(".", "superuser.hbot"))
LOGGING = getConfig("LOGGING")
USER_MODULES_DIR = os.join.path(".", "userbot", "modules_user")
MODULES_DIR = os.join.path(".", "userbot", "modules")

@ehandler.on(command="sudo", hasArgs=True, outgoing=True)
async def superuser(command):
    global WARNING_SHOWN
    cmd_args = command.pattern_match.group(1).split(" ", 1)
    if cmd_args[0].lower() == "disclaimer":
        await command.edit(DISCLAIMER)
        f = open(os.join.path(".", "userbot", "superuser.hbot"), "w+")
        f.write("\n")
        f.close()
        WARNING_SHOWN = True
    elif cmd_args[0].lower() == "remove":
        if not WARNING_SHOWN:
            await command.edit("For safety measures, the command will not run, please make "\
                               "sure you have read the disclaimer by typing `.sudo disclaimer`")
            return
        if len(cmd_args) == 1:
            await command.edit("No name of module to be removed specified, command halted!")
            return
        if len(cmd_args) > 2:
            await command.edit("For safety reasons you can only uninstall one module at a time!")
            return
        modName = cmd_args[1].lower()
        if modName not in getAllModules():
            await command.edit("Unknown module named `{}`. Uninstallation halted!")
            return
        if modName in getUserModules():
            await command.edit("`Uninstalling user module...`")
            os.remove(os.join.path(USER_MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command, "SUPERUSER", "The user module `{}` was removed "\
                                "successfully".format(modName))
            await command.edit("The user module `{}` was uninstalled successfully! "\
                               "Reboot recommended!".format(modName))
        else:
            await command.edit("`Uninstalling system module...`")
            os.remove(os.join.path(MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command, "SUPERUSER", "The system module `{}` was removed "\
                                "successfully".format(modName))
            await command.edit("The system module `{}` was uninstalled successfully! "\
                               "Reboot recommended!".format(modName))
    elif cmd_args[0].lower() == "convert":
        if not WARNING_SHOWN:
            await command.edit("For safety measures, the command will not run, please make "\
                               "sure you have read the disclaimer by typing `.sudo disclaimer`")
            return
        if len(cmd_args) == 1:
            await command.edit("No name of module to be converted specified, command halted!")
            return
        if len(cmd_args) > 2:
            await command.edit("For safety reasons you can only convert one module at a time!")
            return
        modName = cmd_args[1].lower()
        if modName not in getAllModules():
            await command.edit("Unknown module named `{}`. Not found!".format(modName))
            return
        if modName in getUserModules():
            await command.edit("`Converting user module into system module...`")
            copyfile(os.join.path(USER_MODULES_DIR, modName + ".py"), os.join.path(MODULES_DIR, modName + ".py"))
            os.remove(os.join.path(USER_MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command, "SUPERUSER", "The User module `{}` was successfully "\
                                "converted into a System module!".format(modName))
            await command.edit("The User module `{}` was successfully converted into a "\
                               "System module! Reboot recommended!".format(modName))
        else:
            await command.edit("`Converting system module into user module...`")
            copyfile(os.join.path(MODULES_DIR, modName + ".py"), os.join.path(USER_MODULES_DIR, modName + ".py"))
            os.remove(os.join.path(MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command, "SUPERUSER", "The System module `{}` was successfully "\
                                "converted into a User module!".format(modName))
            await command.edit("The System module `{}` was successfully converted into a "\
                               "user module! Reboot recommended!".format(modName))
    else:
        await command.edit("Invalid argument! Please make sure it is **disclaimer**, **remove** or **convert**")
    return

DESC = "The Superuser module offers the possibility of more customization of the userbot. "\
       "Be careful however, as this can break your userbot. The updater will likely "\
       "break if you use this module!"
        
register_cmd_usage("sudo", "<disclaimer/remove <package_name>/convert <package_name>>",
                   "[disclaimer] Shows the warning message, and acknowledges the user has read it.\n"\
                   "[remove] Removes the specified package from the system.\n"\
                   "[convert] Converts a User Module in a System Module and vice-versa.")

register_module_desc(DESC)
register_module_info(
    name="SuperUser",
    authors="nunopenim",
    version=VERSION
)
