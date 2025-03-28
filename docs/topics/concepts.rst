##############
Core Concepts
##############

How does the Lib work?
======================

TgramDND uses Flows and LogicBlocks to run.

Every bot has a main :class:`App Instance <tgram_dnd.app.App>`, which is responsible
for containing all Flows and LogicBlocks.

An app contains Flows,  
which contain LogicBlocks,  
which have a series of actions.

.. raw:: html

    <br><br>

.. _what-is-a-flow?:

What Is A Flow ?
-----------------
a flow is a collection of LogicBlocks and is responsible
for passing needed updates through them

Flows has a lot of kinds, there is MessageFlows which is responsible for Message handling
and CallbackFlows that are responsible for Callbacks handling, etc...

they behave all the same, but just handle different types of Updates

.. raw:: html

    <br><br>

.. _what-are-blocks?:

What Are Blocks (AKA LogicBlocks) ?
------------------------------------
Blocks are like a function in a simple manner
each block has a filter, and an action_list or **actions**

a Block is responsible for passing the updates
to all of its actions 1 by 1

Blocks has a lot of kinds, there is MessageBlocks which is responsible for Message handling
and CallbackBlock that are responsible for Callbacks handling, etc...

they behave all the same, but just handle different types of Updates

.. raw:: html

    <br><br>

.. _what-is-an-action?:

What Is An Action?
-------------------
Action is the smallest unit of a Flow, an action is used
to execute something or preform a specifc task

Actions are like a function logic/lines in a simpler manner

.. raw:: html

    <br><br>

.. _how-it-all-works?:

How It All Works?
------------------

The below photo is a visual explantion to how the Flows work

.. image:: /images/how-it-works.png

Basically, A new update gets to your Telegram bot
This **NewMessage** gets passed to all your :ref:`Flows <what-is-a-flow?>`
then each Flow passes this update to there LogicBlocks
Then if the block filters matches the incoming update
it will execute its :ref:`Actions <what-is-an-action?>` 1 by 1

.. note::
    when running an ``App`` it will inject itself across all
    of its flows, blocks and actions, so every action can access the ``App`` resources

.. note:: Filtering

    All of your Flows and LogicBlocks can have Filters attached to them
    that way they only act if a specific update matches all of there filters
    you can read more about filters :doc:`Here <filters>`

.. raw:: html

    <br><br>

**For Example**

Lets say we have a MessageFlow, that filters messages with the text "!hello" or "!hi"
and 2 MessageBlocks one filters messages with the text "!hello" and other filters "!hi" respectively
and each block has only 1 action, that replies with the opposite keyword
so the "!hello" Block, responds with "!hi" and viceversa

Lets see the code example

first lets make a :ref:`starter setup <get_started>`

.. code-block:: python

    from tgram_dnd import (
        App,
        MessageFlow,
        MessageBlock,
        Reply
    )
    from tgram import TgBot, filters

    bot = TgBot("INSERT_BOT_TOKEN")
    app = App(bot=bot)

Great ! now lets make our message blocks

.. code-block:: python

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

Awesome!, now finally lets make the Flow **Which Will filter only !hi and !hello messages**
And add it to our app

.. code-block:: python

    flow = MessageFlow(
        blocks=[hi, hello],
        filter=(
            filters.command(["hi", "hello"], prefixes="!")
        )
    )

    app.add_flows(flow)

Finally lets run our App

.. code-block:: python

    app.run()

now try it in action 😎

.. image:: /images/hi_hello_bot_result.png

Access this example from `Here <https://github.com/PythonNoob999/tgram_dnd/blob/main/examples/hi_hello_bot.py>`_
By now you should know how the lib works!