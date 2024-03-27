from rest_framework import serializers

from cars.models import Car
from cars.serializers import CarSerializer
from loads.models import Load, LoadCarRelation


class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = ('pick_up', 'delivery', 'weight', 'description')


class LoadWithoutDescriptionSerializer(serializers.ModelSerializer):
    near_cars = serializers.IntegerField(read_only=True)

    class Meta:
        model = Load
        fields = ('pick_up', 'delivery', 'weight', 'near_cars','id')


class LoadCarSerializer(serializers.ModelSerializer):
    loads = LoadSerializer(read_only=True, many=True)

    class Meta:
        model = LoadCarRelation
        fields = ('distance', 'load', 'car', 'loads', 'id')
