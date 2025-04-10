class StopExecution(Exception):
    '''used to stop action Execution'''

class StopBlock(Exception):
    '''used to stop the block Execution'''

class InvalidStrings(Exception):
    '''raised when the given strings argument is invalid'''
    def __init__(self, msg: str):
        self.msg = msg
    
    def __str__(self):
        return f"StringConig should be FilePath or Dict[str, Dict[LANGUAGE_CODE, str]], not {self.msg}"