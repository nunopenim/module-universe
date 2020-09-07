from tg_userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^\.dummy$", outgoing=True))
async def text(msg):
    await msg.edit("Ping!")
    return

MODULE_DESC.update({basename(__file__)[:-3]: "Dummy module designed during testing"})
MODULE_DICT.update({basename(__file__)[:-3]: ".dummy with print 'ping' to see if it is working"})
