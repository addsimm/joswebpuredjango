"""
Legacy Email backend, docs at:
    http://psa.matiasaguirre.net/docs/backends/email.html
"""
from lib.social import LegacyAuth


class EmailAuth(LegacyAuth):
    name = 'email'
    ID_KEY = 'email'
    REQUIRES_EMAIL_VALIDATION = True
    EXTRA_DATA = ['email']
