from __future__ import annotations

from tgram_dnd.enums.language_codes import LANGUAGE_CODES
from tgram_dnd.enums.bot_command_input import BotCommandInput
from tgram_dnd.errors import InvalidStrings

from tgram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    BotCommand,
    Update
)
from tgram import TgBot
from typing import Dict, List, Callable

import os
import json

class BotConfig:
    '''Init BotConfig

    .. code-block:: python

        # Importing data manually
        config = BotConfig(
            strings={
                "start": ...
            },
            keyboards=...,
            commands=...
        )

        # importing from a file
        config = BotConfig(config_file="data.json")

    Args:
        strings (dict[str, dict[:class:`tgram_dnd.enums.language_codes.LANGUAGE_CODES`, str]], *optinal*): the pre-made text
        keyboards (dict[str, dict[:class:`tgram_dnd.enums.language_codes.LANGUAGE_CODES`, :class:`tgram.types.InlineKeyboardMarkup`]], *optinal*): the pre-made keyboards
        default_lang (:class:`tgram_dnd.enums.language_codes.LANGUAGE_CODES`, *optinal*): the default language to fetch if the user language is not supported
        bot_commands (list[:class:`tgram_dnd.enums.bot_command_input.BotCommandInput`], *optinal*): pre-made bot menu buttons/commands
        config_file (str, *optinal*): The path to the configuration file which contains all the strings,keyboards,bot_commands etc
    Returns:
        None'''

    def __init__(
        self,
        strings: Dict[str, Dict[LANGUAGE_CODES, str]] = None,
        keyboards: Dict[str, Dict[LANGUAGE_CODES, InlineKeyboardMarkup]] = None,
        default_lang: LANGUAGE_CODES = "en",
        bot_commands: List[BotCommandInput] = None,
        config_file: str = None
    ):

        self.strings = strings or {}
        self.keyboards = keyboards or {}
        self.default_lang = default_lang
        self.commands = bot_commands or []
        if config_file and os.path.isfile(config_file):
            self.load_file_data(config_file)
    
    def load_file_data(
        self,
        file: str
    ) -> None:
        '''Loads data from ConfigFile
        
        Args:
            file (string) : file path
        
        Returns:
            None'''
        data = json.load(open(file, "r+", encoding="utf-8"))
        self.strings = data.get("strings", {})
        self.commands = data.get("commands", [])
        self.default_lang = data.get("default_language", "en")

        # loading keyboards
        kbs = data.get("keyboards", {})
        result: Dict[str, Dict[LANGUAGE_CODES, InlineKeyboardMarkup]] = {}
        for kb in kbs:
            result[kb] = {}
            for klang in kbs[kb]:
                result[kb][klang] = []
                keyboard = kbs[kb][klang]
                for rows in keyboard:
                    result[kb][klang].append(
                        [InlineKeyboardButton(
                            **button
                        ) for button in rows]
                    )
                result[kb][klang] = InlineKeyboardMarkup(result[kb][klang])
        self.keyboards = result

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
        '''used to return a string based on the user language
        
        Args:
            key (string): the string key
            force_language (:class:`tgram_dnd.enums.language_codes.LANGUAGE_CODES`): a specfic language to force it on the string (despite user language)
        
        Returns:
            Decorator: a decorator to get the string based on user language'''

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
        '''used to return a keyboard based on the user language
        
        Args:
            key (string): the keyboard key
            force_language (:class:`tgram_dnd.enums.language_codes.LANGUAGE_CODES`): a specfic language to force it on the keyboard (despite user language)
        
        Returns:
            Decorator: a decorator to get the keyboard based on user language'''

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
        '''used to apply the configurations
       
        Args:
            bot (:class:`tgram.client.TgBot`)
        Returns:
            None'''
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