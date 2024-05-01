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
        '''wrapper fx for the count_calls decorator'''
        schulssel = method.__qualname__
        self._redis.incr(schulssel)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''Stores history of inputs & outputs for particular fx'''
    inschsl = method.__qualname__ + ":inputs"
    outschsl = method.__qualname__ + ":outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper fx for the call_history decorator'''
        self._redis.rpush(inschsl, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(outschsl, str(res))
        return res

    return wrapper


def replay(method: Callable) -> None:
    """doc doc class"""
    inpt_schsl = "{}:inputs".format(method.__qualname__)
    outpt_schsl = "{}:outputs".format(method.__qualname__)

    inpts = method.__self__._redis.lrange(inpt_schsl, 0, -1)
    outpts = method.__self__._redis.lrange(outpt_schsl, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(inpts)))
    for inp, out in zip(inpts, outpts):
        print(
            "{}(*{}) -> {}".format(
                method.__qualname__, inp.decode("utf-8"), out.decode("utf-8")
            )
        )


class Cache:
    '''Cache class'''

    def __init__(self):
        '''Stores an instance of Redis Client'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
