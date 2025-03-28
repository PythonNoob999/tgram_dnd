from tgram import TgBot, filters
from tgram.types import (
    CallbackQuery
)

from tgram_dnd.actions.action import Action

from typing import Optional, Union, List

import tgram_dnd

class CallbackBlock:
    '''the block that process Callbacks and runs a series of Actions (:ref:`what-is-an-action?`)
    
    Args:
        actions (Union[List[:class:`tgram_dnd.actions.Action`], :class:`tgram_dnd.actions.Action`]): the actions that will be executed
        filter (`tgram.filters.Filter <https://z44d.github.io/tgram/tgram.html#tgram.filters.Filter>`_, *optional*): filter incoming callbacks, pass Nothing to trigger all updates
    
    Returns:
        None'''
    def __init__(
        self,
        actions: Union[List[Action], Optional[Action]],
        filter: Optional[filters.Filter] = None,
    ):
        '''this defines a MessageBlock'''
        self.actions = [actions] if not isinstance(actions, list) else actions
        self.filter = filter or filters.all

    def inject(
        self,
        app: "tgram_dnd.app.App"
    ):
        self.bot = app.bot
        self.app = app

    async def exec(
        self,
        bot: TgBot,
        cb: CallbackQuery
    ):
        '''this is where the block actions run'''
        if await self.filter(bot, cb):
            for action in self.actions:
                action.inject(self.app)
                await action(cb)