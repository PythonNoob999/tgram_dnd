from tgram_dnd.actions.action import Action
from tgram.types import Update

from tgram import TgBot
from typing import Callable

class RawCall(Action):
    '''Run a method from the TgBot instance
    
    .. code-block:: python
    
        action = RawCall(
            func_name='get_me',
        )
        res = await action(AnyUpdate)

        print(res)
        # <class 'tgram.types.User'>
        print("@" + res.username)
        # @MyAwesomeBot
    
    Args:
        func (Callable, *optional*): the function that will be executed
        kwgs (dict[str, Any], *optional*): additonal arguments for func
        middleware (Callabe, *optional*): a function to be executed before the main function run
        fill_vars (bool, *True*): Weither to automatically render vars in kwgs or not, defaults to *true*'''
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
        self.func = getattr(self.bot, self.name, None)
        return await super().__call__(u)