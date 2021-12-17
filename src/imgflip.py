# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License
#
# Imgflip Meme Generator: https://imgflip.com


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
from userbot.sysutils.configuration import getConfig  # noqa: E402
from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from logging import getLogger  # noqa: E402
import os  # noqa: E402
import shlex  # noqa: E402

if not checkPkgByDist("requests"):
    installPkg("requests")

import requests  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)
_headers = {"User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) "
                           "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                           "Version/14.0 Safari/605.1.15")}
_imgflip_user = getConfig("IMGFLIP_USER", "")
_imgflip_pwd = getConfig("IMGFLIP_PWD", "")


async def get_memes(event):
    await event.edit("`Gathering data from Imgflip...`")
    imgflip_data = requests.get("https://api.imgflip.com/get_memes",
                                headers=_headers).json()

    if not imgflip_data.get("success"):
        await event.edit("`Failed to get data!`")
        return

    memes = imgflip_data.get("data", {}).get("memes", [])
    if not memes:
        await event.edit("`Data empty!`")
        return

    text = "**ID** | **Max. Captions** | **Meme Image**\n"
    text += "==================\n"
    for i, meme in enumerate(memes):
        meme_id = meme.get("id", "Unknown")
        meme_name = meme.get("name", "Unknown")
        meme_url = meme.get("url", "")
        meme_boxes = meme.get("box_count", "Unknown")
        text += f"`{meme_id}` | {meme_boxes} | [{meme_name}]({meme_url})\n"
        if i > 20:
            break
    text += "\n"
    text += ("Further meme images "
             f"[here](https://imgflip.com/popular_meme_ids)")
    await event.edit(text)
    return


async def caption_meme(event, img_id: int, cap_boxes: list):
    if not _imgflip_user:
        await event.edit("`No Imgflip username set! Please set your "
                         "Imgflip username to IMGFLIP_USER config in your "
                         "config file (e.g. IMGFLIP_USER='testname'). No "
                         "Imgflip account? Create your own account at "
                         "https://imgflip.com/signup`")
        return

    if not _imgflip_pwd:
        await event.edit("`No Imgflip password set! Please set your "
                         "Imgflip password to IMGFLIP_PWD config in your "
                         "config file (e.g. IMGFLIP_PWD='testpwsd'). No "
                         "Imgflip account? Create your own account at "
                         "https://imgflip.com/signup`")
        return

    parameters = {"template_id": img_id,
                  "username": _imgflip_user,
                  "password": _imgflip_pwd}
    for i, caption in enumerate(cap_boxes):
        parameters[f"boxes[{i}][text]"] = caption.get("text", "")

    await event.edit("`Generating caption to selected meme image...`")
    caption_data = requests.post("https://api.imgflip.com/caption_image",
                                 data=parameters).json()

    if not caption_data.get("success", False):
        await event.edit("**Failed to caption image!**\n"
                         "Message from Server: {}".format(
                             caption_data.get("error_message", "Unknown")))
        return

    caption_url = caption_data.get("data", {}).get("url", "")

    if not caption_url:
        await event.edit("`Unable to get image, as there is no URL!`")
        return

    img_file = os.path.join(getConfig("USERDATA"), "imgflip_recent.jpg")
    try:
        gen_image = requests.get(caption_url, headers=_headers)
        with open(img_file, "wb") as raw_image:
            raw_image.write(gen_image.content)
        raw_image.close()
    except Exception as e:
        log.error(e, exc_info=True)
        await event.edit("`Failed to save generated meme image`")
        return
    try:
        await event.client.send_file(event.chat_id, img_file)
        await event.delete()
    except Exception as e:
        log.error(e, exc_info=True)
        await event.edit("`Failed to send generated meme image to this chat`")
    return


async def recent_image(event):
    img_file = os.path.join(getConfig("USERDATA"), "imgflip_recent.jpg")
    if os.path.exists(img_file) and os.path.isfile(img_file):
        try:
            await event.client.send_file(event.chat_id, img_file)
            await event.delete()
        except Exception as e:
            log.error(e, exc_info=True)
            await event.edit("`Failed to send image to this chat`")
    else:
        await event.edit("`No recent generated meme image found`")
    return


@ehandler.on(command="imgflip", hasArgs=True, outgoing=True)
async def imgflip(event):
    args_from_event = event.pattern_match.group(1).split(" ", 1)
    if len(args_from_event) >= 2:
        first_arg, sec_arg = args_from_event
    else:
        first_arg, sec_arg = args_from_event[0], None

    if first_arg:
        if first_arg.lower() == "recent":
            await recent_image(event)
            return
        try:
            first_arg = int(first_arg)
        except:
            await event.edit("`Given ID is not a number!`")
            return
        if not sec_arg:
            await event.edit("`No text caption(s) given`")
            return
        sec_arg = shlex.split(sec_arg)
        if len(sec_arg) > 20:
            await event.edit("`Too many text caption(s) given. The "
                             "limit is 20 captions`")
            return
        text_captions = []
        for caption in sec_arg:
            text_captions.append({"text": caption})
        await caption_meme(event, first_arg, text_captions)
        return
    await get_memes(event)
    return


DESC = (
    "The Imgflip Meme Generator uses the API by Imgflip to generate known "
    "meme images with custom captions. This requires an Imgflip account to "
    "work. An account can be created at https://imgflip.com/signup. The API "
    "Server may has a rate-limit, so try to keep the requests to the server "
    "as minimum as possible. Up to 20 text captions are supported, as allowed "
    "by the API.\n\n"
    "This module requires the following configs:\n"
    "IMGFLIP_USER = \"YOUR_IMGFLIP_USERNAME\"\n"
    "IMGFLIP_PWD = \"YOUR_IMGFLIP_PASSWORD\""
)
register_cmd_usage(
    "imgflip",
    "[optional: <options>]",
    ("\n`.imgflip`\n"
     "Lists popular memes with their IMG IDs and names\n\n"
     "`.imgflip <IMG ID> <caption 1> [optional: <caption 2> <caption 3> "
     "<caption 4> etc.]`\n"
     "Generates custom captions to the target meme image (IMG ID) from "
     "caption 1 till 20. For example, caption 1 is in most cases the upper "
     "part or left part in an empty field in the meme image while caption 2 "
     "is the bottom part or right part in an another empty field in the meme "
     "image. However it depends on the meme image, so view the image first "
     "before you add captions to it. Sentences should be wrapped by quotes\n\n"
     "`.imgflip recent`\n"
     "Sends the last generated meme image to the chat")
)
register_module_desc(DESC)
register_module_info(
    name="Imgflip Meme Generator",
    authors="prototype74",
    version="1.1.0"
)
