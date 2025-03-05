from typing import TypedDict

class BotCommandInput(TypedDict):
    command: str
    description: str
    language_code: str