from django.urls import include, path
from .views import index, msg

urlpatterns = [
    path('', index, name='helloworld'),
    path('msg', msg, name='msg'),
]