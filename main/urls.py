from django.contrib import admin
from django.urls import path, include
from apps.mysite.views import view_404
handler404 = view_404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.mysite.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('apps.users.urls')),
    path('bedrooms/', include('apps.bedrooms.urls')),
]
