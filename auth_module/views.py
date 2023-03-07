import abc

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from kink import di, inject

from auth_module.core.AuthManagement import AuthManagement
from auth_module.core.Factory.UserFactory import UserFactory
from auth_module.core.decorator.AuthenticatedDecorator import authenticated
from auth_module.core.repository.UserRepository import UserRepository
from auth_module.models import User


# Create your views here

class BaseAuthView(View):
    def __init__(self):
        super().__init__()
        self.__user_repository = di[UserRepository]
        self.__auth_management = di[AuthManagement]

    @property
    def user_repository(self) -> UserRepository:
        return self.__user_repository
    @user_repository.setter
    def user_repository(self, value: UserRepository):
        self.__user_repository = value
    @property
    def auth_management(self) -> AuthManagement:
        return self.__auth_management
    @auth_management.setter
    def auth_management(self, value: AuthManagement):
        self.__auth_management = value



@inject
class RegisterView(BaseAuthView):
    def __init__(self):
        super(RegisterView, self).__init__()
        self.__user_factory = UserFactory()

    @property
    def user_factory(self):
        return self.__user_factory
    @user_factory.setter
    def user_factory(self, value):
        self.__user_factory = value

    def get(self, req):
        return render(req, "auth/register.html", {})

    def post(self, req):  # todo: validation
        email = req.POST['email']
        password = req.POST['password']
        new_user = self.user_factory.create_user(email, password)
        self.user_repository.register_new_user(new_user)
        return redirect('login')


@inject
class LoginView(BaseAuthView):
    def get(self, req):
        return render(req, "auth/login.html", {})
    def post(self, req):
        email = req.POST['email']
        password = req.POST['password']
        user = self.user_repository.find_user_by_email(email)
        user.validate_password(password)

        response = HttpResponse("ok")
        token = self.auth_management.register_token(user)
        response.set_cookie("email", email)
        response.set_cookie("token", token)
        return response

auth_view = None

@authenticated.cls
class AuthorizedView(BaseAuthView):
    def __init__(self):
        super(AuthorizedView, self).__init__()
        global auth_view
        auth_view = self
        print("AuthorizedView init called")

    @authenticated
    def get(self, req, logged_in_user: User):
        print(logged_in_user.email)
        return render(req, "hello-world.html", {})


