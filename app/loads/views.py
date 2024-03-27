from django.db.models import Count, Case, When, Min
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from loads.models import Load, LoadCarRelation
from loads.serializers import LoadSerializer, LoadWithoutDescriptionSerializer


# Create your views here.


class LoadViewSet(ModelViewSet):
    def get_queryset(self):
        return Load.objects.all()

    def list(self, request, *args, **kwargs):
        flag = request.query_params.get('ordering')
        queryset = self.get_queryset().annotate(
            near_cars=Count(Case(When(loadcarrelation__distance__lte=450, then=1))))
        if flag is not None:
            if 'weight' in flag:
                queryset = queryset.order_by(flag)
                serializer = LoadWithoutDescriptionSerializer(queryset, many=True)
                return Response(serializer.data)
        serializer = LoadWithoutDescriptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = LoadCarRelation.objects.filter(load=pk)
        if len(queryset) == 0:
            return Response({'message': 'Wrong load_id'})
        cars = []
        for rel in queryset:
            cars.append({'number': rel.car.number, 'distance': rel.distance})
        serializer = LoadSerializer(queryset[0].load)
        return Response({'load': serializer.data, 'cars': cars})

    def get_serializer_class(self):
        return LoadSerializer

    # def create(self,request):

    # load = LoadSerializer(Load.objects.get(id=self.kwargs['pk']))
    # load.data["cars"] = LoadCarRelation.objects.filter(load=self.kwargs['pk'])

    # return load.data
