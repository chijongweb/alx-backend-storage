#!/usr/bin/env python3
"""
Web caching with expiration and URL access tracking using Redis.
"""

import redis
import requests
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def count_url_access(method):
    """
    Decorator to increment access count for a URL.
    Stores the count in Redis under key "count:{url}".
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        redis_client.incr(f"count:{url}")
        return method(url)
    return wrapper


def cache_page(expiration: int = 10):
    """
    Decorator to cache page content in Redis with a specified expiration time.
    Stores the cached content under key "cache:{url}".
    """
    def decorator(method):
        @wraps(method)
        def wrapper(url: str) -> str:
            cache_key = f"cache:{url}"
            cached_data = redis_client.get(cache_key)
            if cached_data:
                return cached_data.decode('utf-8')

            page_content = method(url)
            redis_client.setex(cache_key, expiration, page_content)
            return page_content
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


if __name__ == "__main__":
    test_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://example.com"

    print("First request (slow, not cached):")
    print(get_page(test_url)[:100])  # Print first 100 chars

    print("\nSecond request (should be cached):")
    print(get_page(test_url)[:100])

    print("\nAccess count:")
    print(redis_client.get(f"count:{test_url}"))