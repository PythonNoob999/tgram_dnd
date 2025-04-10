from tgram_dnd.actions import Action
from tgram_dnd.errors import StopBlock
from tgram_dnd.utils import run_function
from tgram_dnd.conditions.base import BaseCondition
from tgram_dnd.errors import StopBlock

from tgram.types import Update
from typing import Union, Callable

class Condition(BaseCondition):
    '''a condition in its name, is a condition
    
    this is a basic condition just like if-else
    which takes `action` as the main condition
    and it executes the `success` function if `action` turned out to be True
    else it will execute the `fail` function
    
    Args:
        action (Union[:class:`tgram_dnd.actions.action.Action`, Callable]): the main condition
        success (Union[:class:`tgram_dnd.actions.action.Action`, Callable], *optional*): the function/action that will be executed in successful condition
        fail (Union[:class:`tgram_dnd.actions.action.Action`, Callable], *optional*): the function/action that will be executed in failing condition
        stop: (bool, *False*): wether to stop the current block execution or not, defaults to False'''
    def __init__(
        self,
        action: Union[Callable, Action],
        success: Union[Callable, Action] = None,
        fail: Union[Callable, Action] = None,
        stop: bool = False
    ):
        self.condition = action
        self.success = success
        self.fail = fail
        self.stop = stop
    
    async def __call__(self, u: Update):

        # inject app
        for obj in [
            self.condition,
            self.success,
            self.fail
        ]:
            if isinstance(obj, Action):
                obj.inject(self.app)

        # run conditions
        
        if await run_function(self.condition, u):
            if self.success:
                await run_function(self.success, u)
            return
        
        if self.fail:
            await run_function(self.fail, u)

        if self.stop:
            raise StopBlock