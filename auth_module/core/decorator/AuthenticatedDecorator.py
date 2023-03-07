import queue
from inspect import ismethod, getfullargspec

from kink import di, inject

from auth_module.core.AuthManagement import AuthManagement
from auth_module.exceptions.NotLoggedInException import NotLoggedInException


# decorator
# accepts func(self, req, logged_in_user, *args, **kwargs)
# returns func(self, req, *args, **kwargs)
class AuthenticatedDecorator:
    def __init__(self):
        self.__auth_management = di[AuthManagement]

    @property
    def auth_management(self) -> AuthManagement:
        return self.__auth_management

    @auth_management.setter
    def auth_management(self, value: AuthManagement):
        self.__auth_management = value

    def __call__(self, method):
        args = getfullargspec(method).args
        is_method = False
        if len(args) > 1 and ("self" in args[0].lower()):
            is_method = True
        return self.__decorate(method, is_method)

    def __decorate(self, method_or_func, is_method):

        class wrapper:
            def __init__(self_2nd):
                self_2nd._user_mock = queue.Queue()
                self_2nd.auth_management = self.auth_management

            def __call__(self_2nd, arg1, *args_list, **kwargs):
                req = arg1
                if is_method:
                    req = args_list[0]  # args2

                logged_in_user = self_2nd.get_user_object(req)
                args_list = args_list + (logged_in_user,)
                return method_or_func(arg1, *args_list, **kwargs)

            def restore_auth_management(self_2nd):
                self_2nd.auth_management = self.auth_management

            def __addi__(self_2nd, user_mock):  # to add mock
                self_2nd._user_mock.put(user_mock)

            def get_user_object(self_2nd, req):
                if not self_2nd._user_mock.empty():  # for mocking purpose
                    return self_2nd._user_mock.get()
                if 'token' not in req.COOKIES:
                    raise NotLoggedInException()
                token = req.COOKIES['token']
                return self_2nd.auth_management.get_user(token)
        return wrapper()


authenticated = AuthenticatedDecorator()
