#!/usr/bin/env python3
'''Module uses requests to get html content'''
import requests
import redis
import time


def get_page(url: str) -> str:
    '''Fx gets HTML content from URL, tracks access & caches for 10sec'''
    red = redis.Redis()

    cached_html = red.get(url)
    if cached_html:
        red.incr(f"count:{url}")
        return cached_html.decode('utf-8')

    respse = requests.get(url)
    html_content = respse.text

    red.setex(url, 10, html_content)
    red.setex(f"count:{url}", 10, 1)

    return html_content
