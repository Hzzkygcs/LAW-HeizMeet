from __future__ import annotations
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model
from kink import inject

from schedule.core.Intersection import Intersection
from schedule.models import DateRange


@inject
class DateRangeRepository(Model):
    def save(self, model):
        model.save()

    def create(self):
        return DateRange()
