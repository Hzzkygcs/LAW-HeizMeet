import os
import string
from random import choice



class RandomFactory:
    def random_bytes(self, length=4) -> bytes:
        return os.urandom(length)

    def random_string(self, length, strings=string.ascii_letters+string.digits):
        random_chars = [
            choice(strings) for _ in range(length)
        ]
        return ''.join(random_chars)

