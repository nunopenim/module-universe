from userbot import tgclient
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^\.dummy$", outgoing=True))
async def text(msg):
    await msg.edit("Ping!")
    return

