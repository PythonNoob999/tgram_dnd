from tgram_dnd.actions.action import Action
from tgram_dnd.utils import get_target_function

from tgram.types import Update
from typing import Callable

class Raw(Action):
    '''Run a method from the Update
    
    .. code-block:: python
    
        action = Raw(
            func_name='reply_text',
            kwgs={"text": "Wassup"},
        )
        await action(Message)
        # Called Message.reply_text(text="Wassup")
         
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
        # getting to wanted function
        self.func = get_target_function(
            u, self.name
        )
        return await super().__call__(u)