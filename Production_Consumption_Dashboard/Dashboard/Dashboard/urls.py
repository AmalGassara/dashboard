from django.urls import path
from .views import map_view, update_measures, update_exchange

urlpatterns = [
    path('', map_view, name='map-view'),
    path('update_measures', update_measures, name="update-measures"),
    path('update_exchange', update_exchange, name="update_exchange"),
]