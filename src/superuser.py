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
from userbot.sysutils.registration import (getAllModules,  # noqa: E402
                                           getUserModules,  # noqa: E402
                                           register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from logging import getLogger  # noqa: E402
from shutil import copyfile  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)
DISCLAIMER = ("**SUPERUSER MODULE DISCLAIMER**\n\nThis module allows you "
              "to make changes to the system directory of the userbot. These "
              "changes will be permanent, and cannot be revertible. "
              "They will also likely break the updating system! You have "
              "been warned!")

WARNING_SHOWN = os.path.isfile(os.path.join(".", "superuser.hbot"))
LOGGING = getConfig("LOGGING")
USER_MODULES_DIR = os.path.join(".", "userbot", "modules_user")
MODULES_DIR = os.path.join(".", "userbot", "modules")


@ehandler.on(command="sudo", hasArgs=True, outgoing=True)
async def superuser(command):
    global WARNING_SHOWN
    cmd_args = command.pattern_match.group(1).split(" ", 1)
    if cmd_args[0].lower() == "disclaimer":
        await command.edit(DISCLAIMER)
        f = open(os.path.join(".", "userbot", "superuser.hbot"), "w+")
        f.write("\n")
        f.close()
        WARNING_SHOWN = True
    elif cmd_args[0].lower() == "remove":
        if not WARNING_SHOWN:
            await command.edit("For safety measures, the command will not "
                               "run, please make sure you have read the "
                               "disclaimer by typing `.sudo disclaimer`")
            return
        if len(cmd_args) == 1:
            await command.edit("No name of module to be removed specified, "
                               "command halted!")
            return
        if len(cmd_args) > 2:
            await command.edit("For safety reasons you can only uninstall "
                               "one module at a time!")
            return
        modName = cmd_args[1].lower()
        if modName not in getAllModules():
            await command.edit(f"Unknown module named `{modName}`. "
                               "Uninstallation halted!")
            return
        if modName in getUserModules():
            await command.edit("`Uninstalling user module...`")
            os.remove(os.path.join(USER_MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command, "SUPERUSER",
                                ("The user module `{}` was removed "
                                 "successfully").format(modName))
            await command.edit("The user module `{}` was uninstalled "
                               "successfully! "
                               "Reboot recommended!".format(modName))
        else:
            await command.edit("`Uninstalling system module...`")
            os.remove(os.path.join(MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command, "SUPERUSER",
                                ("The system module `{}` was removed "
                                 "successfully").format(modName))
            await command.edit("The system module `{}` was uninstalled "
                               "successfully! "
                               "Reboot recommended!".format(modName))
    elif cmd_args[0].lower() == "convert":
        if not WARNING_SHOWN:
            await command.edit("For safety measures, the command will not "
                               "run, please make sure you have read the "
                               "disclaimer by typing `.sudo disclaimer`")
            return
        if len(cmd_args) == 1:
            await command.edit("No name of module to be converted "
                               "specified, command halted!")
            return
        if len(cmd_args) > 2:
            await command.edit("For safety reasons you can only convert "
                               "one module at a time!")
            return
        modName = cmd_args[1].lower()
        if modName not in getAllModules():
            await command.edit("Unknown module named "
                               "`{}`. Not found!".format(modName))
            return
        if modName in getUserModules():
            await command.edit("`Converting user module into "
                               "system module...`")
            copyfile(os.path.join(USER_MODULES_DIR, modName + ".py"),
                     os.path.join(MODULES_DIR, modName + ".py"))
            os.remove(os.path.join(USER_MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command,
                                "SUPERUSER",
                                ("The User module `{}` was successfully "
                                 "converted into a "
                                 "System module!").format(modName))
            await command.edit("The User module `{}` was successfully "
                               "converted into a System module! Reboot "
                               "recommended!".format(modName))
        else:
            await command.edit("`Converting system module "
                               "into user module...`")
            copyfile(os.path.join(MODULES_DIR, modName + ".py"),
                     os.path.join(USER_MODULES_DIR, modName + ".py"))
            os.remove(os.path.join(MODULES_DIR, modName + ".py"))
            time.sleep(1)
            if LOGGING:
                await event_log(command,
                                "SUPERUSER",
                                ("The System module `{}` was "
                                 "successfully converted into a "
                                 "User module!").format(modName))
            await command.edit("The System module `{}` was successfully "
                               "converted into a user module! "
                               "Reboot recommended!".format(modName))
    else:
        await command.edit("Invalid argument! Please make sure it is "
                           "**disclaimer**, **remove** or **convert**")
    return


DESC = ("The Superuser module offers the possibility of more customization "
        "of the userbot. Be careful however, as this can break your "
        "userbot. The updater will likely break if you use this module!")

register_cmd_usage("sudo",
                   "<option> <package_name>",
                   ("\n`.sudo disclaimer`\n"
                    "Shows the warning message, and acknowledges the user "
                    "has read it.\n\n"
                    "`.sudo remove <package_name>`\n"
                    "Removes the specified package from the system.\n\n"
                    "`.sudo convert <package_name>`\n"
                    "Converts a User Module in a System Module and "
                    "vice-versa."))

register_module_desc(DESC)
register_module_info(
    name="SuperUser",
    authors="nunopenim",
    version=VERSION
)
