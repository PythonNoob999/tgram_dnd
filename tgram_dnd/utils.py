from jinja2 import Template
from typing import Optional, Callable, Union

def get_target_function(
    obj: object,
    function_name: str
) -> Optional[Callable]:
    '''used to get a specific function from obj by getting its attribuites
    
    .. code_block:: python

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
) -> Union[int, str]:
    '''used to render all jinja-style variables
    
    Args:
        string (str): the target string
        *data (dict): the data to fill with
    Returns
        Union[str, int]'''
    _ = {}
    for dictt in data:
        _ |= dictt
    
    result = Template(string).render(**_)

    if result.isdigit(): result = int(result)
    return result