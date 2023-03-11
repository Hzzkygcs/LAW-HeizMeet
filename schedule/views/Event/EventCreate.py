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


# Create your views here





class EventCreate(BaseScheduleView):
    def __init__(self):
        super(EventCreate, self).__init__()
        self.schedule_factory = ScheduleFactory(di[DateRangeRepository], di[ScheduleRepository])

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    @authenticated
    def get(self, req, logged_in_user: User):
        events = logged_in_user.get_list_of_events()
        print(events)
        return render(req, "events/event-create.html", {})

    @authenticated
    def post(self, req, logged_in_user: User):
        body = req.POST.get('schedules')
        if body is None:
            raise BadRequestException("No post data: 'schedules'")
        event_name = req.POST.get('event_name')
        if event_name is None:
            raise BadRequestException("No post data: 'event_name'")

        schedules = self.convertToDate(json.loads(body))
        print(schedules, logged_in_user.email)
        self.saveNewEvent(logged_in_user, event_name, schedules)

        response = {'success': 1}
        return HttpResponse(json.dumps(response), content_type='application/json')

    def convertToDate(self, array_of_schedules):
        for arr_item in array_of_schedules:
            for key in ("start", "end"):
                date_time = datetime.strptime(arr_item[key], "%Y-%m-%dT%H:%M:%S.%fZ")
                arr_item[key] = timezone.make_aware(date_time)
        return array_of_schedules

    def saveNewEvent(self, user, name, schedules):
        created_schedules = []
        event = Event.objects.create(name=name, owner_id=user.email,
                                     slot_selection_minute_multiplier=15, slot_book_minute_width=30)

        for schedule in schedules:
            start, end = schedule['start'], schedule['end']
            new_schedule = self.schedule_factory.create_schedule(event.ID, start, end)
            created_schedules.append(new_schedule)
        print(created_schedules)