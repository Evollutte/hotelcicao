from django.urls import path
from .views import index, bedrooms, gallery, about, contact


urlpatterns = [
    path('', index, name='home'),
    path('bedrooms/', bedrooms, name='bedrooms'),
    path('gallery/', gallery, name='galerry'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]