from django.core import validators
from django.db import models

from cars.models import Car
from locations.models import Location


# Create your models here.
class Load(models.Model):
    pick_up = models.ForeignKey(Location, related_name='pick_up', on_delete=models.PROTECT)
    delivery = models.ForeignKey(Location, related_name='delivery', on_delete=models.PROTECT)
    weight = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(1000)])
    description = models.TextField()
    near_cars = models.ManyToManyField(Car, related_name='near_cars')

    def __str__(self):
        return f'From : {self.pick_up.city} To : {self.delivery.city}'
