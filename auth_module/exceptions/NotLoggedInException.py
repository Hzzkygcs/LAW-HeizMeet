from http import HTTPStatus

from global_exception.exceptions.AutomaticallyHandledException import AutomaticallyHandledException


class NotLoggedInException(AutomaticallyHandledException):
    def __init__(self):
        super().__init__(
            HTTPStatus.UNAUTHORIZED,
            "Please Log In"
        )