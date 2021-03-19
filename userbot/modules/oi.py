from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Woy Pantek People...`")
    sleep(3)
    await typew.edit("`Muka Kayak Kontol`")
    sleep(1)
    await typew.edit("`Gausa Caper Ya Ngentod`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.io(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Pantek People...`")
    sleep(3)
    await typew.edit("`Kerjaan Caper Aja Kontol`")
    sleep(1)
    await typew.edit("`Sadar Tolol Muka Kalian Jelek Kontol `")
# Create by myself @localheart


@register(outgoing=True, pattern='^.ll(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Lu Kaya Kontol ...`")
    sleep(3)
    await typew.edit("`Gausa Caper la Ngentod`")
    sleep(1)
    await typew.edit("`Gak Pantes Kontol!`")
# Create by myself @localheart
