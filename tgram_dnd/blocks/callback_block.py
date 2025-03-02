from tgram import TgBot, filters
from tgram.types import (
    CallbackQuery
)
from tgram_dnd.actions.action import Action
from typing import Optional, Union, List

class CallbackBlock:
    def __init__(
        self,
        actions: Union[List[Action], Optional[Action]],
        filter: Optional[filters.Filter] = None,
    ):
        '''this defines a MessageBlock'''
        self.actions = [actions] if not isinstance(actions, list) else actions
        self.filter = filter or filters.all

    async def exec(
        self,
        bot: TgBot,
        cb: CallbackQuery
    ):
        '''this is where the block logic run'''
        if await self.filter(bot, cb):
            for action in self.actions:
                await action(cb)