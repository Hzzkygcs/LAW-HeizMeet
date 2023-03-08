from django.urls import include, path
from .views import RegisterView, LoginView, AuthorizedView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('authenticated', AuthorizedView.as_view(), name='authenticated'),
]