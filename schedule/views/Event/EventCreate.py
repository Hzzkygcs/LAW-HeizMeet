from django.http import HttpResponse
from django.shortcuts import render

from auth_module.core.Factory.UserFactory import UserFactory
from auth_module.core.decorator.AuthenticatedDecorator import authenticated
from auth_module.core.repository.UserRepository import UserRepository
from auth_module.models import User
from schedule.views.BaseScheduleView import BaseScheduleView


# Create your views here

class EventCreate(BaseScheduleView):
    @authenticated
    def get(self, req, logged_in_user: User):
        events = logged_in_user.get_list_of_events()
        print(events)
        return render(req, "events/event-create.html", {})

