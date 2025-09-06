import os

from .base import *

_env = os.getenv("DJANGO_ENV", "development").lower()
if _env == "production":
    from .production import *
else:
    from .development import *
