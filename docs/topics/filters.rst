#########
Filters
#########

Filters What, Why and How !
============================

.. raw:: html

    <br><br>

.. _what-is-a-filter?:

What is a filter?
------------------

A filter is used to **as the name implies :)** filter incoming updates.
for example, lets say that we have a :ref:`MessageBlock <what-are-blocks?>` that
we want it to only process Message with the text "/start"

we will pass the tgram `filters.command() <https://z44d.github.io/tgram/tgram.html#tgram.filters.command>`_ to the block
just like this:

.. code-block:: python

    from tgram import filters

    MessageBlock(
        ...,
        filter=(
            filters.command("start", prefixes="/")
        )
    )

.. raw:: html

    <br><br>

.. _why-do-we-use-filters?:

Why Do We Use Filters?
------------------------

We use filters not only to filter incoming updates
But also to seperate our app logic
Instead of 1 big MessageFlow that has 1 big MessageBlock that process all messages
We can have multiple Flows and multiple MessageBlocks to handle different data

For example we can have 1 MessageFlow processing our bot basic commands
Like /start, /about, /support, /language etc...
And this flow includes 4 MessageBlocks to process each command

.. raw:: html

    <br><br>

.. _how-do-we-use-filters?:

How Do We Use Filters?
-----------------------

alot of basic filters like

* `command <https://z44d.github.io/tgram/tgram.html#tgram.filters.command>`_.

* `chat <https://z44d.github.io/tgram/tgram.html#tgram.filters.chat>`_.

* etc...

can be found in tgram `documentation <https://z44d.github.io/tgram/tgram.html#tgram.filters>`_.

but those filters can be limiting sometimes..., what if we want a custom filter to fill our needs?

.. raw:: html

    <br>

**How To Create A Custom Filter**

for this example, lets make a *vip-users* list filter
that only passes if the ComingUpdate is from a vip-user

lets start!

.. code-block:: python

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

Congrats! now you made your own custom filter,
you can test it thorugh this `example <https://github.com/PythonNoob999/tgram_dnd/blob/main/examples/custom_filter.py>`_