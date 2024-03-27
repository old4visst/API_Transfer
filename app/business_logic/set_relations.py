from cars.models import Car
from loads.models import LoadCarRelation, Load


def set_relations(load: Load, car: Car):
    rel,created = LoadCarRelation.objects.get_or_create(load=load, car=car)
    if not created:
        rel.save()
