from django.utils import timezone
from datetime import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from kink import di

from auth_module.core.Factory.UserFactory import UserFactory
from auth_module.core.decorator.AuthenticatedDecorator import authenticated
from auth_module.core.repository.UserRepository import UserRepository
from auth_module.models import User
from global_exception.exceptions import BadRequest
from global_exception.exceptions.BadRequest import BadRequestException
from schedule.core.Repository.DateRangeRepository import DateRangeRepository
from schedule.core.Repository.ScheduleRepository import ScheduleRepository
from schedule.core.ScheduleFactory import ScheduleFactory
from schedule.models import Event
from schedule.views.BaseScheduleView import BaseScheduleView


class BookingDetail(BaseScheduleView):
    def __init__(self):
        super(EventCreate, self).__init__()

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    @authenticated
    def get(self, req, logged_in_user: User, schedule_id):
        events = logged_in_user.get_list_of_events()
        print(events)
        return render(req, "events/event-create.html", {})
