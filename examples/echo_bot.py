from tgram_dnd import (
    MessageBlock,
    MessageFlow,
    Reply,
    App, BotConfig
)
from tgram import TgBot, filters

bot = TgBot("INSERT_BOT_TOKEN")
strings = BotConfig(
    strings={
        "echo": {
            # {{var_name}} see vars templating for more info in the docs
            "ar": "{{from.first_name}} لقد قال: {{text}}",
            "en": "{{from.first_name}} Said: {{text}}"
        }
    },
    default_lang="ar"
)
app = App(
    bot,
    config=strings
)

# creating basic echo not
app.add_flows(
    MessageFlow(
        MessageBlock(
            actions=[
                Reply(
                    func_name="text",
                    # here are the arguments
                    kwgs={
                        "text": app.string("echo")
                    },
                )
            ],
            filter=(
                filters.private & filters.text
            )
        ),
    )
)


# running bot
app.run()