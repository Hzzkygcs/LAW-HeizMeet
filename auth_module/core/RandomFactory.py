import os

import bcrypt as bcrypt


class RandomFactory:
    def __init__(self):
        pass

    def random_bytes(self, length=4) -> bytes:
        return os.urandom(length)

