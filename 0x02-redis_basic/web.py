#!/usr/bin/env python3
'''Module uses requests to get html content'''
import requests
import redis
import time


def get_page(url: str) -> str:
    '''Fx gets HTML content from URL, tracks access & caches for 10sec'''
    r = redis.Redis()

    cached_html = r.get(url)
    if cached_html:
        return cached_html.decode('utf-8')

    response = requests.get(url)
    html_content = response.text

    r.setex(url, 10, html_content)

    r.incr(f"count:{url}")

    return html_content
