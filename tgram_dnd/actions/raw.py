from tgram_dnd.actions.action import Action
from tgram.types import Update

from tgram import TgBot
from typing import Callable

class Raw(Action):
    def __init__(
        self,
        func_name: str,
        kwgs: dict = {},
        middleware: Callable = None,
        fill_vars: bool = True,
    ):
        super().__init__(None, kwgs, middleware, fill_vars=fill_vars)
        self.name = func_name

    async def __call__(self, u: Update):
        # getting to wanted function
        func = getattr(u, self.name.split(".")[0])
        for attr in self.name.split(".")[1:]:
            func = getattr(func, attr, None)
        self.func = func
        return await super().__call__(u)