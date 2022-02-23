from .base import *

DEBUG = False

SECRET_KEY = "405t(*e^o+0ep)=g8@36=0v&*y#60o%8++q8+ep72(f+r$qoa5"

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
