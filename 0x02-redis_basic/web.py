#!/usr/bin/env python3
"""
Web caching with expiration and tracking URL access counts using Redis.
"""

import redis
import requests
from functools import wraps

redis_client = redis.Redis()


def count_url_access(method):
    """
    Decorator to increment count for the URL access using Redis key "count:{url}".
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        redis_client.incr(f"count:{url}")
        return method(url)
    return wrapper


def cache_page(expiration: int = 10):
    """
    Decorator to cache page content in Redis with expiration.
    """
    def decorator(method):
        @wraps(method)
        def wrapper(url: str) -> str:
            cached = redis_client.get(f"cache:{url}")
            if cached:
                return cached.decode('utf-8')
            page = method(url)
            redis_client.setex(f"cache:{url}", expiration, page)
            return page
        return wrapper
    return decorator


@count_url_access
@cache_page(expiration=10)
def get_page(url: str) -> str:
    """
    Fetch HTML content of a URL using requests.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

