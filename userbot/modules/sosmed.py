# Port by Koala 🐨/@manuskarakitann
# Nyenyenye bacot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern="^.pint ?(.*)")
@register(outgoing=True, pattern="^.tik ?(.*)")
@register(outgoing=True, pattern="^.ig ?(.*)")
async def insta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Balas Ke Link Untuk Download Cok.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Link Ny Mana Njing?.`")
        return
    chat = "@SaveAsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Apalah Apalah Njing.")
        return
    await event.edit("`Proses Bentar Su...` 😡")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("@SaveAsbot'u `Unblock Dulu Lah Babi`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Wah Private Nih Su Hmmm."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"@manusiarakitann 🐨",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()


@register(outgoing=True, pattern="^.dez(?: |$)(.*)")
async def DeezLoader(event):
    if event.fwd_from:
        return
    dlink = event.pattern_match.group(1)
    if ".com" not in dlink:
        await event.edit("`Link Ny Mana Su? Mau Di Downlod Gak?`")
    else:
        await event.edit("**Lagi Download Bentar** 🎶")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
#                                   #
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("@DeezLoadBot'Unblok Dulu La Asu.")
            return
        await bot.send_file(event.chat_id, song, caption=details.text)

CMD_HELP.update(
    {
        "sosmed": ">`.pint`"
        "\nUsage: Download Media Dari Pinterest"
        "\n\n>`.tik`"
        "\nUsage: Download Vidip Tiktod Jedag Jedug."
        "\n\n>`.ig`"
        "\nUsage: Download Media Dari Instagram."
        "\n\n>`.dez`"
        "\nUsage: Download Lagu Via Deezloader"


    }
)
