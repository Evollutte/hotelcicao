from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.mysite.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('apps.users.urls')),
    path('bedrooms/', include('apps.bedrooms.urls')),
]
