from tgram_dnd.blocks.message_block import MessageBlock

from tgram import TgBot, filters
from tgram.types import Message

from typing import List, Optional, Union

import tgram_dnd

class MessageFlow:
    '''a flow used to track Messages
    
    Args:
        blocks (Union[List[:class:`tgram_dnd.flows.MessageBlock`]], :class:`tgram_dnd.flows.MessageBlock`): The proccesing blocks
        filter (`tgram.filters.Filter <https://z44d.github.io/tgram/tgram.html#tgram.filters.Filter>`_, *optional*): filter incoming messages, pass Nothing to trigger all updates
    
    Returns:
        None'''
    def __init__(
        self,
        blocks: Union[List[MessageBlock], MessageBlock],
        filter: Optional[filters.Filter] = None,
    ):
        self.blocks = [blocks] if not isinstance(blocks, list) else blocks
        self.filter = filter or filters.all

    def inject(
        self,
        app: "tgram_dnd.app.App"
    ):
        self.bot = app.bot
        self.app = app

    def load_plugin(self) -> None:
        '''loads plugin into the bot'''
        @self.bot.on_message(self.filter)
        async def handle(
            bot: TgBot,
            m: Message
        ):
            for block in self.blocks:
                block.inject(self.app)
                await block.exec(bot, m)