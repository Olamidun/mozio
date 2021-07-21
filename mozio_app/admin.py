from django.contrib import admin
from .models import Provider, ServiceArea
# Register your models here.

class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'currency', 'language']


class ServiceareaAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider', 'price', 'polygon']

admin.site.register(Provider, ProviderAdmin)
admin.site.register(ServiceArea, ServiceareaAdmin)

# admin.site.register(GeoJsonModel)