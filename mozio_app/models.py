from django.contrib.gis.db import models
from django.contrib.gis.db.models.fields import PointField
from djgeojson.fields import PolygonField
# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    language = models.CharField(max_length=30)
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=3, max_digits=12, default=0)
    polygon = models.PolygonField()