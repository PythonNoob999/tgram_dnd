from tgram_dnd.caching.cached_item import CachedItem
from tgram_dnd.caching.base import BaseCache
from tgram_dnd.utils import run_function

from typing import Any, Dict, Optional, Callable

class MemoryCache(BaseCache):
    '''A Memory cache to store temporary items
    
    Args:
        default_ttl (int, *optional*): the default time_to_live in seconds for each item, defaults to 10'''

    def __init__(
        self,
        default_ttl: int = 10
    ):
        self.items: Dict[str, CachedItem] = {}
        self.default_ttl = default_ttl

    def set(
        self,
        key: str,
        value: Any,
        ttl: int = None
    ) -> Optional[CachedItem]:
        '''create a CachedItem with the ttl specified or the default_tll
        
        Args:
            key (str): the item key
            value (Any): the cached value
            ttl (int, *optional*): item time_to_live, defaults to self.default_ttl
        
        Returns:
            Optional[:class:`tgram_dnd.caching.cached_item.CachedItem`]'''

        if key in self.items: return

        self.items[key] = CachedItem(
            value=value,
            ttl=ttl or self.default_ttl
        )
        return self.items[key]
    
    def get(
        self,
        key: str
    ) -> Optional[Any]:
        '''get the CachedItem by key if has not expired
        
        Args:
            key (str): the item key
        
        Returns:
            Optional[Any]: the cached value'''

        if key not in self.items: return
        item = self.items[key]

        if item.has_expired:
            self.items.pop(key)
            return
        
        return item.get()
    
    async def get_or_create(
        self,
        key: str,
        value: Callable,
        ttl: int = None
    ) -> CachedItem:
        '''get the CachedItem by key, and if not exists a new CachedItem will be created and returned
        
        Args:
            ket (str): the item key
            value (Callable): the function that will retrieve the item value (in case the item does not exist/expired)
            ttl (int, *optional*): item time_to_live, defaults to self.default_ttl
        
        Returns:
            Any: The cached Value'''

        item = self.get(key)

        if item: return item

        item = self.set(
            key,
            (await run_function(value)),
            ttl,
        )
        return item.get()