#!/usr/bin/env python3
'''Module writes strings to Redis'''
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    '''Counts the no. of times a method is called'''


    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper function for the count_calls decorator'''
        schulssel = method.__qualname__
        self.redis_db.incr(schulssel)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''Cache class'''

    def __init__(self):
        '''Stores an instance of Redis Client'''
        self.redis_db = redis.Redis()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores data in Redis & generates a random key'''
        schulssel = str(uuid.uuid4())
        self.redis_db.set(schulssel, data)
        return schulssel

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        '''Retrieves data from Redis'''
        info = self.redis_db.get(key)
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
