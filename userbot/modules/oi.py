from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Woy Jamet Tolol...`")
    sleep(3)
    await typew.edit("`Muka Kayak Kontol`")
    sleep(1)
    await typew.edit("`Gausa Caper Lu Ngentod`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.io(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Anjeng! Jamet Pantek...`")
    sleep(3)
    await typew.edit("`Kerjaan Caper Aja Kontol`")
    sleep(1)
    await typew.edit("`Sadar Tolol Muka Kalian Jelek Kontol `")
# Create by myself @localheart


@register(outgoing=True, pattern='^.ui(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Muka Lu Kaya Kontol ...`")
    sleep(3)
    await typew.edit("`Gausa Caper la Ngentod!`")
    sleep(1)
    await typew.edit("`Gak Pantes Kontol!`")
# Create by myself @localheart

CMD_HELP.update({
    "Hujatan":
    "`.oi`\
\nUsage: Ngatain Jamet.\
\n\n`.io`\
\nUsage: Hina Jamet.\
\n\n`ui`\
\nUsage: Hujat Orang."
})
