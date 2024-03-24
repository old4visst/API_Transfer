from decimal import Decimal

from django.core.management.base import BaseCommand

from locations.models import Location

file = open('/app/locations/management/commands/uszips.csv', 'r')
class Command(BaseCommand):
    def handle(self, *args, **options):

        file.readline()
        for i in file.readlines():
            print(i)
            values = i.replace('"', '').split(',')
            zip, lat, lng, city, state_name = int(values[0]), Decimal(values[1]), Decimal(values[2]), values[3], \
                values[5]
            locate = Location(zip=zip, lat=lat, lng=lng, city=city, state_name=state_name)
            locate.save()

        print('finished')
