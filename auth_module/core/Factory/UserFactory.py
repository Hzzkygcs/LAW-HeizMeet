from typing import Union

from auth_module.models import User


class UserFactory:
    def __init__(self):
        raise NotImplementedError()

    def create_user(self, email: str, password: Union[bytes, str]):

        raise NotImplementedError()
