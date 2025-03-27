from tgram_dnd.errors import StopExecution
from tgram_dnd.utils import render_vars, run_function

from tgram import TgBot
from tgram.types import Update
from typing import Callable, Union

import asyncio

class Action:
    '''The base class for all Actions
    
    Args:
        func (Callable, *optional*): the function that will be executed
        kwgs (dict[str, Any], *optional*): additonal arguments for func
        middleware (Callabe, *optional*): a function to be executed before the main function run
        fill_vars (bool, *True*): Weither to automatically render vars in kwgs or not, defaults to *true*'''
    def __init__(
        self,
        func: Callable = None,
        kwgs: dict = None,
        middleware: Callable = None,
        fill_vars: bool = True
    ):
        self.func = func
        self.kwgs = kwgs or {}
        self.middleware = middleware
        self.fill_vars = fill_vars

    def add_bot(self, bot: TgBot) -> None:
        self.bot = bot

    async def __call__(self, u: Update):
        '''the entry-point to the action
        here we
        render vars, run middlewares, and finally executing main funciton'''
        _vars = self.kwgs.copy()

        if self.fill_vars:
            for var in _vars:

                if isinstance(_vars[var], Callable):
                    _vars[var] = _vars[var](u)

                if isinstance(_vars[var], str):
                    _vars[var] = render_vars(_vars[var], u.json)

        if not isinstance(self.func, Callable):
            raise ValueError(f"{self.__class__.__name__}.func should be callable, not {type(self.func)}")
        
        if self.middleware:
            try:
                await run_function(
                    self.middleware, self.func, u, _vars
                )
            except StopExecution:
                return

        return await run_function(self.func, **_vars)