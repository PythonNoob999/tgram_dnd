from tgram import TgBot, filters
from tgram.types import (
    Message
)
from tgram_dnd.actions.action import Action
from typing import Optional, Union, List

class MessageBlock:
    def __init__(
        self,
        actions: Union[List[Action], Optional[Action]],
        filter: Optional[filters.Filter] = None,
    ):
        '''this defines a MessageBlock'''
        self.actions = actions if isinstance(actions, list) else [actions]
        self.filter = filter or filters.all

    async def exec(
        self,
        bot: TgBot,
        m: Message
    ):
        '''this is where the block logic run'''
        if await self.filter(bot, m):
            for action in self.actions:
                await action(m)