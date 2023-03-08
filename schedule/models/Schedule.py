from django.db import models
from django.db.models import Model

from schedule.models.DateRange import DateRange
from schedule.models.Event import Event
from schedule.models.Label import Label


class Schedule(Model):
    ID = models.CharField(max_length=10, primary_key=True, auto_created=True)
    name = models.CharField(max_length=25)

    datetime_range = models.OneToOneField(DateRange, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.RESTRICT)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

# TODO