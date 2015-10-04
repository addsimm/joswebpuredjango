"""
Legacy Username backend, docs at:
    http://psa.matiasaguirre.net/docs/backends/username.html
"""
from lib.social import LegacyAuth


class UsernameAuth(LegacyAuth):
    name = 'username'
    ID_KEY = 'username'
    EXTRA_DATA = ['username']
