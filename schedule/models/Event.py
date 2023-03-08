from django.db import models
from django.db.models import Model

from auth_module.models import User


class Event(Model):
    ID = models.CharField(max_length=10, primary_key=True, auto_created=True)
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    slot_selection_minute_multiplier = models.IntegerField()
    slot_book_minute_width = models.IntegerField()