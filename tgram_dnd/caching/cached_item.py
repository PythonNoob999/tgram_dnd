from typing import Any, Optional

import time

class CachedItem:
    '''a Cached Item
    
    Args:
        value (Any): the stored Value
        ttl (int): the time_to_live for the item'''

    def __init__(
        self,
        value: Any,
        ttl: int = None
    ):
        self.value = value
        self.ttl = time.time() + (0 or ttl)

    @property
    def has_expired(self) -> bool:
        '''check if the item has passed its ttl or not'''
        return time.time() >= self.ttl

    def get(self) -> Optional[Any]:
        '''used to return the item value if it has not expired yet.'''
        return self.value if not self.has_expired else None