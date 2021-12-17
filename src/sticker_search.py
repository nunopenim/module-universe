# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License
#
# Special thanks to HitaloSama @github, from HitsukiNetwork, for the
# idea and partial implementation in his Group Manager Bot, @Hitsuki


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
from logging import getLogger  # noqa: E402
from subprocess import check_call  # noqa: E402
import requests  # noqa: E402

if not checkPkgByDist("beautifulsoup4"):
    installPkg("beautifulsoup4")

from bs4 import BeautifulSoup as bs  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)
COMBOT_STICKERS_URL = "https://combot.org/telegram/stickers?q="


@ehandler.on(command="stksearch", hasArgs=True, outgoing=True)
async def stksearch(message):
    arg = message.pattern_match.group(1)
    if len(arg) == 0:
        await message.edit('Provide some name to search for pack.')
        return
    text = requests.get(COMBOT_STICKERS_URL + arg).text
    soup = bs(text, 'lxml')
    results = soup.find_all("a", {'class': "sticker-pack__btn"})
    titles = soup.find_all("div", "sticker-pack__title")
    if not results:
        await message.edit('No results found!')
        return
    reply = "Stickers for {}:\n".format(arg)
    count = 1
    for result, title in zip(results, titles):
        link = result['href']
        reply += "\n{}. [{}]({})".format(count, title.get_text(), link)
        count += 1
    await message.delete()
    await message.respond(reply)
    return


DESC = (
    "The sticker_search module allows you to search for sticker packs! It is "
    "powered by Combot."
)
register_cmd_usage(
    "stksearch",
    "<name>",
    ("Searches in Combot's Telegram Sticker Catalogue for sticker packs that "
     "contain the specified name.")
)
register_module_desc(DESC)
register_module_info(
    name="Sticker Searcher",
    authors="nunopenim",
    version="1.2.2"
)
