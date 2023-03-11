from django.db import models
from django.db.models import Model

from auth_module.models import User
from schedule.models.DateRange import DateRange
from schedule.models.Label import Label
from schedule.models.Schedule import Schedule


class Booking(Model):
    ID = models.CharField(max_length=10, primary_key=True, auto_created=True)

    name = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)


