from tgram_dnd import (
    App,
    MessageFlow,
    MessageBlock,
    Reply
)
from tgram import TgBot, filters
from tgram.types import Update

def vip_only(vip_users_list: list[str]):
    
    def inner_filter(
        bot: TgBot,
        update: Update
    ) -> bool:
        # here is our actual filter, a filter takes in
        # bot: your bot instance
        # update: the incoming update, it can be one of Message, CallbackQuery, etc...
        # and returns a boolean, true if this update is allowes, False if not

        # get username from the update
        username = "@" + update.from_user.username

        # check if the user is VIP or not
        if username in vip_users_list:
            return True
        else:
            return False

    # now after making out filter above, lets return it as a Filter type
    return filters.Filter(inner_filter)

bot = TgBot("INSERT_BOT_TOKEN")
app = App(bot=bot)

# its my tg usernamn ;) you can edit it
vip_users = ["@kerolis55463"]

# make a Quick flow and add it in 1 call
app.add_flows(
    MessageFlow(
        MessageBlock(
            Reply(
                "text",
                kwgs={"text": "Hi VIP ⭐"}
            )
        ),
        filter=(vip_only(vip_users))
    )
)
app.run()