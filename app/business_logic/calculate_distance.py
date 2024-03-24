from geopy import distance

from locations.models import Location


def calc_dist(loc_1, loc_2):
    loc_1 = Location.objects.get(zip=loc_1)
    loc_2 = Location.objects.get(zip=loc_2)
    loc_1 = (loc_1.lat, loc_1.lng)
    loc_2 = (loc_2.lat, loc_2.lng)
    return (distance.distance(loc_1, loc_2).miles)
