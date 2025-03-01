from tgram_dnd.actions.action import Action
from tgram_dnd.enums.reply import REPLY_METHODS
from tgram_dnd.enums.reply_input import ReplyInput

from tgram.types import Message
from tgram import TgBot

from typing import Callable
from jinja2 import Template

class Reply(Action):
    def __init__(
        self,
        func_name: REPLY_METHODS,
        kwgs: ReplyInput = {},
        bot: TgBot = None,
        middleware: Callable = None,
        fill_vars: bool = True,
    ):
        super().__init__(None, kwgs, bot, middleware, fill_vars=fill_vars)
        self.kwgs = kwgs
        self.name = func_name

    def render_vars(self, string: str, m: Message) -> str:
        return Template(string).render(m.json)

    async def __call__(self, m: Message):
        self.func = getattr(m, f"reply_{self.name}", None)
        
        if self.kwgs.get('text', None):
            self.kwgs['text'] = self.render_vars(self.kwgs['text'], m)

        if self.kwgs.get('caption', None):
            self.kwgs['caption'] = self.render_vars(self.kwgs['caption'], m)

        return await super().__call__(m)