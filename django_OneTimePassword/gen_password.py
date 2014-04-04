from django.conf import settings
from hashlib import sha512
from time import time


class sha512TS(object):
    dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"

    def get_user_seed(self, username, length=6, interval=30, dictionary=None):
        if dictionary == None:
            dictionary = self.dictionary
        return sha512(
            settings.SECRET_KEY.encode('utf-8') +
            str(interval).encode('utf-8') +
            str(length).encode('utf-8') +
            username.encode('utf-8') +
            str(dictionary).encode('utf-8')
        ).hexdigest()

    def get_user_password(self, username, length=6, interval=30, dictionary=None):
        if dictionary == None:
            dictionary = self.dictionary
        token = sha512(
            self.get_user_seed(
                username,
                length,
                interval,
                dictionary
            ).encode('utf-8') +
            str(int(time() / interval)).encode('utf-8')
        ).digest()
        password = ""
        for byte in token:
            password += dictionary[ord(byte) % len(dictionary)]
            if len(password) >= length:
                break
        return password[:length]
