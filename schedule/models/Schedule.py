from django.db import models
from django.db.models import Model

from schedule.models.DateRange import DateRange
from schedule.models.Event import Event
from schedule.models.Label import Label


class Schedule(Model):
    ID = models.AutoField(primary_key=True)
    datetime_range = models.OneToOneField(DateRange, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.RESTRICT, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

# TODO