# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

VERSION = "1.2.1"

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
import base64  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)


def encode(message_str):
    message_bytes = message_str.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_str = base64_bytes.decode('ascii')
    return base64_str


def decode(base64_str):
    base64_bytes = base64_str.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message_str = message_bytes.decode('ascii')
    return message_str


@ehandler.on(command="b64enc", hasArgs=True, outgoing=True)
async def encode_me(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        text = msg.message
    else:
        text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Give me something to encode!`")
        return
    encoded = encode(text)
    await event.edit("**BASE64 ENCODING**\n\nYour text: `{}`\n\n"
                     "Encoded text: `{}`".format(text, encoded))
    return


@ehandler.on(command="b64dec", hasArgs=True, outgoing=True)
async def decode_me(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        text = msg.message
    else:
        text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Give me something to decode!`")
        return
    try:
        decoded = decode(text)
    except:
        decoded = "FAILURE! Probably this is not a base64 message!"
    await event.edit("**BASE64 DECODING**\n\nBase64 text: `{}`\n\n"
                     "Decoded message: `{}`".format(text, decoded))
    return


DESC = "The base_64 module allows you to encode and decode messages in base64."
register_cmd_usage("b64enc", "<reply/text>", ("Encodes the given message "
                                              "in base64."))
register_cmd_usage("b64dec", "<reply/text>", ("Decodes the given message "
                                              "from base64."))

register_module_desc(DESC)
register_module_info(
    name="Base64 utilities",
    authors="nunopenim",
    version=VERSION
)
