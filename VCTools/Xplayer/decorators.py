from .events import *


def vc_asst(dec, **kwargs):
    def ult(func):
        kwargs["func"] = (
            lambda e: not e.is_private and not e.via_bot_id and not e.fwd_from
        )
        handler = udB.get_key("VC_HNDLR") or HNDLR
        kwargs["pattern"] = compile_pattern(dec, handler)
        vc_auth = kwargs.get("vc_auth", True)
        key = udB.get_key("VC_AUTH_GROUPS") or {}
        if "vc_auth" in kwargs:
            del kwargs["vc_auth"]

        async def vc_handler(e):
            VCAUTH = list(key.keys())
            if not (
                (e.out)
                or (e.sender_id in VC_AUTHS())
                or (vc_auth and e.chat_id in VCAUTH)
            ):
                return
            elif vc_auth and key.get(e.chat_id):
                cha, adm = key.get(e.chat_id), key[e.chat_id]["admins"]
                if adm and not (await admin_check(e)):
                    return
            try:
                await func(e)
            except Exception:
                LOGS.exception(Exception)
                await tgbot.send_message(
                    LOG_CHANNEL,
                    f"VC Error - <code>{PandaVersion}</code>\n\n<code>{e.text}</code>\n\n<code>{format_exc()}</code>",
                    parse_mode="html",
                )

        vclient.add_event_handler(
            vc_handler,
            events.NewMessage(**kwargs),
        )

    return ult
