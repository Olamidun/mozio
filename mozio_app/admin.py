from django.contrib import admin
from .models import ServiceArea, Provider
# Register your models here.

class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'currency', 'language']


class ServiceareaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'polygon']

admin.site.register(Provider)
admin.site.register(ServiceArea, ServiceareaAdmin)

# admin.site.register(GeoJsonModel)