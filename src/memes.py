# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License
#
# Note: This module should be taken with humor, no one should be
# offended by this


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


from userbot.include.aux_funcs import fetch_user  # noqa: E402
from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from telethon.events import MessageEdited, NewMessage  # noqa: E402
from logging import getLogger  # noqa: E402
import random  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)


SLAP_WEAPON = [
    "a chair",
    "a computer mouse",
    "an iPhone",
    "an iPad",
    "a MacBook",
    "a MacBook Pro",
    "an IndentationError",
    "a BO'OH'O'WA'ER",
    "a Bluescreen",
    "kernel panic",
    "a PS5",
    "a PS4",
    "a PS3",
    "a PS2",
    "a XBox 360",
    "a XBox One",
    "a XBox Series X",
    "a galaxy phone",
    "a remote control",
    "a keyboard",
    "software updates",
    "a windows cumulative update",
    "a book",
    "a rock",
    "a gaming pc",
    "a gaming laptop",
    "a thesis",
    "a TV",
    "a printer",
    "a lamp",
    "a heart monitor",
    "a sony camera",
    "a pen",
    "fake news",
    "a HTTP cookie",
    "paranormal KG state",
    "a building"
]


SLAP_TEXT = [
    "throws **{weapon}** at {person}'s face",
    "slaps {person} around a bit with **{weapon}**",
    "grabs up **{weapon}** and shoots it with a rocket launcher at {person}",
    "hits {person} with **{weapon}**",
    "starts hitting {person} repeatedly with **{weapon}**",
    "punches {person} with **{weapon}** like in Tom and Jerry",
    "slaps {person} in a 1vs1 fight with **{weapon}**",
    "hunts {person} with **{weapon}** in a forest"
]

# by @KebapciEBY and @nunopenim
GUN = [
    "AK-47",
    "M1911",
    "M1928 Thommy",
    "M1 Abrams tank",
    "M16",
    "M1 Garand",
    "Avtomat Federov",
    "CHAUCHAT",
    "Avtomat Kalashnikov",
    "M1928.A1 Thompson",
    "M1911.A1",
    ".45 ACP",
    "Colt 1911",
    "Ithaca 1911",
    "9mm Luger",
    "UZI",
    "Galil Ace",
    "StG 44",
    "MP 38",
    "MP 40",
    "StG 40",
    "Model 27",
    ".44 Magnum",
    "MP 28",
    "M8 con Tromboncino",
    "STEN",
    "M3 Carbine",
    "M3 Grease Gun",
    "M2 Carbine",
    "Kar98k",
    "Maschinengewehr 34",
    "Maschinengewehr 42",
    "HK MP5",
    "MP5",
    "Heckler & Koch G36 C",
    "Heckler & Koch G36",
    "HK G36 C",
    "HK G36",
    "SCAR FN",
    "Glock 17",
    "Glock 18",
    "Glock 19",
    "Glock 20",
    "Glock 21",
    "Glock 22",
    "Glock 23",
    "Glock 30",
    "Glock 40",
    "Glock 42",
    "Glock 44",
    "Glock 45",
    "Glock 48",
    "M1941 Johnson Rifle",
    "M1941 Johnson",
    "Nambu Type 2A",
    "Type 100",
    "FLAK",
    "Type 99 Arisaka",
    "Ribeyrolles 1918",
    "Panzerbüchse 39"
    "Panzerbüchse Boys",
    "M1897",
    "12 Gauge Automatic",
    "Drilling M30",
    "PPsh",
    "Sturmgewehr 40",
    "Sturmgewehr 44",
    "Maschinenpistole 38",
    "Maschinenpistole 40",
    "AK-44S",
    "Colt 44 Magnum",
    "AA-12",
    "ACR",
    "Desert Eagle",
    ".50",
    "FAL",
    "M-200 Intervention",
    "M249 Saw",
    "M4A1",
    "FN P90",
    "Suomi KP31",
    "PDR",
    "PPsh-41",
    "SPAS-12",
    "Beretta M9",
    "SCAR-H",
    "Thompson M1921",
    "M1921",
    "HK USP",
    "Heckler & Koch USP",
    "XD-9",
    "1887 Mare S Leg",
    "M1912 Repetierpistole",
    "Ruby",
    "AK-45 Korovin",
    "AK-45 KOROVIN",
    "AVTOMAT KALASHNIKOV 45 KOROVIN",
    "AK-74",
    "Avtomat Kalashnikov 74",
    "Avtomat Kalashnikov 47",
    "AR-70",
    "Fliegerfaust",
    "PIAT",
    "M1A1 Bazooka",
    "Bazooka",
    "Bangalore",
    "AK-5C",
    "Avtomat Kalashnikov 5C",
    "Ameli",
    "Welgun",
    "Coach Gun",
    "HK 417",
    "Heckler & Koch 417",
    "Honey Badger",
    "Sjögren",
    "M1898",
    "Krag-Jørgensen",
    "Krag-Jørgensen M1898",
    "Maschinengewehr 15",
    "MG 15",
    "Madsen MG",
    "Panzerfaust",
    "PANZERFAUST",
    "PANZERABWEHRMINE",
    "Panzerabwehrmine",
    "SCAR PDW",
    "XD59",
    "Model 37 shotgun"
]

# by @KebapciEBY and @nunopenim
PUNCH = [
    "punches",
    "RKOs",
    "smashes the skull of",
    "throws a pipe wrench at"
]

# by @KebapciEBY and @nunopenim
PUNCH_TEMPLATES = [
    "{punches} {victim} to assert dominance.",
    "{punches} {victim} to see if they shut the fuck up for once.",
    "{punches} {victim} because they were asking for it.",
    "It's over {victim}, they have the high ground.",
    "performs a superman punch on {victim}, {victim} is rekt now.",
    "makes {victim} go on tiktok. {victim} gets cancer. ",
    "kills off {victim} with a T.K.O",
    "attacks {victim} with a billiard cue. A bloody mess.",
    "disintegrates {victim} with a MG.",
    "A hit and run over {victim} performed by me",
    "punches {victim} into the throat. Warning, choking hazard!",
    "drops a piano on top of {victim}. A harmonical death.",
    "throws rocks at {victim}",
    "forces {victim} to drink chlorox. What a painful death.",
    "got sliced in half by {victim}'s katana.",
    "makes {victim} fall on their sword. A stabby death lol.",
    "kangs {victim} 's life energy away.",
    "shoots {victim} into a million pieces. Hasta la vista baby.",
    "drops the frigde on {victim}. Beware of crushing.",
    "engages a guerilla tactic on {victim}",
    "ignites {victim} into flames. IT'S LIT FAM.",
    "pulls a loaded 12 gauge on {victim}.",
    ("throws a Galaxy Note7 into {victim}'s general direction. A bombing "
     "massacre."),
    ("walks with {victim} to the end of the world, then pushes him over the "
     "edge."),
    "performs a Stabby McStabby on {victim} with a butterfly.",
    "cuts {victim}'s neck off with a machete. A blood bath.",
    ("secretly fills in {victim}'s cup with Belle Delphine's Gamer Girl "
     "Bathwater instead of water. Highly contagious herpes."),
    "is tea cupping on {victim} after a 1v1, to assert their dominance.",
    "asks for {victim}'s last words. {victim} is ded now.",
    "lets {victim} know their position.",
    "makes {victim} to his slave. What is your bidding? My Master.",
    "forces {victim} to commit suicide.",
    "shouts 'it's garbage day' at {victim}.",
    "throws his axe at {victim}.",
    "is now {victim}'s grim reaper.",
    "slappety slap's {victim}.",
    "ends the party.",
    "will never know what hit them.",
    "breaks {victim}'s neck like a kitkat.",
    "flings knives at {victim}.",
    "gangs {victim} in a drive by.",
    "Thanks to my airstrike, {victim} is no more.",
    "waterboard's {victim}.",
    "hangs {victim} upside down.",
    "breaks (victim)'s skull with a PS4.",
    "throws Xbox controller batteries at {victim}'s face.",
    "shouts 'Look at me, I'm the Captain now.' at {victim}.",
    "puts {victim} in their place.",
    "poisons {victim}'s meal, it was their last meal.",
    "burns {victim} into ashes.",
    "bites in the dust.",
    "stabs {victim} in their back, what a way to die.",
    "uses {victim} to play Fruit Ninja.",
    "blueballs {victim}.",
    "makes the fool die a fool's death.",
    "orders Agent 47 on {victim}'s ass.",
    "gets struck by a lightning. Warning, high tension.",
    "breaks all of {victim}'s bones.",
    "Someone save {victim} because I is about to murder them.",
    "throws {victim} into a volcano.",
    "chokes {victim} through the force.",
    "throws their lightsaber at {victim}.",
    "orders a full broadside on {victim}.",
    "deploys the garrison on {victim}.",
    "lets freeze {victim} to death.",
    "throws {victim} across the room by the force.",
    "makes {victim} go crazy by high pitch sounds.",
    "rolls over {victim} with a Panzerkampfwagen VI Tiger.",
    "blows {victim} up with a bazooka.",
    "plays Sniper Elite with {victim} as the target.",
    "yeets {victim}'s ass.)",
    "puts a grenade in {victim}'s hood.",
    "throws an iPhone 11 Pro Max at {victim}'s face.",
    "throws a Galaxy S20 Ultra 5G at {victim}'s face.",
    "draws a dick on {victim}'s forehead.",
    "cuts open {victim}'s throat. Very bloody.",
    "shoots {victim} to dust with a {gun}.",
    "lands a headshot on {victim} with their {gun}.",
    "shoots down {victim} with a {gun}."
    "stashes a Glock."
    "lures {victim} on a minefield.",
    "wins over {victim} in a western 1v1.",
    "plays robbers and gendarmes with {victim}.",
    "tries their new {gun} on {victim}.",
    "steals all of {victim}'s money. Now they're broke af.",
    "drops a TV on {victim}.",
    "throws their Apple TV at {victim}.",
    "hijacks {victim}'s ship.",
    "makes {victim} sign their death certificate.",
    "kangs everything what {victim} owns.",
    "manipulates {victim}'s breaks.",
    "ties {victim} down on the train tracks.",
    "chops {victim}'s arm off with their lightsaber."
]

# From wikipedia:
# https://en.wikipedia.org/wiki/Transformation_of_text#Upside-down_text
UPSIDEDOWN_TABLE = {
    "A": "Ɐ",
    "B": "ꓭ",
    "C": "Ɔ",
    "D": "ꓷ",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "⅁",
    "J": "ꓩ",
    "K": "ꓘ",
    "L": "⅂",
    "M": "ꟽ",
    "P": "Ԁ",
    "Q": "ტ",
    "R": "ꓤ",
    "T": "Ʇ",
    "U": "Ո",
    "V": "Ʌ",
    "W": "M",
    "Y": "⅄",
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ᵷ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ſ̣",
    "k": "ʞ",
    "l": "ꞁ",
    "m": "ɯ",
    "n": "u",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "y": "ʎ",
    "1": "⇂",
    "2": "ᘔ",
    "3": "Ɛ",
    "4": "߈",
    "5": "ဌ",
    "6": "9",
    "7": "ㄥ",
    "9": "6",
    "0": "0",
    "!": "¡",
    "?": "¿",
    "&": "⅋",
    "_": "‾",
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
    "\"": "„",
    "'": ",",
    ".": "˙",
    "\\": "/",
    "`": ","
}


@ehandler.on(command="iq", hasArgs=True, outgoing=True)
async def iq(event):
    user = await fetch_user(event)

    if not user:
        return

    if user.is_self:
        # only if you think you're smart, you're smart, get it?
        iq = random.randint(150, 250)
        await event.edit(f"I have an IQ of **{iq}**")
        return

    iq = random.randint(-50, 250)
    if user.deleted:
        await event.edit(f"Deleted Account has an IQ of **0**")
    elif user.username:
        await event.edit(f"@{user.username} has an IQ of **{iq}**")
    else:
        await event.edit(f"[{user.first_name}](tg://user?id={user.id}) "
                         f"has an IQ of **{iq}**")
    return


@ehandler.on(command="idiot", hasArgs=True, outgoing=True)
async def idiot_meter(event):
    user = await fetch_user(event)

    if not user:
        return

    if user.is_self:
        # no idiot?
        await event.edit("I am **100%** an idiot because I tested "
                         "this on myself")
        return

    percentage = random.randint(0, 100)
    if user.deleted:
        person = "Deleted Account"
    elif user.username:
        person = f"@{user.username}"
    else:
        person = f"[{user.first_name}](tg://user?id={user.id})"

    await event.edit(f"{person} is **{percentage}%** an idiot")
    return


@ehandler.on(command="slap", hasArgs=True, outgoing=True)
async def slap(event):
    user = await fetch_user(event)

    if not user:
        return

    if user.is_self:
        # still no idiot?
        await event.edit("I won't slap myself lol")
        return

    if user.deleted:
        person = "Deleted Account"
    elif user.username:
        person = f"@{user.username}"
    else:
        person = f"[{user.first_name}](tg://user?id={user.id})"

    slap_weapon = random.choice(SLAP_WEAPON)
    slap_text = random.choice(SLAP_TEXT)
    await event.edit("..." + slap_text.format(weapon=slap_weapon,
                                              person=person))
    return


# by @KebapciEBY and @nunopenim
@ehandler.on(command="punch", hasArgs=True, outgoing=True)
async def punch_in_yoo_face_lol(event):
    user = await fetch_user(event)

    if not user:
        return

    if user.is_self:
        await event.edit("Can't punch myself *loading 12 gauge buckshot "
                         "in my shotgun!!*")
        return

    if user.deleted:
        person = "Deleted Account"
    elif user.username:
        person = f"@{user.username}"
    else:
        person = f"[{user.first_name}](tg://user?id={user.id})"

    weapon = random.choice(GUN)
    punch = random.choice(PUNCH)
    punch_text = random.choice(PUNCH_TEMPLATES)
    await event.edit("..." + punch_text.format(victim=person,
                                               punches=punch,
                                               gun=weapon))
    return


@ehandler.on(command="f", alt="F", hasArgs=True, outgoing=True)
async def press_f_to_pay_respects(event):
    arg_from_event = event.pattern_match.group(1)
    if not arg_from_event:
        await event.edit("`Plox gib an emoji or symbol lol`")
        return
    if len(arg_from_event) > 3:
        await event.edit("`Too many symbols or emojis. Maximum length is 3`")
        return
    f = arg_from_event * 7 + "\n"   # -------
    f += arg_from_event * 7 + "\n"  # -------
    f += arg_from_event * 2 + "\n"  # --
    f += arg_from_event * 2 + "\n"  # --
    f += arg_from_event * 5 + "\n"  # -----
    f += arg_from_event * 5 + "\n"  # -----
    f += arg_from_event * 2 + "\n"  # --
    f += arg_from_event * 2 + "\n"  # --
    f += arg_from_event * 2 + "\n"  # --
    f += arg_from_event * 2         # --
    await event.edit(f)  # Very F
    return


@ehandler.on(command="oof", outgoing=True)
async def oof(event):
    oof = "oof"
    for _ in range(14):
        oof = "o" + oof
        await event.edit(oof)  # Very big oof
    return


def mock_them_all(text: str) -> str:
    mocked_chars = []
    for char in list(text):
        if random.getrandbits(1):
            mocked_chars.append(char.lower() if char.isupper()
                                else char.upper())
        else:
            mocked_chars.append(char)
    mocked_text = "".join(mocked_chars)
    return mocked_text if mocked_text else text


@ehandler.on(command="mock", hasArgs=True, outgoing=True)
async def mock(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        msg = msg.message
    else:
        msg = event.pattern_match.group(1)

    mocked_text = mock_them_all(msg if msg else "No text to mock!")
    await event.edit(f"`{mocked_text}`")
    return


@ehandler.on(command="reverse", hasArgs=True, outgoing=True)
async def reverse(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        msg = msg.message
    else:
        msg = event.pattern_match.group(1)

    if not msg:
        await event.edit("`No text given to reverse!`")
        return

    try:
        msg = msg[::-1]
        await event.edit(msg)
    except Exception as e:
        log.warning(f"[reverse]: {e}")
        await event.edit("`Too bad! I couldn't reverse this "
                         "text or message...`")
    return


@ehandler.on(command="flip", hasArgs=True, outgoing=True)
async def upsidedown(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        msg = msg.message
    else:
        msg = event.pattern_match.group(1)

    if not msg:
        await event.edit("`¡dᴉꞁɟ oʇ uǝʌᴉᵷ ʇxǝʇ oN`")
        return

    try:
        upsidedown_chars = []
        for char in list(msg):
            for key, value in UPSIDEDOWN_TABLE.items():
                if char == key:
                    upsidedown_chars.append(value)
                    break
                elif char == value:
                    upsidedown_chars.append(key)
                    break
            else:
                upsidedown_chars.append(char)
        upsidedown_text = "".join(upsidedown_chars)
        upsidedown_text = upsidedown_text[::-1]
        await event.edit(upsidedown_text)
    except Exception as e:
        log.warning(f"[flip]: {e}")
        await event.edit("`Too bad! I couldn't flip this text or message...`")
    return


DESC = (
    "Meeeeeeeeeeeemes!!!111!!11!!1!\n"
    "Enjoy the funny commands this module does offer to fool or having fun "
    "with your friends. This module should be taken with humor, no one should "
    "feel being offended by this"
)
register_cmd_usage(
    "iq",
    "[username or id] or reply",
    "Check someone's IQ, or your own?"
)
register_cmd_usage(
    "idiot",
    "[username or id] or reply",
    "Uh oh, idiot spotted"
)
register_cmd_usage(
    "slap",
    "[username or id] or reply",
    "Slaps a person"
)
register_cmd_usage(
    "punch",
    "[username or id] or reply",
    "A punch in someone's face lol"
)
register_cmd_usage(
    "f",
    "emoji or symbol",
    "Press F to pay respects"
)
register_cmd_usage(
    "oof",
    None,
    "Very oooooooooooof"
)
register_cmd_usage(
    "mock",
    "text or reply",
    mock_them_all("Mock them all!")
)
register_cmd_usage(
    "reverse",
    "text or reply",
    "Read everything from right to left, or from left to right?"
)
register_cmd_usage(
    "flip",
    "text or reply",
    "Change given text or replied message to upside down"
)
register_module_desc(DESC)
register_module_info(
    name="Memes",
    authors="prototype74",
    version="1.0.0"
)
