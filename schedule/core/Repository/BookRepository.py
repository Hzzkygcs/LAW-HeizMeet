from django.db import models
from django.db.models import Model
from kink import inject

from auth_module.models import User
from schedule.models import Book
from schedule.models.DateRange import DateRange
from schedule.models.Label import Label
from schedule.models.Schedule import Schedule


@inject
class BookRepository(Model):
    def save(self, model):
        model.save()

    def create(self):
        return Book()

