from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights

from asyncio import sleep
from userbot import CMD_HELP
from userbot.events import register, errors_handler


@register(outgoing=True, pattern=r"^.lock ?(.*)")
@errors_handler
async def locks(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        input_str = event.pattern_match.group(1)
        peer_id = event.chat_id
        msg = None
        media = None
        sticker = None
        gif = None
        gamee = None
        ainline = None
        gpoll = None
        adduser = None
        cpin = None
        changeinfo = None
        if "msg" in input_str:
            msg = True
        if "media" in input_str:
            media = True
        if "sticker" in input_str:
            sticker = True
        if "gif" in input_str:
            gif = True
        if "game" in input_str:
            gamee = True
        if "inline" in input_str:
            ainline = True
        if "poll" in input_str:
            gpoll = True
        if "invite" in input_str:
            adduser = True
        if "pin" in input_str:
            cpin = True
        if "info" in input_str:
            changeinfo = True
        banned_rights=ChatBannedRights(
            until_date=None,
            send_messages=msg,
            send_media=media,
            send_stickers=sticker,
            send_gifs=gif,
            send_games=gamee,
            send_inline=ainline,
            send_polls=gpoll,
            invite_users=adduser,
            pin_messages=cpin,
            change_info=changeinfo,
        )
        try:
            result = await event.client(EditChatDefaultBannedRightsRequest(
                peer=peer_id,
                banned_rights=banned_rights
            ))
        except Exception as e:
            await event.edit(str(e))
        else:
            await sleep(5)
            await event.delete()

CMD_HELP.update({
    "locks": ".lock <type(s)>\
\nUsage: Allows you to lock away some common message types in the chat.\
\nNOTE: Requires admin rights in the chat !!\
\n\nAvailable message types to lock are: \
\n`msg, media, sticker, gif, game, inline, poll, invite, pin, info`\
"})
