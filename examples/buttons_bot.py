from tgram_dnd import (
    App,
    BotConfig,
    MessageFlow,
    CallbackFlow,
    MessageBlock,
    CallbackBlock,
    Reply,
    Raw
)
from tgram import TgBot, filters

bot = TgBot("INSERT_BOT_TOKEN")
config = BotConfig(
    config_file="buttons.json"
)
app = App(
    bot=bot,
    config=config
)

# command flow
app.add_flows(
    MessageFlow(
        [
            MessageBlock(
                Reply(
                    "text",
                    {
                        "text": app.config.string("start"),
                        "reply_markup": app.config.keyboard("start")
                    }
                ),
                filter=filters.command("start")
            ),
            MessageBlock(
                Reply("text", {"text": app.config.string("communities")}),
                filter=filters.command("communities")
            ),
            MessageBlock(
                Reply("text", {"text": app.config.string("about")}),
                filter=filters.command("about")
            ),
            MessageBlock(
                Reply("text", {"text": app.config.string("rules")}),
                filter=filters.command("rules")
            )
        ],
        filter=(
            filters.private & filters.command(["start", "rules", "about", "communities"])
        )
    )
)

# callback flow
app.add_flows(
    CallbackFlow(
        [
            CallbackBlock(
                Raw(
                    "message.reply",
                    {
                        "text": app.config.string("about"),
                        "reply_markup": app.config.keyboard("close"),
                    },
                ),
                filter=(filters.regex("about"))
            ),
            CallbackBlock(
                Raw(
                    "message.reply",
                    {
                        "text": app.config.string("communities"),
                        "reply_markup": app.config.keyboard("close"),
                    },
                ),
                filter=(filters.regex("com"))
            ),
            CallbackBlock(
                Raw(
                    "message.reply",
                    {
                        "text": app.config.string("rules"),
                        "reply_markup": app.config.keyboard("close"),
                    },
                ),
                filter=(filters.regex("rules"))
            ),
            CallbackBlock(
                Raw(
                    "message.delete"
                ),
                filter=(filters.regex("close"))
            )
        ],
        filter=((filters.regex("about")) | (filters.regex("rules")) | (filters.regex("com")) | (filters.regex("close")))
))

app.run()