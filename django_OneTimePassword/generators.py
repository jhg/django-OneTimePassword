"""
Password generators

NOTE:
    For time synchronized use time.time() because is timezone-independent.
    http://stackoverflow.com/questions/11845803/is-pythons-time-time-timezone-specific
"""
from django.conf import settings
from hashlib import sha512
from time import time


class sha512TS(object):
    dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"
    length = 6
    interval = 30

    def __init__(self, length=6, interval=30, dictionary=None):
        if not dictionary is None:
            self.dictionary = dictionary
        self.length = length
        self.interval = interval

    def get_user_seed(self, username, *args, **kwargs):
        return sha512(
            settings.SECRET_KEY.encode('utf-8') +
            str(self.interval).encode('utf-8') +
            str(self.length).encode('utf-8') +
            username.encode('utf-8') +
            str(self.dictionary).encode('utf-8')
        ).hexdigest()

    def get_user_password(self, username, *args, **kwargs):
        token = sha512(
            self.get_user_seed(username).encode('utf-8') +
            str(int(time() / self.interval)).encode('utf-8')
        ).digest()
        password = ""
        for byte in token:
            password += self.dictionary[ord(byte) % len(self.dictionary)]
            if len(password) >= self.length:
                break
        return password[:self.length]
