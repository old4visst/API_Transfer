from decimal import Decimal
from random import choice, randint

from django.core.management.base import BaseCommand

from cars.models import Car
from locations.models import Location


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(20):
            car = Car()
            car.current_location = choice(Location.objects.all())
            car.number = f'{randint(1000,9999)}A'
            car.lifting_capacity = randint(1,1000)
            car.save()
            print(car)
        print('finished')
