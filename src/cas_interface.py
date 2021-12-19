# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License
#
# This module is powered by Combot Anti-Spam (CAS) system (https://cas.chat)


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


from userbot.include.pip_utils import checkPkgByDist, installPkg  # noqa: E402
from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from telethon.tl.types import Channel, PeerChannel, PeerUser, User  # noqa: E402
from dateutil.parser import parse  # noqa: E402
from logging import getLogger  # noqa: E402
import json  # noqa: E402

if not checkPkgByDist("requests"):
    installPkg("requests")

import requests  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)


async def _getCASUser(event, entity, entity_id):
    user_id = entity.id if entity else entity_id
    if entity:
        if isinstance(entity, Channel):
            firstname = entity.title
            lastname = None
            user_id = int(f"-100{str(user_id)}")
        else:
            firstname = (entity.first_name if not entity.deleted
                         else "Deleted Account")
            lastname = entity.last_name  # can be None
        username = entity.username  # can be None
        await event.edit(f"Checking CAS status of {firstname}...")
    else:
        await event.edit(f"Checking CAS status of ID `{user_id}`...")

    cas_link = f"https://api.cas.chat/check?user_id={user_id}"

    try:
        with requests.request("GET", cas_link) as raw_data:
            cas_data = json.loads(raw_data.text)
        raw_data.close()
    except Exception:
        log.error("CAS user data not available", exc_info=True)
        await event.edit("`CAS check failed`")
        return

    try:
        offenses = cas_data.get("result", {}).get("offenses")
    except Exception as e:
        log.warning(e)
        offenses = None

    try:
        time_banned = cas_data.get("result", {}).get("time_added")
        if time_banned:
            time_banned = parse(time_banned)
    except Exception as e:
        log.warning(e)
        time_banned = None

    is_banned = f"[Banned]({cas_link})" if cas_data.get("ok") else "Not Banned"

    entity_type = "Channel" if isinstance(entity, Channel) else "User"
    text = f"**{entity_type} data**\n"
    text += f"ID: `{user_id}`\n"
    if entity:
        if isinstance(entity, Channel):
            text += f"Title: {firstname}\n"
        else:
            text += f"First name: {firstname}\n"
        if lastname:
            text += f"Last name: {lastname}\n"
        if username:
            text += f"Username: @{username}\n"
    text += "\n**CAS data**\n"
    text += f"Result: {is_banned}\n"
    if offenses:
        text += f"Offenses: `{offenses}`\n"
    if time_banned:
        text += (f"Banned since: "
                 f"`{time_banned.strftime('%b %d, %Y')} - "
                 f"{time_banned.time()} {time_banned.tzname()}`")
    await event.edit(text)
    return


@ehandler.on(command="cascheck", hasArgs=True, outgoing=True)
async def cascheck(event):
    entity_id = None
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        if isinstance(msg.from_id, PeerUser):
            entity_id = msg.from_id.user_id
        elif isinstance(msg.from_id, PeerChannel):
            entity_id = msg.from_id.channel_id
        else:
            await event.edit("`This is not a bot, person or channel`")
            return
    else:
        entity_id = event.pattern_match.group(1)
        try:
            entity_id = int(entity_id)
        except ValueError:
            pass

    try:
        if not entity_id:
            entity = await event.client.get_me()
        else:
            entity = await event.client.get_entity(entity_id)
    except Exception as e:
        err_msg = e
        entity = None

    if entity and (not isinstance(entity, (User, Channel)) or
                   isinstance(entity, Channel) and not entity.broadcast):
        await event.edit("`This is not a bot, person or channel`")
        return

    if not entity and not isinstance(entity_id, int):
        await event.edit("`Given ID is invalid`")
        log.error(err_msg)
        return

    try:
        await _getCASUser(event, entity, entity_id)
    except Exception as e:
        log.error(e)
        await event.edit("`CAS check failed`")
    return


DESC = "The CAS interface allows you to check a specific user for CAS bans."
register_cmd_usage(
    "cascheck",
    "[optional: <username/id>] or reply",
    "Checks if an user is CAS Banned"
)
register_module_desc(DESC)
register_module_info(
    name="CAS Interface",
    authors="nunopenim, prototype74",
    version="7.0.0"
)
