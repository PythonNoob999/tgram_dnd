from tgram_dnd.errors import StopExecution
from tgram import TgBot

from typing import Callable
from jinja2 import Template
from tgram.types import Update
import asyncio

class Action:
    def __init__(
        self,
        func: Callable = None,
        kwgs: dict = {},
        bot: TgBot = None,
        middleware: Callable = None,
        fill_vars: bool = True
    ):
        self.bot = bot
        self.func = func
        self.kwgs = kwgs
        self.middleware = middleware
        self.fill_vars = fill_vars

    def render_vars(self, string: str, u: Update) -> str:
        return Template(string).render(**u.json)

    async def __call__(self, u: Update):
        _vars = self.kwgs.copy()
        if self.fill_vars:
            for var in _vars:
                if isinstance(_vars[var], str):
                    _vars[var] = self.render_vars(_vars[var], u)

        if not isinstance(self.func, Callable):
            raise ValueError(f"{self.__class__.__name__}.func should be callable, not {type(self.func)}")
        
        if self.middleware:
            try:
                if asyncio.iscoroutinefunction(self.middleware):
                    await self.middleware(self.func, u, _vars)
                else:
                    await asyncio.to_thread(self.middleware, self.func, u, _vars)
            except StopExecution:
                return

        if asyncio.iscoroutinefunction(self.func):
            await self.func(**_vars)
        else:
            await asyncio.to_thread(self.func, **_vars)