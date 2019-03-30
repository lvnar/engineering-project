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

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField('date_joined', auto_now_add=True)

    def __str__(self):
        return self.name
    
    def destroy(self, request, *args, **kwargs):
        vehicle = request.vehicle
        vehicle.is_active = False
        vehicle.save()
