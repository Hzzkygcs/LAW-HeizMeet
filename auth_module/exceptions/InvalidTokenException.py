from http import HTTPStatus

from global_exception.exceptions.AutomaticallyHandledException import AutomaticallyHandledException


class InvalidTokenException(AutomaticallyHandledException):
    def __init__(self):
        super().__init__(
            HTTPStatus.BAD_REQUEST,
            "Invalid Token"
        )