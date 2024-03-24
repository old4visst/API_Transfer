from django.db import models


class Location(models.Model):
    zip = models.PositiveIntegerField(primary_key=True)
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    lng = models.DecimalField(max_digits=8, decimal_places=5)
    city = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return f"City : {self.city}, State : {self.state_name}, ZIP : {self.zip}"
