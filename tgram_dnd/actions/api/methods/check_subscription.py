from tgram_dnd.actions import Action

from tgram.types import (
    ChatMemberLeft,
    ChatMemberBanned,
    ChatMemberRestricted
)

from typing import TypedDict, Union

class SubscribedKwargs(TypedDict):
    chat_id: Union[int, str]
    user_id: Union[int, str]
'''Subscribed kwgs'''

class Subscribed(Action):
    '''this Action is used to check wether a user is a member in the specified channel/chat

    .. code-block:: python

        from tgram_dnd import ..., Subscribed, Reply, Condition

        Condition(
            action=Subscribed({
                "chat_id": CHAT_ID,
                "user_id": "{{from.id}}"
            }),
            success=Reply("text", {"text": "You are Subscribed"}),
            fail=Reply("text", {"text": "You are NOT Subscribed please subscribe @YourChat"})
        )
        
    Args:
        kwgs: (:class:`tgram_dnd.actions.api.methods.check_subscription.SubscribedKwargs`): the check arguments
        middleware (Callable, *optional*): a function to be executed before the main function run
        fill_vars (bool, *True*): Wether to automatically render vars in kwgs or not, defaults to *true*
        allow_resticted (bool, *True*): wether to count `RestrictedChatMember <https://z44d.github.io/tgram/tgram.types.html#tgram.types.ChatMemberRestricted>`_ as an allowed condition or not
        default_value (bool, *False*): the default boolean value returned when an Exception occurs during the check process, defaults to False (Operation Failed)'''

    def __init__(
        self, 
        kwgs: SubscribedKwargs,
        middleware = None,
        fill_vars = True,
        allow_restricted: bool = True,
        default_value: bool = False
    ):
        super().__init__(None, kwgs, middleware, fill_vars)
        self.allow_restricted = allow_restricted
        self.default_value = default_value

    async def __call__(self, u):

        async def check(
            chat_id: Union[int, str],
            user_id: Union[int, str]
        ) -> bool:
            try:
                member = await self.bot.get_chat_member(
                    chat_id=chat_id,
                    user_id=user_id
                )

                return not (
                    isinstance(
                        member,
                        (ChatMemberBanned, ChatMemberLeft)
                    ) or
                    (
                        isinstance(
                            member,
                            ChatMemberRestricted
                        ) if not self.allow_restricted else False
                    )
                )
            except Exception as e:
                print(e)
                return self.default_value

        self.func = check
        return await super().__call__(u)