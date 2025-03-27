from tgram_dnd.caching.cached_item import CachedItem

from typing import Any, Dict, Optional, Callable

class BaseCache:

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
        raise NotImplementedError
    
    def get(
        self,
        key: str
    ) -> Optional[CachedItem]:
        '''get the CachedItem by key if has not expierd
        
        Args:
            key (str): the item key
        
        Returns:
            Optional[:class:`tgram_dnd.caching.cached_item.CachedItem`]'''
        raise NotImplementedError
    
    def get_or_create(
        self,
        key: str,
        value: Callable,
        ttl: int = None
    ) -> CachedItem:
        '''get the CachedItem by key, and if not exists a new CachedItem will be created and returned
        
        Args:
            ket (str): the item key
            value (Callable): the function that will retrive the item value (in case the item does not exist/expired)
            ttl (int, *optional*): item time_to_live, defaults to self.default_ttl
        
        Returns:
            :class:`tgram_dnd.caching.cached_item.CachedItem`'''
        raise NotImplementedError