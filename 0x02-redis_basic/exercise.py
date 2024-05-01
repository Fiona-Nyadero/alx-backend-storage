#!/usr/bin/env python3
'''Module writes strings to Redis'''
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    '''Cache class'''

    def __init__(self):
        '''Stores an instance of Redis Client'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores data in Redis & generates a random key'''
        schulssel = str(uuid.uuid4())
        self._redis.set(schulssel, data)
        return schulssel

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        '''Retrieves data from Redis'''
        info = self._redis.get(key)
        if info is None:
            return None
        if fn:
            return fn(info)
        return info

    def get_str(self, key: str) -> str:
        '''Uses get method above with auto str conversion'''
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        '''Uses get method above with auto int conversion'''
        return self.get(key, fn=int)
