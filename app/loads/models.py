from django.core import validators
from django.db import models

from business_logic.calculate_distance import calc_dist
from cars.models import Car

from locations.models import Location


# Create your models here.
class Load(models.Model):

    pick_up = models.ForeignKey(Location, related_name='pick_up', on_delete=models.PROTECT)
    delivery = models.ForeignKey(Location, related_name='delivery', on_delete=models.PROTECT)
    weight = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(1000)])
    description = models.TextField(blank=True)

    def __str__(self):
        return f'From : {self.pick_up.city} To : {self.delivery.city}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for i in Car.objects.all():
            from business_logic.set_relations import set_relations
            set_relations(load=self, car=i)




class LoadCarRelation(models.Model):
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=100, decimal_places=2, blank=True, default=None, null=True)

    def __str__(self):
        return f'From: {self.car.current_location.city} to {self.load.pick_up.city} {self.distance} miles. Number of car {self.car.number}'

    def save(
            self, *args, **kwargs):
        new_distance = calc_dist(self.load, self.car)
        self.distance = new_distance
        super().save(*args, **kwargs)
