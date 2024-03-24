from rest_framework import serializers

from business_logic.calculate_distance import calc_dist
from cars.models import Car
from cars.serializers import CarSerializer
from loads.models import Load


class LoadSerializer(serializers.ModelSerializer):
    Load.near_cars = []
    for i in Car.objects.all():
        if calc_dist(Load.pick_up.zip,i.current_location.zip) > 0:
            Load.near_cars.append(i.current_location)

    class Meta:
        model = Load
        fields = ('pick_up', 'delivery', 'weight', 'near_cars')
