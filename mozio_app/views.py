from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .serializers import ProviderSerializer, ServiceAreaSerializer, CreateServiceSerializer
from .models import Provider, ServiceArea
from django.core.serializers import serialize
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


class CreateServiceArea(generics.CreateAPIView):
    serializer_class = CreateServiceSerializer
