#Panda Userbot

import asyncio
import os
import re
import traceback
from time import time
from traceback import format_exc

from telethon import events
from telethon.tl import functions, types
from telethon.utils import get_display_name
from userbot.versions import __version__ as PandaVersion

def compile_pattern(data, hndlr):
    if data.startswith("^"):
        data = data[1:]
    if data.startswith("."):
        data = data[1:]
    if hndlr in [" ", "NO_HNDLR"]:
        # No Hndlr Feature
        return re.compile("^" + data)
    return re.compile("\\" + hndlr + data)


try:
    from yt_dlp import YoutubeDL
except ImportError:
    YoutubeDL = None
    LOGS.error("'yt-dlp' not found!")

try:
   from youtubesearchpython import VideosSearch
except ImportError:
    VideosSearch = None
    
from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError
from telethon.errors.rpcerrorlist import (
    ParticipantJoinMissingError,
    ChatSendMediaForbiddenError,
)

from userbot._misc.data import _sudousers_list
from userbot import *
from userbot.resources import (
    bash,
    downloader,
    inline_mention,
    mediainfo,
    time_formatter,
    admin_check, 
    in_pattern,
    get_videos_link,
    eod,
    eor,
)
from userbot.helpers.utils.misc import async_searcher
from userbot.config import Config

async def is_url_ok(url: str):
    try:
        return await async_searcher(url, real=True)
    except BaseException as er:
        LOGS.debug(er)
        return False
    
vcClient = PandaBot
HNDLR = Config.COMMAND_HAND_LER  
def sudoers():
    return _sudousers_list() 

from userbot.resources.en import *
def owner_and_sudos():
    return [udB.get_key("OWNER_ID") or Config.OWNER_ID, *sudoers()]

def VC_AUTHS():
    _vcsudos = udB.get_key("VC_SUDOS") or []
    return [int(a) for a in [*owner_and_sudos(), *_vcsudos]]

asstUserName = Config.TG_BOT_USERNAME
LOG_CHANNEL = udB.get_key("PRIVATE_GROUP_BOT_API_ID") or int(Config.PRIVATE_GROUP_BOT_API_ID)
ACTIVE_CALLS, VC_QUEUE = [], {}
MSGID_CACHE, VIDEO_ON = {}, {}
CLIENTS = {}


if udB.get_key("VCMODE"):
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot2:
        _client2 = GroupCallFactory(
                        PandaBot2, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot3:
        _client3 = GroupCallFactory(
                        PandaBot3, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot4:
        _client4 = GroupCallFactory(
                        PandaBot4, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot5:
        _client5 = GroupCallFactory(
                        PandaBot5, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot6:
        _client6 = GroupCallFactory(
                        PandaBot6, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot7:
        _client7 = GroupCallFactory(
                        PandaBot7, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot8:
        _client8 = GroupCallFactory(
                        PandaBot8, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot9:
        _client9 = GroupCallFactory(
                        PandaBot9, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot10:
        _client10 = GroupCallFactory(
                        PandaBot10, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot11:
        _client11 = GroupCallFactory(
                        PandaBot11, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot12:
        _client12 = GroupCallFactory(
                        PandaBot12, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot13:
        _client13 = GroupCallFactory(
                        PandaBot13, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot14:
        _client14 = GroupCallFactory(
                        PandaBot14, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot15:
        _client15 = GroupCallFactory(
                        PandaBot15, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot16:
        _client16 = GroupCallFactory(
                        PandaBot16, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot17:
        _client17 = GroupCallFactory(
                        PandaBot17, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot18:
        _client18 = GroupCallFactory(
                        PandaBot18, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot19:
        _client19 = GroupCallFactory(
                        PandaBot19, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot20:
        _client20 = GroupCallFactory(
                        PandaBot20, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot21:
        _client21 = GroupCallFactory(
                        PandaBot21, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot22:
        _client22 = GroupCallFactory(
                        PandaBot22, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot23:
        _client23 = GroupCallFactory(
                        PandaBot23, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot24:
        _client24 = GroupCallFactory(
                        PandaBot24, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot25:
        _client25 = GroupCallFactory(
                        PandaBot25, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot26:
        _client26 = GroupCallFactory(
                        PandaBot26, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot27:
        _client27 = GroupCallFactory(
                        PandaBot27, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot28:
        _client28 = GroupCallFactory(
                        PandaBot28, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot29:
        _client29 = GroupCallFactory(
                        PandaBot29, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot30:
        _client30 = GroupCallFactory(
                        PandaBot30, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot31:
        _client31 = GroupCallFactory(
                        PandaBot31, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot32:
        _client32 = GroupCallFactory(
                        PandaBot32, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot33:
        _client33 = GroupCallFactory(
                        PandaBot33, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot34:
        _client34 = GroupCallFactory(
                        PandaBot34, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot35:
        _client35 = GroupCallFactory(
                        PandaBot35, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot36:
        _client36 = GroupCallFactory(
                        PandaBot36, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot37:
        _client37 = GroupCallFactory(
                        PandaBot37, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot38:
        _client38 = GroupCallFactory(
                        PandaBot38, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot39:
        _client39 = GroupCallFactory(
                        PandaBot39, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot40:
        _client40 = GroupCallFactory(
                        PandaBot40, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot41:
        _client41 = GroupCallFactory(
                        PandaBot41, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot42:
        _client42 = GroupCallFactory(
                        PandaBot42, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot43:
        _client43 = GroupCallFactory(
                        PandaBot43, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot44:
        _client44 = GroupCallFactory(
                        PandaBot44, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot45:
        _client45 = GroupCallFactory(
                        PandaBot45, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot46:
        _client46 = GroupCallFactory(
                        PandaBot46, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot47:
        _client47 = GroupCallFactory(
                        PandaBot47, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot48:
        _client48 = GroupCallFactory(
                        PandaBot48, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot49:
        _client49 = GroupCallFactory(
                        PandaBot49, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot50:
        _client50 = GroupCallFactory(
                        PandaBot50, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



