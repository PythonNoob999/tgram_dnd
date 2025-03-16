from typing import Literal

REPLY_METHODS = Literal[
    "text",
    "photo",
    "audio",
    "document",
    "video",
    "dice",
    "sticker"
]
''':class:`tgram_dnd.actions.methods.reply.Reply` Methods'''