from django.contrib import admin
from .models import Profile, Location
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, profileAdmin)
admin.site.register(Location, LocationAdmin)

