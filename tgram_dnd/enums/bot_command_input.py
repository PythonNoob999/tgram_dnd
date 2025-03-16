from typing import TypedDict

class BotCommandInput(TypedDict):
    '''translated to `tgram.types.BotCommand <https://z44d.github.io/tgram/tgram.types.html#tgram.types.BotCommand>`_'''
    command: str
    description: str
    language_code: str