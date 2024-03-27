from random import choice

from django.core import validators
from django.db import models

from locations.models import Location


# Create your models here.
class Car(models.Model):
    number = models.CharField(max_length=5, primary_key=True,
                              validators=[
                                  validators.RegexValidator(regex=r'^[1-9][0-9]{3}[A-Z]$', message='Wrong number')])
    current_location = models.ForeignKey(Location, on_delete=models.PROTECT)
    lifting_capacity = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(1000)])

    def __str__(self):
        return f'Numb : {self.number}, Location : {self.current_location.city}, Max lift : {self.lifting_capacity}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from loads.models import Load
        for i in Load.objects.all():
            from business_logic.set_relations import set_relations
            set_relations(load=i,car=self)