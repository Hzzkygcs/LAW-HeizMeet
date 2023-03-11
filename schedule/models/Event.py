from django.db import models
from django.db.models import Model

from auth_module.models import User
from schedule.models.not_django_models.AvailableBooking import AvailableBooking


class Event(Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    slot_selection_minute_multiplier = models.IntegerField()
    slot_book_minute_width = models.IntegerField()

    @property
    def get_all_available_booking_slots(self) -> list[AvailableBooking]:
        ret = []
        schedules = self.schedule_set.all()

        for schedule in schedules:
            available_slots = schedule.get_available_slots()
            for available_slot in available_slots:
                ret.append(AvailableBooking(schedule.ID, available_slot))
        return ret
