from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^\\.kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAMET KONTOLLL**")
    sleep(3)
    await typew.edit("`TOLOL TOLOL TOLOL!!!`")
    sleep(3)
    await typew.edit("`CAPER AJA KONTOLLL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**ANGKASA BAWA BOTOL**")
    sleep(3)
    await typew.edit("`KALIAN SEMUA JAMET TOLOL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**ANGKASA BAWA BOTOL**")
    sleep(3)
    await typew.edit("`KALIAN SEMUA JAMET TOLOLLL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**HALO BABUUU! GUA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`PUNTENNNN.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**HALO BABUUU! GUA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`PUNTENNNN.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Bentar Gua Jawab Salam Lu...`")
    sleep(1)
    await typew.edit("`وَعَلَيْكُمُ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Bentar Gua Jawab Salam Lu...`")
    sleep(1)
    await typew.edit("`وَعَلَيْكُمُ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**STRAWBERRY MANGGA APEL**")
    sleep(3)
    await typew.edit("`SORRY GAK LEVEL!`")


@register(outgoing=True, pattern='^\\.W(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**STRAWBERRY MANGGA APEL**")
    sleep(3)
    await typew.edit("`SORRY GAK LEVEL!`")


CMD_HELP.update({
    "salam":
    "`.P`\
\nUsage: Untuk Memberi Hujatan.\
\n\n`.L`\
\nUsage: Untuk Menjawab Salam.\"
\n\n`.W`
    \nUsage: Untuk Menolak Jamet.\"

})
