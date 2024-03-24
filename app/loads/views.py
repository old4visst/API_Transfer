from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from loads.models import Load
from loads.serializers import LoadSerializer


# Create your views here.
class LoadsViewSet(ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
