from __future__ import annotations

from tgram_dnd.actions.action import Action
from tgram_dnd.enums.reply_methods import REPLY_METHODS
from tgram_dnd.enums.reply_input import ReplyInput

from tgram.types import Message
from tgram import TgBot

from typing import Callable

class Reply(Action):
    '''an abstract method to Reply to update
    
    Args:
        func_name (:class:`tgram_dnd.enums.reply_methods.REPLY_METHODS`): The wanted function to reply with, example; "photo" will use reply_photo
        kwgs (:class:`tgram_dnd.enums.reply_input.ReplyInput`, *optional*): arguments for reply
        middleware (Callable, *optional*): middleware
        fill_vars (bool, *True*): Weither to automatically render vars in kwgs or not, defaults to *true*'''
    def __init__(
        self,
        func_name: REPLY_METHODS,
        kwgs: ReplyInput = {},
        middleware: Callable = None, 
        fill_vars: bool = True,
    ):
        super().__init__(None, kwgs, middleware, fill_vars=fill_vars)
        self.name = func_name

    async def __call__(self, m: Message):
        self.func = getattr(m, f"reply_{self.name}", None)

        return await super().__call__(m)