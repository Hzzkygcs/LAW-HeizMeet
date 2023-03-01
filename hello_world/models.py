from django.db import models

# Create your models here.

class HelloWorldMessage(models.Model):
    message = models.CharField(max_length=90)
