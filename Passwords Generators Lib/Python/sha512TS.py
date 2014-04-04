from django.conf import settings
from hashlib import sha512
from time import time


def gen_user_password(seed, username, length=6, interval=30, dictionary=None):
    """
    Generate a password time synchroned for a user with a seed
    """
    # dictionary for generate password human friendly
    if dictionary == None:
        dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"
    # calc a sha512 hash from seed and time
    token = sha512(
        seed.encode('utf-8') +
        str(int(time() / interval)).encode('utf-8')
    ).digest()
    # make password
    password = ""
    for byte in token:
        # integer from byte value and in range of dictionary
        password += dictionary[ord(byte) % len(dictionary)]
        if len(password) >= length:
            break
    return password[:length]
