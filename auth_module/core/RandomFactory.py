import os
import string
from random import choice



class RandomFactory:
    def __init__(self):
        pass

    def random_bytes(self, length=4) -> bytes:
        return os.urandom(length)

    def random_string(self, length):
        random_chars = [
            choice(string.ascii_uppercase + string.digits) for _ in range(length)
        ]
        return ''.join(random_chars)

