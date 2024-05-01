#!/usr/bin/env python3
'''Module writes strings to Redis'''
import redis
import uuid
from typing import Union


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
