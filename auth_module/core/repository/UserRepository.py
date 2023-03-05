from kink import inject

from auth_module.models import User


@inject
class UserRepository:
    def register_new_user(self, user: User):
        raise NotImplementedError()

    def find_user_by_email(self, email: str) -> User:
        raise NotImplementedError()






