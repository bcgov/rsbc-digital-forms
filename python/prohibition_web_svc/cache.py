
from flask_caching import Cache
from python.prohibition_web_svc.config import Config

cache = Cache(config={
    'CACHE_TYPE': 'SimpleCache', 
    'CACHE_DEFAULT_TIMEOUT': Config.CACHE_TIMEOUT,
  })