#from decimal import Decimal
#
#from locations.models import Location
#
#file = open('uszips.csv', 'r')
#file.readline()
#for i in file.readlines():
#    values = i.replace('"', '').split(',')
#    zip, lat, lng, city, state_name = int(values[0]), Decimal(values[1]), Decimal(values[2]), values[3], values[5]
#    locate = Location(zip=zip, lat=lat,lng=lng, city=city, state_name=state_name)
#    locate.save()