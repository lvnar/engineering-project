from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Vehicle(models.Model):
    number_plate = models.CharField(max_length=10, unique=True)

    last_position = ArrayField(
        models.DecimalField(decimal_places=8, max_digits=11),
        size=2,
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
