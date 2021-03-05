from django.urls import path
from apps.bedrooms.views import standard, higher, deluxe


urlpatterns = [
    path('standard/', standard, name='standard'),
    path('higher/', higher, name='higher'),
    path('deluxe/', deluxe, name='deluxe'),
]