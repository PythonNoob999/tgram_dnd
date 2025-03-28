from tgram_dnd.blocks.callback_block import CallbackBlock

from tgram import TgBot, filters
from tgram.types import CallbackQuery

from typing import List, Optional, Union

import tgram_dnd

class CallbackFlow:
    '''a flow used to track CallBacks
    
    Args:
        blocks (Union[List[:class:`tgram_dnd.flows.CallbackBlock`]], :class:`tgram_dnd.flows.CallbackBlock`): The proccesing blocks
        filter (`tgram.filters.Filter <https://z44d.github.io/tgram/tgram.html#tgram.filters.Filter>`_, *optional*): filter incoming callbacks, pass Nothing to trigger all updates
    
    Returns:
        None'''
    def __init__(
        self,
        blocks: Union[List[CallbackBlock], CallbackBlock],
        filter: Optional[filters.Filter] = None,
    ) -> None:
        self.blocks = [blocks] if not isinstance(blocks, list) else blocks
        self.filter = filter or filters.all
        self.bot: TgBot = None

    def inject(
        self,
        app: "tgram_dnd.app.App"
    ):
        self.bot = app.bot
        self.app = app

    def load_plugin(self) -> None:
        '''loads plugin into the bot'''
        @self.bot.on_callback_query(self.filter)
        async def handle(
            bot: TgBot,
            cb: CallbackQuery
        ):
            for block in self.blocks:
                block.inject(self.app)
                await block.exec(bot, cb)