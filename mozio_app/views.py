import json
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework import generics
from .serializers import ServiceAreaSerializer,  ProviderSerializer, CreateServiceSerializer
from .models import ServiceArea, Provider
from django.contrib.gis.geos import GEOSGeometry, Polygon
# Create your views here.

class ProviderAPIView(generics.ListCreateAPIView):
    serializer_class = ProviderSerializer
    def get_queryset(self):
        return Provider.objects.all()


class RetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ProviderSerializer
    def get_queryset(self):
        return Provider.objects.filter()


class ServiceAreaAPIView(generics.ListAPIView):
    serializer_class = ServiceAreaSerializer
    def get_queryset(self):
        return ServiceArea.objects.all()


class RetrieveUpdateDestroyServiceAreaAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceAreaSerializer
    def get_queryset(self):
        return ServiceArea.objects.filter()


class ListServiceAreaWithLongAndLat(generics.ListAPIView):
    serializer_class = ServiceAreaSerializer
    def get_queryset(self):
        # longitude is horizontal
        longitude = self.request.query_params.get('lng')
        print(longitude)
        
        latitude = self.request.query_params.get('lat')
        print(latitude)
        
        polygon = {"type": "Point", "coordinates": [float(longitude), float(latitude)]}
        pnt = GEOSGeometry(json.dumps(polygon))
        qs = ServiceArea.objects.filter(polygon__contains=pnt)
        return qs

class CreateServiceArea(generics.CreateAPIView):
    serializer_class = CreateServiceSerializer
