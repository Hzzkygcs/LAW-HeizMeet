from django.db import models
from django.db.models import Model
from colorfield.fields import ColorField


class Label(Model):
    ID = models.CharField(max_length=10, primary_key=True, auto_created=True)
    name = models.CharField(max_length=25)
    color = ColorField(default='#99e4ff')
    keterangan = models.CharField(max_length=200)