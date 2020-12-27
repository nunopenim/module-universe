# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot import MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from userbot.sysutils.event_handler import EventHandler
import base64
from os.path import basename

VERSION = "1.1.0"
ehandler = EventHandler()

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

@ehandler.on(pattern=r"^\.b64enc(?: |$)(.*)", outgoing=True)
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
    await event.edit("**BASE64 ENCODING**\n\nYour text: `{}`\n\nEncoded text: `{}`".format(text, encoded))
    return

@ehandler.on(pattern=r"^\.b64dec(?: |$)(.*)", outgoing=True)
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
    await event.edit("**BASE64 DECODING**\n\nBase64 text: `{}`\n\nDecoded message: `{}`".format(text, decoded))
    return

DESC = "The base_64 module allows you to encode and decode messages in base64."
USAG = "`.b64enc` <reply/text>"\
       "\nUsage: Encodes the given message in base64."\
       "\n\n`.b64dec` <reply/text>"\
       "\nUsage: Decodes the given message from base64."

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAG})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Base64 utilities", version=VERSION)})
