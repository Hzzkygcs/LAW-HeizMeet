from __future__ import annotations
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model

from schedule.core.Intersection import Intersection


class DateRange(Model):
    ID = models.AutoField(primary_key=True)

    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def intersection_status(self, other: DateRange) -> Intersection:
        if self.end_date_time <= other.start_date_time:
            return Intersection.BEFORE  # self comes before other
        if other.end_date_time <= self.start_date_time:
            return Intersection.AFTER  # self comes after other
        if other.start_date_time < self.start_date_time and self.end_date_time < other.end_date_time:
            return Intersection.INSIDE  # self is inside the other
        if self.start_date_time < other.start_date_time and other.end_date_time < self.end_date_time:
            return Intersection.CONTAINS  # self contains the other
        return Intersection.INTERSECT  # self contains the other

    def clean(self):
        if self.start_date_time > self.end_date_time:
            raise ValidationError('Start date is after end date')

