# Copyright 2020 nunopenim @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License
#
# Special thanks to HitaloSama @github, from HitsukiNetwork, for the
# idea and partial implementation in his Group Manager Bot, @Hitsuki

from userbot import MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from userbot.sysutils.event_handler import EventHandler
import requests
from bs4 import BeautifulSoup as bs
from os.path import basename

VERSION = "1.1.0"
ehandler = EventHandler()
COMBOT_STICKERS_URL = "https://combot.org/telegram/stickers?q="

@ehandler.on(pattern=r"^\.stksearch(?: |$)(.*)", outgoing=True)
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

DESC = "The sticker_search module allows you to search for sticker packs! "\
       "It is powered by Combot."
USAGE = "`.stksearch` <name>\nUsage: Searches in Combot's Telegram Sticker "\
        "Catalogue for sticker packs that contain the specified name."

MODULE_DESC.update({basename(__file__)[:-3]: DESC})
MODULE_DICT.update({basename(__file__)[:-3]: USAGE})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name="Sticker Searcher", version=VERSION)})
