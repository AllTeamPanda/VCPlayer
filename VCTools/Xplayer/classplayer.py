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

async def is_url_ok(url: str):
    try:
        return await async_searcher(url, real=True)
    except BaseException as er:
        LOGS.debug(er)
        return False




