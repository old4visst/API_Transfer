from geopy import distance


def calc_dist(load, car):
    loc_1 = load.pick_up
    loc_2 = car.current_location
    loc_1 = (loc_1.lat, loc_1.lng)
    loc_2 = (loc_2.lat, loc_2.lng)
    return (distance.distance(loc_1, loc_2).miles)
