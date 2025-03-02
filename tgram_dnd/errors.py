class StopExecution(Exception):
    '''used to stop action Execution'''

class InvalidStrings(Exception):
    def __init__(self, msg: str):
        self.msg = msg
    
    def __str__(self):
        return f"StringConig should be FilePath or Dict[str, Dict[LANGUAGE_CODE, str]], not {self.msg}"