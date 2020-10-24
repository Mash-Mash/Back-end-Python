from collections import OrderedDict
from typing import Optional


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> Optional[str]:
        """получить значение по ключу"""
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def set(self, key: str, value: str) -> None:
        """добавить ключ-значение"""
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def delete(self, key: str) -> None:
        """удалить по ключу"""
        if key in self.cache:
            del self.cache[key]
