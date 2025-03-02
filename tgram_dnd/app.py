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
        self.config.load_strings()

    def add_flows(
        self,
        flows: Union[List[Union[MessageFlow, CallbackFlow]], Union[MessageFlow, CallbackFlow]]
    ):
        flows = [flows] if not isinstance(flows, list) else flows
        self.flows += flows

    def string(self, key: str, force_language: LANGUAGE_CODES = None) -> Callable:

        def deco(u: Update):
            if force_language:
                _ = self.config.strings[key].get(
                    force_language, self.config.strings[key][self.config.default_lang]
                )
            else:
                _ = self.config.strings[key].get(
                    u.from_user.language_code, self.config.strings[key][self.config.default_lang]
                )
            return _
        return deco
    
    def run(self) -> None:
        for flow in self.flows:
            flow.add_bot(self.bot)
            flow.load_plugin()

        self.bot.run()