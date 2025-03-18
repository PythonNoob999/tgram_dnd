from tgram_dnd import (
    App,
    MessageFlow,
    MessageBlock,
    Reply # abstract Action
)
from tgram import TgBot, filters

bot = TgBot("INSERT_BOT_TOKEN")
app = App(bot=bot)

hello = MessageBlock(
    # this block will reply with "hi!" when getting a message with the text "!hello"
    Reply(
        # reply_method
        "text",
        kwgs={"text": "hi!"}
    ),
    filter=(filters.command("hello", prefixes="!"))
)
hi = MessageBlock(
    # this block will reply with "hello!" when getting a message with the text "!hi"
    Reply(
        "text",
        kwgs={"text": "hello!"}
    ),
    filter=(filters.command("hi", prefixes="!"))
)

flow = MessageFlow(
    blocks=[hi, hello],
    filter=(
        filters.command(["hi", "hello"], prefixes="!")
    )
)

app.add_flows(flow)
app.run()