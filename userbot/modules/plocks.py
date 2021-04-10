# PORT BY @Vckyouuu / For FromVT-UserBot / @VckyouuBitch FROM CAT USERBOT
# BASED ON PLUGINS

import base64
from telethon import functions
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import ChatBannedRights
from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern=r"^\.plock(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    if not event.is_group:
        return await event.edit("`Bodoh! ,Ini Bukan Grup Yang Bisa Dikunci`")
    chat_per = (await event.get_chat()).default_banned_rights
    result = await bot(
        functions.channels.GetParticipantRequest(
            channel=peer_id, user_id=reply.from_id)
    )
    admincheck = await event.client(is_admin, peer_id, reply.from_id)
    if admincheck:
        return await event.edit("`User Ini Adalah Admin! Lu Gabisa Gunakan Pada Dia.`")
    kampang = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "msg":
        if msg:
            return await event.edit("`Grup Ini Telah Dikunci Untuk Ijin Pesan.`"
                                    )
        if umsg:
            return await event.edit("`Pengguna Ini Telah Dikunci Untuk Ijin Pesan.`"
                                    )
        umsg = True
        locktype = "messages"
    elif input_str == "media":
        if media:
            return await event.edit("`Grup Ini Telah Dikunci Untuk Ijin Kirim M0edia`"
                                    )
        if umedia:
            return await event.edit("`Pengguna Ini Telah Dikunci Untuk Ijin Kirim Media`"
                                    )
        umedia = True
        locktype = "media"
    elif input_str == "sticker":
        if sticker:
            return await event.edit("`Grup ini telah dikunci untuk ijin kirim stiker.`"
                                    )
        if usticker:
            return await event.edit("`Pengguna ini telah dikunci untuk ijin kirim stiker.`"
                                    )
        usticker = True
        locktype = "stickers"
    elif input_str == "preview":
        if embed_link:
            return await event.edit("`Grup ini telah dikunci untuk ijin kirim tautan.`"
                                    )
        if uembed_link:
            return await event.edit("`Pengguna ini telah dikunci untuk ijin kirim tautan.`"
                                    )
        uembed_link = True
        locktype = "preview links"
    elif input_str == "gif":
        if gif:
            return await event.edit("`Grup ini telah dikunci untuk ijin kirim GIfs`"
                                    )
        if ugif:
            return await event.edit("`Pengguna ini telah dikunci untuk ijin kirim GIFs`"
                                    )
        ugif = True
        locktype = "GIFs"
    elif input_str == "game":
        if gamee:
            return await event.edit("`Grup ini telah dikunci untuk ijin kirim permainan`"
                                    )
        if ugamee:
            return await event.edit("`Pengguna ini telah dikunci untuk ijin kirim permainan`"
                                    )
        ugamee = True
        locktype = "games"
    elif input_str == "inline":
        if ainline:
            return await event.edit("`Grup ini telah dikunci untuk ijin menggunakan inline bot`"
                                    )
        if uainline:
            return await event.edit("`Pengguna ini telah dikunci untuk ijin menggunakan inline bot`"
                                    )
        uainline = True
        locktype = "inline bots"
    elif input_str == "poll":
        if gpoll:
            return await event.edit("`Grup ini telah dikunci untuk ijin kirim pemilihan`"
                                    )
        if ugpoll:
            return await event.edit("`Pengguna ini telah dikunci untuk ijin kirim pemilihan`"
                                    )
        ugpoll = True
        locktype = "polls"
    elif input_str == "invite":
        if adduser:
            return await event.edit("`Grup ini telah dikunci untuk ijin tambahkan anggota`"
                                    )
        if uadduser:
            return await event.edit("`Pengguna ini telah dikunci untuk ijin tambahkan anggota`"
                                    )
        uadduser = True
        locktype = "invites"
    elif input_str == "pin":
        if cpin:
            return await event.edit("`Grup ini telah dikunci untuk ijin sematkan pesan.`",
                                    )
        if ucpin:
            return await event.edit("`Pengguna ini telab dikunci untuk ijin sematkan pesan`",
                                    )
        ucpin = True
        locktype = "pins"
    elif input_str == "info":
        if changeinfo:
            return await event.edit("`Grup ini telah di kunci untuk merubah info grup.`",
                                    )
        if uchangeinfo:
            return await event.edit("`Pengguna ini telah dikunci untuk merubah info grup`",
                                    )
        uchangeinfo = True
        locktype = "chat info"
    elif input_str == "all":
        umsg = True
        umedia = True
        usticker = True
        ugif = True
        ugamee = True
        uainline = True
        uembed_link = True
        ugpoll = True
        uadduser = True
        ucpin = True
        uchangeinfo = True
        locktype = "everything"
    else:
        if input_str:
            return await event.edit(f"**Tipe Kunci Salab :** `{input_str}`", time=5
                                    )

        return await event.edit_or_reply("`Saya tidak bisa kunci apapun!`")
    try:
        kampang = Get(kampang)
        await event.client(kampang)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await event.edit_or_reply(f"`Mengunci {locktype} untuk penguna ini!`")
    except BaseException as e:
        await event.edit(f"`Apakah saya memiliki hak untuk lakukan itu?`\n\n**Error:** `{str(e)}`",
                         time=5,
                         )


@register(outgoing=True, pattern=r"^\.unplock(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    if not event.is_group:
        return await edit_delete(event, "`Bodoh! ,Ini Bukan Grup Yang Bisa Dikunci `")
    chat_per = (await event.get_chat()).default_banned_rights
    result = await bot(
        functions.channels.GetParticipantRequest(
            channel=peer_id, user_id=reply.from_id)
    )
    admincheck = await event.client(is_admin, peer_id, reply.from_id)
    if admincheck:
        return await event.edit("`Pengguna Ini Adalah Admin, Tidak Bisa Kunci Dia`")
    kampang = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "msg":
        if msg:
            return await event.edit("`Grup dikunci untuk kirim pesan.`"
                                    )
        if not umsg:
            return await event.edit("`Pengguna telah dibuka untuk kirim pesan.`"
                                    )
        umsg = False
        locktype = "messages"
    elif input_str == "media":
        if media:
            return await event.edit("`Grup telah dikunci untuk kirim media`")
        if not umedia:
            return await event.edit("`Pengguna telah dibuka untuk kirim media`"
                                    )
        umedia = False
        locktype = "media"
    elif input_str == "sticker":
        if sticker:
            return await event.edit("`Grup telah dikunci untuk kirim stiker`"
                                    )
        if not usticker:
            return await event.edit("`Pengguna telah dibuka untuk kirim stiker`"
                                    )
        usticker = False
        locktype = "stickers"
    elif input_str == "preview":
        if embed_link:
            return await event.edit("`Grup telah dikunci untuk kirim tautan`"
                                    )
        if not uembed_link:
            return await event.edit("`Pengguna telah dibuka untuk kirim tautan`"
                                    )
        uembed_link = False
        locktype = "preview links"
    elif input_str == "gif":
        if gif:
            return await event.edit("`Grup telah dikunci untuk kirim GIFs`")
        if not ugif:
            return await event.edit("`Pengguna telah dibuka untuk kirim GIFs`"
                                    )
        ugif = False
        locktype = "GIFs"
    elif input_str == "game":
        if gamee:
            return await event.edit("`Grup telah dikunci untuk kirim permainan`")
        if not ugamee:
            return await event.edit("`Pengguna telah dibuka untuk kirim permainan`"
                                    )
        ugamee = False
        locktype = "games"
    elif input_str == "inline":
        if ainline:
            return await event.edit("`Grup telah dikunci untuk kirim bot inline`"
                                    )
        if not uainline:
            return await event.edit("`Pengguna telah dibuka untuk kirim bot inline`"
                                    )
        uainline = False
        locktype = "inline bots"
    elif input_str == "poll":
        if gpoll:
            return await event.edit("`Grup telah dikunci untuk kirim pemilihan`")
        if not ugpoll:
            return await event.edit("`Pengguna telah dibuka untuk kirim pemilihan`"
                                    )
        ugpoll = False
        locktype = "polls"
    elif input_str == "invite":
        if adduser:
            return await event.edit("`Grup dikunci untuk tambahkan anggoga`"
                                    )
        if not uadduser:
            return await event.edit("`Pengguna telah dibuka untuk tambahkan anggota`"
                                    )
        uadduser = False
        locktype = "invites"
    elif input_str == "pin":
        if cpin:
            return await event.edit("`Grup dikunci untuk semat pesan`",
                                    )
        if not ucpin:
            return await event.edit("`Pengguna telah dibuka untuk semat pesan`",
                                    )
        ucpin = False
        locktype = "pins"
    elif input_str == "info":
        if changeinfo:
            return await event.edit("`Grup telah dikunci untuk ubah info grup`",
                                    )
        if not uchangeinfo:
            return await event.edit("`Pengguna ini telah dibuka untuk ubah info grup`",
                                    )
        uchangeinfo = False
        locktype = "chat info"
    elif input_str == "all":
        if not msg:
            umsg = False
        if not media:
            umedia = False
        if not sticker:
            usticker = False
        if not gif:
            ugif = False
        if not gamee:
            ugamee = False
        if not ainline:
            uainline = False
        if not embed_link:
            uembed_link = False
        if not gpoll:
            ugpoll = False
        if not adduser:
            uadduser = False
        if not cpin:
            ucpin = False
        if not changeinfo:
            uchangeinfo = False
        locktype = "everything"
    else:
        if input_str:
            return await event.edit(f"**Invalid lock type :** `{input_str}`", time=5
                                    )

        return await event.edit_or_reply("`I can't lock nothing !!`")
    try:
        kampang = Get(kampang)
        await event.client(kampang)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await event.edit_or_reply(f"`Buka {locktype} untuk pengguna ini!`")
    except BaseException as e:
        await event.edit(f"`Apakah Saya Punya Ijin Itu ??`\n\n**Error:** `{str(e)}`",
                         time=5,
                         )

CMD_HELP.update({
    "plock":
    "`.plock <all atau Jenis>` atau `.unplock <all atau Jenis>`\
\nFungsi: Memungkinkan anda mengunci atau membuka kunci, beberapa jenis pesan dalam obrolan.\
\n[Anda Harus Jadi Admin Grup Untuk Menggunakan Perintah!]\
\n\nJenis pesan yang bisa dikunci atau dibuka adalah: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`\n**Contoh:** `.plock msg` atau `.punlock msg`"
})
