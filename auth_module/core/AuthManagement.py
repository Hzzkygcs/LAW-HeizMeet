from auth_module.core.RandomFactory import RandomFactory


# singleton
class AuthManagement:
    @staticmethod
    def get_instance():
        raise NotImplementedError()

    _random_factory = RandomFactory()

    def get_user(self, token: str):
        raise NotImplementedError()

    def register_token(self, user):
        raise NotImplementedError()

    def __generate_random_token(self) -> str:
        raise NotImplementedError()