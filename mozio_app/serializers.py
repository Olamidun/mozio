import json
import pprint
from .models  import Provider, ServiceArea
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize



class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    
    class Meta:
        model = ServiceArea
        geo_field = 'polygon'
        fields = ['id', 'provider', 'polygon', 'name', 'price']
        # depth = 1

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }


class CreateServiceSerializer(serializers.Serializer):
    provider_id = serializers.IntegerField()
    polygon = serializers.JSONField(write_only=True)
    name = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=12, default=0)


    def create(self, validated_data):
        polygon = validated_data.get('polygon')
        name = validated_data.get('name')
        price = validated_data.get('price')
        # pprint.PrettyPrinter(indent=4).pprint(polygon)
        provider = Provider.objects.get(id=validated_data.get('provider_id'))
        service_area = ServiceArea.objects.create(polygon=GEOSGeometry(json.dumps(polygon)), name=name, price=price, provider=provider)
        return service_area
