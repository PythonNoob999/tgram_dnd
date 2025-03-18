#############
Basic Setup
#############

.. _get_started:

How To Get Started?
===================

| we can get started by making a (TgBot and App instance) and Making a config.json file
| this file will contain our bot Pre-made Text, keyboards and commands

*config.json:*

.. code-block:: javascript

    {
        "strings": {
            "start": {
                "en": "Welcome {{from.first_name}}"
            }
        },
        "commands": [
            {
                "command": "start",
                "description": "start the bot",
                "language_code": "en"
            }
        ]
    }

*main.py:*

.. code-block:: python

    from tgram import TgBot
    from tgram_dnd import App, BotConfig

    bot = TgBot("INSERT_BOT_TOKEN")
    app = App(
        bot=bot,
        config=BotConfig(
            config_file="config.json"
        )
    )

    app.run()

| Great, now we are ready to make our first Flow and run our bot!