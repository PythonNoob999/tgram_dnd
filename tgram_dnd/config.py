from tgram_dnd.enums.language_codes import LANGUAGE_CODES
from tgram_dnd.errors import InvalidStrings

from typing import Dict

import os
import json

class BotConfig:
    def __init__(
        self,
        strings: Dict[str, Dict[LANGUAGE_CODES, str]],
        default_lang: LANGUAGE_CODES = "en"
    ):
        self.strings = strings
        self.default_lang = default_lang

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