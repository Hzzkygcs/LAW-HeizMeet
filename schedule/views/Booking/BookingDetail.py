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
from schedule.views.Event.EventCreate import EventCreate


class BookingDetail(BaseScheduleView):
    def __init__(self):
        super().__init__()

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)


    @authenticated
    def get(self, req, logged_in_user: User, event_id):
        event = logged_in_user.event_set.get(ID=event_id)
        available_booking_slots = event.get_all_available_booking_slots()

        return render(req, "booking/available-booking-list.html", {
            'available_bookings': available_booking_slots
        })
