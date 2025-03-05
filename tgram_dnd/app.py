from tgram_dnd.flows import MessageFlow, CallbackFlow
from tgram_dnd.config import BotConfig
from tgram_dnd.enums.language_codes import LANGUAGE_CODES

from tgram import TgBot
from tgram.types import Update

from typing import List, Union, Callable

class App:
    def __init__(
        self,
        bot: TgBot,
        flows: List[Union[MessageFlow, CallbackFlow]] = [],
        config: BotConfig = None
    ):
        self.bot = bot
        self.flows = flows
        self.config = config

    def add_flows(
        self,
        flows: Union[List[Union[MessageFlow, CallbackFlow]], Union[MessageFlow, CallbackFlow]]
    ):
        flows = [flows] if not isinstance(flows, list) else flows
        self.flows += flows
    
    def run(self) -> None:
        for flow in self.flows:
            flow.add_bot(self.bot)
            flow.load_plugin()
        
        # setting up config
        if self.config:
            self.config.configure(bot=self.bot)

        self.bot.run()