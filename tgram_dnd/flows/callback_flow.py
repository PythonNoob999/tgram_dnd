from tgram_dnd.blocks import CallbackBlock

from tgram import TgBot, filters
from tgram.types import CallbackQuery

from typing import List, Optional, Union

class CallbackFlow:
    def __init__(
        self,
        blocks: Union[List[CallbackBlock], CallbackBlock],
        filter: Optional[filters.Filter] = None,
    ):
        self.blocks = [blocks] if not isinstance(blocks, list) else blocks
        self.filter = filter or filters.all

    def add_bot(self, bot: TgBot):
        self.bot = bot

    def load_plugin(self) -> None:
        '''loads plugin into the bot'''
        @self.bot.on_callback_query(self.filter)
        async def handle(
            bot: TgBot,
            cb: CallbackQuery
        ):
            for block in self.blocks:

                for action in block.actions:
                    action.add_bot(self.bot)

                await block.exec(bot, cb)