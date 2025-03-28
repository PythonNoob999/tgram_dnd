from tgram_dnd import (
    App,
    MessageFlow,
    MessageBlock,
    Reply
)
from tgram_dnd.utils import run_function

from tgram import TgBot, filters
from tgram.types import Message

import requests as r

# setting api vars
URL = "https://api.coingecko.com/api/v3/coins/bitcoin"
API_KEY = "INSERT-COINGECKO-TOKEN"

async def update_price(
    action: Reply,
    update: Message,
    vars: dict
) -> None:
    # first we will get the cached price
    price = action.app.cache.get("btc_price")

    if price:
        # price exists and didn't expire
        return
    
    # price expired/does not exist, now we will update it

    # get new price
    data = (await run_function(
        r.get,
        URL,
        headers={
            "accept": "application/json",
            "x-cg-demo-api-key": API_KEY
        }
    )).json()

    price = data["market_data"]["current_price"]["usd"]

    # store it in the cache
    res = action.app.cache.set(
        "btc_price",
        value=str(price),
        ttl=5
    )

bot = TgBot("INSERT_BOT_TOKEN")
app = App(
    bot=bot,
)

app.add_flows(
    MessageFlow(
        MessageBlock(
            [
                Reply(
                    "text",
                    {
                        "text": "Current BTC Price is {{cache.get('btc_price')}}$"
                    },
                    middleware=update_price
                )
            ],
            filter=(filters.command("price", prefixes=[".", "/", "!"]))
        ),
        filter=(filters.command("price", prefixes=[".", "/", "!"]))
    )
)

app.run()