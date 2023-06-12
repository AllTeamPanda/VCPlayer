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
from userbot.helper.utils.misc import async_searcher
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
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )
    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )

    if PandaBot:
        _client = GroupCallFactory(
                        PandaBot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
                    )



