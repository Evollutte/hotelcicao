from django.contrib import admin
from .models import Bedrooms


class BedroomsAdmin(admin.ModelAdmin):
    list_display = ['category', 'size', 'value', 'capacity', 'service']
    search_fields = ['category', 'size', 'value', 'capacity', 'service']


admin.site.register(Bedrooms, BedroomsAdmin)
