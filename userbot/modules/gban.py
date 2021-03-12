# Fixed by:koala @mixiologist
# Lord Userbot

from userbot import ALIVE_NAME, CMD_HELP
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import register
from telethon.tl.types import MessageEntityMentionName


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Gabisa Tolol, Tanpa ID`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("`Wahh Ngebug Anjing... Mohon Lapor Ke Angkasa` @leoangkasaaa", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@register(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Lu Harus Di Global Banned, Karena Faktor Face!`")
    else:
        dark = await dc.edit("`💣 Global Banned Segera Di Proses`")
    me = await userbot.client.get_me()
    await dark.edit(f"`💣 Terdeteksi Muka Jelek, Rasakan Dibanned Secara Global`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(f"`Anjeng Error Asu😭`")
    if user:
        if user.id == 1073848376:
            return await dark.edit(
                f"`Elu Ga Bisa GBAN Gua Asu, Karena Faktor Face😡`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"`💣 Global Banned Lagi Proses`")
            except BaseException:
                b += 1
    else:
        await dark.edit(f"`Reply Pesannya Goblok`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**Syntax Error Asu! Itu Bocah Pantek Udah Di GBAN Ngentod.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**🚀 EKSEKUTOR:** `{ALIVE_NAME}`\n**❂ Nama Jamet:** [{user.first_name}](tg://user?id={user.id})\n**❂ Hukuman:** `Global Banned`"
    )


@register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`🚀 Mengampuni PANTEK PEOPLE Yang Buriq`")
    else:
        dark = await dc.edit("`🚀 Mengampuni SI PANTEK Sedang Di Proses`")
    me = await userbot.client.get_me()
    await dark.edit(f"`PANTEK PEOPLE Telah Di Ampuni, Lain Kali Gausah Caper ya ASUUUU...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Syntax Eror Asu 🚫`")
    if user:
        if user.id == 1073848376:
            return await dark.edit("**Gua Kebal Asu, Makanya Ganteng KONTOLL...**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"`🚀 Pengampunan Pantek People... Sabar ngentod... `")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Balas Pesannya Ngentod`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Lawak Lu Badut? Dia Ga Masuk GBAN List Lu Goblok.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**🚀 EKSEKUTOR:** `{ALIVE_NAME}`\n**❂ nama Jamet:** [{user.first_name}](tg://user?id={user.id})\n**❂ Pengampunan:** `Membatalkan Global Banned`"
    )


CMD_HELP.update({
    "gban": "\
`.gban`\
\nUsage: ✒ Melakukan Global Banned Untuk PANTEK PEOPLE Yang Meresahkan.\
\n\n`.ungban`\
\nUsage: ✒ Mengampuni Pantek People Yang Jelek "
})
