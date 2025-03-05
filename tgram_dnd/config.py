from tgram_dnd.enums.language_codes import LANGUAGE_CODES
from tgram_dnd.enums.bot_command_input import BotCommandInput
from tgram_dnd.errors import InvalidStrings

from tgram.types import (
    InlineKeyboardMarkup,
    BotCommand,
    Update
)
from tgram import TgBot
from typing import Dict, List, Union, Callable

import os
import json

class BotConfig:
    def __init__(
        self,
        strings: Dict[str, Dict[LANGUAGE_CODES, str]],
        keyboards: Dict[str, Dict[LANGUAGE_CODES, InlineKeyboardMarkup]] = None,
        default_lang: LANGUAGE_CODES = "en",
        bot_commands: List[BotCommandInput] = None
    ):
        self.strings = strings
        self.keyboards = keyboards or {}
        self.default_lang = default_lang
        self.commands = bot_commands or []

    def load_strings(self) -> None:
        if isinstance(self.strings, str):

            if os.path.isfile(self.strings):
                self.strings = json.load(
                    open(
                        self.strings,
                        mode="r+"
                    )
                )
                return

            raise InvalidStrings(type(self.strings))
        
    def string(self, key: str, force_language: LANGUAGE_CODES = None) -> Callable:

        def deco(u: Update):
            if force_language:
                _ = self.strings[key].get(
                    force_language, self.strings[key][self.default_lang]
                )
            else:
                _ = self.strings[key].get(
                    u.from_user.language_code, self.strings[key][self.default_lang]
                )
            return _

        return deco
    
    def keyboard(self, key: str, force_language: LANGUAGE_CODES = None) -> Callable:

        def deco(u: Update):
            if force_language:
                _ = self.keyboards[key].get(
                    force_language, self.keyboards[key][self.default_lang]
                )
            else:
                _ = self.keyboards[key].get(
                    u.from_user.language_code, self.keyboards[key][self.default_lang]
                )
            return _

        return deco
        
    def configure(
        self,
        bot: TgBot
    ) -> None:
        # setting bot commands
        commands = {}
        for command in self.commands:
            command.setdefault("language_code", "en")
            if command.get("language_code", "en") not in commands:
                commands[command.get("language_code", "en")] = []

            commands[command["language_code"]].append(
                BotCommand(
                    command=command["command"],
                    description=command["description"]
                )
            )

        for lang_code in commands:
            bot.set_my_commands(
                commands=commands[lang_code],
                language_code=lang_code
            )

        # loading strings
        self.load_strings()