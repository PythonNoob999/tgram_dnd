############
Caching
############

What is Caching ⁉️
-------------------
caching is the process of storing some items
temporarily in memory

caching can be used in multiple scenario's

1. Database Caching
    caching is useful for storing a database field
    for example we can cache a user Posts in the caching system instead
    of querying the database every time for it. thus database efficiency increases

2. API Calls limiting
    caching can be also used in decreasing the calls to your API

    for example (in IMDB API) we can cache the gross revenue of a certain movie
    with a ttl (time to live) of 5 seconds
    
    thus instead of calling the API every time our users query's this data
    we will only launch 1 get request every 5 seconds instead of recalling the API every time any user query the data

.. raw:: html

    <br>

How Caching Works in TgramDND ⁉️
---------------------------------

every main ``App`` instance has a ``cache`` property
which can be any of the available :doc:`Caching Tools </tgram_dnd.caching>`

every ``cache`` has an ``items`` property, which is a map of string to :class:`CachedItem <tgram_dnd.caching.cached_item.CachedItem>`
each ``CachedItem`` has 2 property's

**value**: the value we cached in it

**ttl**: time_to_live

**What Is TTL?**
TTL (AKA time_to_live) is the value that this cached item will expire in, in seconds
for example if we have a ``CachedItem`` with a ttl of 10, when trying to ``get()`` this item's value
after 10 seconds has passed, the item will return ``None`` because it has expired

.. note::

    you can pass -1 in ttl for specifying infinite seconds
    by this way the item will **Never** expire

.. raw:: html

    <br>

Caching Example 🌈
---------------------

if you didn't understand the caching concept yet, we will make an example bot

.. note::

    in this example we will use :class:`MemoryCache <tgram_dnd.caching.memory.MemoryCache>`

**The App Idea**

we have an api that gives us the current Bitcoin Price `(ref) <https://docs.coingecko.com/reference/introduction>`_ 

we want to make a Bot UI for our users to know the price of Bitcoin

But There is a problem ❗

our current API plan is the Demo/Free one,
so our CallsPerMinute limit is 30 which is pretty low

so in a scenario where Bob, Alice, Jack (50+ others) make a request at the same time
only 30 of them will get the result, and the rest are gonna be blocked because of the CallsPerMinute limit

we can solve this problem by using a ``Cache``, which we will store the Bitcoin price in it every 5 seconds only

in the same scenario above (now using Caching ofc), all of the users will get the current Bitcoin Price.

this way the bot will check the cache

if the current cached price has no remaining ttl (Time to live, eg: expired), the bot will make another request
to the API 
and replace the cached price with the new price and the same 5 second limit

this way we can't exceed the CallsPerMinute API limit, and our max usage will be 12 CallsPerMinute which is way lower then the Free plan limit

**Enough Talking, More Coding 📊**

lets make the usual setup, :ref:`iykyk <get_started>`
and pass ``cache`` argument to the main ``App`` instance

.. note::
    each ``App`` has a MemoryCache as a default cache

lets start by importing needed stuff

.. code-block:: python

    from tgram_dnd import (
        App,
        MessageFlow,
        MessageBlock,
        Reply
    )
    from tgram_dnd.utils import run_function

    from tgram import TgBot, filters
    from tgram.types import Message

now lets make our custom **Middleware** to update the BTC price in the app cache

.. code-block:: python

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

as we see in the ``update_price`` Middleware above

we check the app cache for "btc_price", and
if the result is ``None`` we will query the API for the price.
and we will set the "btc_price" to the app Cache with a ttl of 5 seconds

now lets end it with the UI (Flows & Blocks)

.. code-block:: python

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

running this bot and trying to type .price, !price or /price should reply with
the BTC price

you can test it thorough the `Example <https://github.com/PythonNoob999/tgram_dnd/blob/main/examples/caching/price_bot.py>`_