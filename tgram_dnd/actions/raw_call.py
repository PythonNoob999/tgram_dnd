from tgram_dnd.actions.action import Action
from tgram.types import Update

from tgram import TgBot
from jinja2 import Template
from typing import Callable

import asyncio

class RawCall(Action):
    def __init__(
        self,
        func_name: str,
        kwgs: dict = {},
        middleware: Callable = None,
        bot: TgBot = None,
        fill_vars: bool = True,
    ):
        super().__init__(None, kwgs, bot, middleware, fill_vars=fill_vars)
        self.middleware = middleware
        self.name = func_name

    def render_vars(self, string: str, u: Update) -> str:
        return Template(string).render(u.json)

    async def __call__(self, u: Update):
        self.func = getattr(self.bot, self.name, None)
        return await super().__call__(u)