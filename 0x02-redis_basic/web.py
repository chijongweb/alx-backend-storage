#!/usr/bin/env python3
"""
Web caching with expiration and URL access tracking using Redis.
"""

import redis
import requests
from functools import wraps


def count_url_access(method):
    @wraps(method)
    def wrapper(url: str) -> str:
        r = redis.Redis()
        r.incr(f"count:{url}")
        return method(url)
    return wrapper


def cache_page(expiration: int = 10):
    def decorator(method):
        @wraps(method)
        def wrapper(url: str) -> str:
            r = redis.Redis()
            cache_key = f"cache:{url}"
            cached_data = r.get(cache_key)
            if cached_data:
                return cached_data.decode("utf-8")
            content = method(url)
            r.setex(cache_key, expiration, content)
            return content
        return wrapper
    return decorator


@count_url_access
@cache_page(expiration=10)
def get_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text
