"""
Get and process settings for django-OneTimePassword
"""
from django.conf import settings
from importlib import import_module


# Default settings

OTP_TIME_SYNCHRONIZED_GENERATOR = 'django_OneTimePassword.generators.sha512TS'

OTP_TIME_SYNCHRONIZED_OPTIONS = {
    'length': 6,
    'interval': 30,
    'dictionary': "abcdefghijklmnopqrstuvwxyz0123456789"
}


# Try get settings

OTP_TIME_SYNCHRONIZED_GENERATOR = getattr(
    settings,
    'OTP_TIME_SYNCHRONIZED_GENERATOR',
    OTP_TIME_SYNCHRONIZED_GENERATOR
)

OTP_TIME_SYNCHRONIZED_OPTIONS = getattr(
    settings,
    'OTP_TIME_SYNCHRONIZED_OPTIONS',
    OTP_TIME_SYNCHRONIZED_OPTIONS
)


# Get password generatos

OTP_TIME_SYNCHRONIZED_GENERATOR = getattr(
    import_module('.'.join(OTP_TIME_SYNCHRONIZED_GENERATOR.split('.')[:-1])),
    OTP_TIME_SYNCHRONIZED_GENERATOR.split('.')[-1]
)

# Instance generators

OTP_TIME_SYNCHRONIZED = OTP_TIME_SYNCHRONIZED_GENERATOR(
    **OTP_TIME_SYNCHRONIZED_OPTIONS
)
