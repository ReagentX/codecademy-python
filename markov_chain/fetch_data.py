import requests
import requests_cache
from datetime import timedelta

expiry = timedelta(hours=4)
requests_cache.install_cache(expire_after=expiry)

def train(url):
    """Gets the data from a URL and caches it so that we do not make too many requests when testing"""
    r = requests.get(url)
    return r.content.decode('utf-8')
