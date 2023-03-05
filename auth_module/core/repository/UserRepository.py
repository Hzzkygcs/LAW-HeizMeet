from kink import inject

from auth_module.models import User


@inject
class UserRepository:
    def register_new_user(self, user: User):
        user.save()

    def find_user_by_email(self, email: str) -> User:
        return User.objects.get(email=email)






