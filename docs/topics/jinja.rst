##################
Jinja Templating
##################

What Is Jinja ⁉️
------------------
as said in jinja's `introduction page <https://jinja.palletsprojects.com/en/stable/intro/>`_

    Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.

eg: Jinja can template strings and run python code inside them

Why TgramDND Uses Jinja ⁉️
---------------------------

| TgramDND uses Jinja2 for string templating
| which enables formatting variables on demand

**For Example**
in the usual :class:`BotConifg <tgram_dnd.config.BotConfig>` we declare strings like this:

.. code-block:: python

    BotConfig(
        strings={
            "string_name": {
                "language_code": "message"
            }
        }
    )

    # for example
    BotConfig(
        strings={
            "welcome": {
                "en": "Welcome in our bot 🖐️",
                "sp": "Bienvenido a nuestro bot 🖐️",
                "ru": "Добро пожаловать в наш бот 🖐️"
            }
        }
    )

| and to declare dynamic things like (user first name, user id, etc) we use the {{from.attribute}}
| where "from" is the variable that contains user info
| so for including the user name in our welcome message we can do the following:

.. code-block:: python

    BotConfig(
        strings={
            "welcome": {
                "en": "Welcome in our bot {{from.first_name}} 🖐️",
                "sp": "Bienvenido a nuestro bot {{from.first_name}} 🖐️",
                "ru": "Добро пожаловать в наш бот {{from.first_name}} 🖐️"
            }
        }
    )

| now when the user gets this string, the data between the curly braces
| will get replaced with its corresponding variable
| here is code demonstration:

tgram_dnd/utils.py:

.. code-block:: python

    def render_vars(
        string: str,
        *data
    ) -> Any:
        '''used to render all jinja-style variables
        
        Args:
            string (str): the target string
            *data (dict): the data to fill with
        Returns
            Any'''
        _ = {}
        for dictt in data:
            _ |= dictt
        
        result = NativeTemplate(string).render(**_)

        return result

| In the above code the ``render_vars`` function will Template the string using `jinja2.NativeTemplate <https://jinja.palletsprojects.com/en/stable/nativetypes/#jinja2.nativetypes.NativeTemplate>`_
| and pass any given Dict object as variables for the template to use it
| when using tgram_dnd's ``Reply`` action, this action will pass the user ``Message.json`` into the template data

tgram.types.Message.json Example:

.. code-block:: python

    {
        ...,
        "from": {
            "first_name": "Alice",
            "last_name": "Bob",
            "id": 1983032712,
        }
    }

| thus by using {{from.first_name}} variable in the code "Alice" will be passed (AKA the user first_name)

| You can see more examples at `Jinja's Documentation <https://jinja.palletsprojects.com/en/stable/nativetypes/#examples>`_ 
| to further understand how templating works