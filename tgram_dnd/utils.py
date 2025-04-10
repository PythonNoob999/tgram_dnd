from jinja2.nativetypes import NativeTemplate
from typing import Optional, Callable, Union, Any

import asyncio
import tgram_dnd

def get_target_function(
    obj: object,
    function_name: str
) -> Optional[Callable]:
    '''used to get a specific function from obj by getting its attribuites
    
    .. code-block:: python

        # example with first class method
        obj = Message
        target = "reply_text"
        method = get_target_function(obj, target)
        
        print(method)
        # <function Message.reply_text at 0xSomeAddress>

        # example with indented method
        obj = Message
        target = "user.mention"
        method = get_target_function(obj, target)
        
        print(method)
        # <funtion Message.User.mention at 0xSomeAddress>
         
        
    Args:
        obj (object)
        function_name (str): the wanted method seperated by dots, eg: obj_property.method_x
    Returns:
        Callable'''
    
    lom = function_name.split(".")
    func = obj

    for attr in lom:
        func = getattr(func, attr)
    
    return func

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

async def run_function(
    func: Union[Callable, "tgram_dnd.actions.Action"],
    *args,
    **kwargs
) -> Any:
    if asyncio.iscoroutinefunction(func) or isinstance(func, tgram_dnd.actions.Action):
        return await func(*args, **kwargs)
    return await asyncio.to_thread(func, *args, **kwargs)