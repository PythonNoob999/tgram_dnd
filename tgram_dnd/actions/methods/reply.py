from tgram_dnd.actions.action import Action
from tgram_dnd.enums.reply import REPLY_METHODS
from tgram_dnd.enums.reply_input import ReplyInput

from tgram.types import Message
from tgram import TgBot

from typing import Callable

class Reply(Action):
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