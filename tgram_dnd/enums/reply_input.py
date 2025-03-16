from typing import TypedDict, Optional
from tgram.types import (
    InlineKeyboardMarkup
)

class ReplyInput(TypedDict):
    text: Optional[str]
    caption: Optional[str]
    document: Optional[str]
    video: Optional[str]
    photo: Optional[str]
    sticker: Optional[str]
    audio: Optional[str]
    emoji: Optional[str]
    reply_markup: Optional[InlineKeyboardMarkup]

'''a set of arguments for :class:`tgram_dnd.actions.methods.Reply`'''