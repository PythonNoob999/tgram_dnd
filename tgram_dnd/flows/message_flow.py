from tgram_dnd.blocks import MessageBlock

from tgram import TgBot, filters
from tgram.types import Message

from typing import List, Optional, Union

class MessageFlow:
    '''a flow used to track Messages
    
    Args:
        blocks (Union[List[:class:`tgram_dnd.flows.MessageBlock`]], :class:`tgram_dnd.flows.MessageBlock`): The proccesing blocks
        filter (`tgram.filters.Filter <https://z44d.github.io/tgram/tgram.html#tgram.filters.Filter>`_, *optional*): filter incoming callbacks, pass Nothing to trigger all updates
    
    Returns:
        None'''
    def __init__(
        self,
        blocks: Union[List[MessageBlock], MessageBlock],
        filter: Optional[filters.Filter] = None,
    ):
        self.blocks = [blocks] if not isinstance(blocks, list) else blocks
        self.filter = filter or filters.all

    def add_bot(self, bot: TgBot):
        '''adds a TgBot instance to pass it to Blocks
        
        Args:
            bot (`tgram.client.TgBot <https://z44d.github.io/tgram/tgram.html#tgram.TgBot>`_)
        
        Returns:
            None'''
        self.bot = bot

    def load_plugin(self) -> None:
        '''loads plugin into the bot'''
        @self.bot.on_message(self.filter)
        async def handle(
            bot: TgBot,
            m: Message
        ):
            for block in self.blocks:

                for action in block.actions:
                    action.add_bot(self.bot)

                await block.exec(bot, m)