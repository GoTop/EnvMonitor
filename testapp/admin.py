from django.contrib import admin

# Register your models here.
from .models import Continent
from .models import Country
from .models import Area
from .models import Location


class ContinentAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    pass

class AreaAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Location, LocationAdmin)