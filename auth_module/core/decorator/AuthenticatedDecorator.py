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

    def __call__(self, method_or_func):
        args = getfullargspec(method_or_func).args
        if len(args) > 1 and args[0] == "self":
            return self.method(method_or_func)
        return self.func(method_or_func)

    def method(self, method):
        def method_wrapper(their_self, req, *args, **kwargs):
            logged_in_user = self.get_user_object(req)
            return method(their_self, req, logged_in_user, *args, **kwargs)
        return method_wrapper

    def func(self, func, *args, **kwargs):
        def func_wrapper(req, *args, **kwargs):
            logged_in_user = self.get_user_object(req)
            return func(req, logged_in_user, *args, **kwargs)
        return func_wrapper

    def get_user_object(self, req):
        if 'token' not in req.COOKIES:
            raise NotLoggedInException()
        token = req.COOKIES['token']
        return self.auth_management.get_user(token)


authenticated = AuthenticatedDecorator()
