from typing import TypedDict, Optional
from tgram.types import (
    InlineKeyboardMarkup as IKM,
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
    reply_markup: Optional[IKM]