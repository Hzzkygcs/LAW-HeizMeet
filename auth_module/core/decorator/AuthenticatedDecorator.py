import inspect
import queue
from inspect import ismethod, getfullargspec, getmembers

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

    def cls(self, cls):
        return self.class_decorator(cls)

    def __call__(self, method):
        return self.method_decorator(method)

    def method_decorator(self, method):
        method._AuthenticatedDecorator_need_authentication = True
        return method

    def class_decorator(self, cls):
        outter_self = self
        orig_init = cls.__init__

        def __init__(self, *args, **kwargs):
            orig_init(self, *args, **kwargs)
            self._AuthenticatedDecorator_user_mock = queue.Queue()
            self._AuthenticatedDecorator_auth_management = outter_self.auth_management
            self.add_user_mock = lambda mock: self._AuthenticatedDecorator_user_mock.put(mock)
        cls.__init__ = __init__

        for name, method in getmembers(cls):
            if hasattr(method, "_AuthenticatedDecorator_need_authentication"):
                def wrap(method):
                    def new_method(inner_self, req, *args, **kwargs):
                        logged_in_user = self.get_user_object(req, inner_self)
                        args = args + (logged_in_user,)
                        return method(self, req, *args, **kwargs)
                    return new_method
                setattr(cls, name, wrap(method))
        return cls


    def get_user_object(self, req, instance):
        user_mock = instance._AuthenticatedDecorator_user_mock
        auth_management = instance._AuthenticatedDecorator_auth_management

        if not user_mock.empty():  # for mocking purpose
            return user_mock.get()
        if 'token' not in req.COOKIES:
            raise NotLoggedInException()
        token = req.COOKIES['token']
        return auth_management.get_user(token)



authenticated = AuthenticatedDecorator()
