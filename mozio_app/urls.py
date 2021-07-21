from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name = 'mozio_app'

urlpatterns = [
    # path('', views.ProviderAPIView.as_view(), name='provider'),
    # path('<int:pk>', views.RetrieveUpdateDestroyAPIView.as_view()),
    path('service_areas', views.ServiceAreaAPIView.as_view()),
    path('service_areas/<int:pk>', views.RetrieveUpdateDestroyServiceAreaAPIView.as_view()),
    path('create_service_area', views.CreateServiceArea.as_view()),
    path('filter', views.ListServiceAreaWithLongAndLat.as_view())

]
