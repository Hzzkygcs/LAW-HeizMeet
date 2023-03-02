import hashlib

from django.db.models import Model
from django.db import models

from auth_module.core.SaltFactory import SaltFactory


class User(Model):
    app_label = 'auth_manager'

    email = models.EmailField(primary_key=True)
    _password = models.BinaryField(editable=True, max_length=128)
    _salt = models.BinaryField(editable=True, max_length=4)

    _salt_factory = SaltFactory()


    @property
    def password(self) -> bytes:
        return self._password

    @password.setter
    def password(self, value: bytes):
        self._salt = self._salt_factory.generate_salt()
        self._password = hashlib.sha512(self._salt + value).digest()

    def is_password_valid(self, password: bytes):
        hashed = hashlib.sha512(self._salt + password).digest()
        return hashed == self._password