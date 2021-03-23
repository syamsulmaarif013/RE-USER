
# Port by Koala @manusiarakitann
# jangan datang hanya saat perlu :) aku bukan tuhan

from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern='^.bin ?(.*)')
async def _(event):
    if event.fwd_from:
        return
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Sabar anjeng lagi prosess 😅😁...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await event.client.send_message(chat, "/bin {}".format(danish))
            respond = await response
        except YouBlockedUserError:
            await event.reply("Tolol! Unblock @Carol5_bot dulu ")
            return
        if respond.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless 😂😂")
        else:

            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@register(outgoing=True, pattern='^.vbv ?(.*)')
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Sabar asu gi prosesss....")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await event.client.send_message(chat, "/vbv {}".format(danish))
            respond = await response
        except YouBlockedUserError:
            await event.reply("Goblok! Unblock @Carol5_bot dulu ")
            return
        if respond.text.startswith(" "):
            await event.edit("Botnya Mati Asu 😂😂")
        else:

            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@register(outgoing=True, pattern='^.key ?(.*)')
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await event.client.send_message(chat, "/key {}".format(danish))
            response = await response
        except YouBlockedUserError:
            await event.reply("Asu! Unblock @Carol5_bot dulu ")
            return
        if response.text.startswith(" "):
            await event.edit("Bot gi matii asuuu 😂😂")
        else:
            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@register(outgoing=True, pattern='^.iban ?(.*)")
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Proses asuuu...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await event.client.send_message(chat, "/iban {}".format(danish))
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolol! Unblock @Carol5_bot dulu ")
            return
        if response.text.startswith(" "):
            await event.edit("Bot gi mati asuuu 😂😂")
        else:
            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()

CMD_HELP.update(
    {
        "binner": ">`.bin`"
        "\nUsage: Buat Bin CC"
        "\n\n>`.vbv`"
        "\nUsage: Liat Aja Sendiri, Gua Gangerti."
        "\n\n>`.key`"
        "\nUsage: Liat Aja Sendiri, Gua Gangerti."
        "\n\n>`.iban`"
        "\nUsage: Liat Aja Sendiri, Gua Gangerti."


    }
)
