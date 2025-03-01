from tgram_dnd.blocks import MessageBlock
from tgram import TgBot
from tgram.types import Message
from typing import List

class MessageFlow:
    def __init__(
        self,
        bot: TgBot,
        blocks: List[MessageBlock],
    ):
        self.bot = bot
        self.blocks = blocks

    def load_plugin(self) -> None:
        '''loads plugin into the bot'''
        @self.bot.on_message()
        async def handle(
            bot: TgBot,
            m: Message
        ):
            for block in self.blocks:
                await block.exec(bot, m)