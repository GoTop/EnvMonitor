from django.contrib import admin
from company.models import *
from company.db_baise_models import *
# Register your models here.

class DatavalidationInline(admin.StackedInline):
    model = DataValidation
    max_num = 1


class Station_Admin(admin.ModelAdmin):
    list_display = ('district','name', 'type', 'in_or_out', 'station_id', 'report_url')
    list_display_links = ('name', )
    inlines = [
        DatavalidationInline,
    ]

    list_filter = ('company', )

    search_fields = ['name']




class Company_Admin(admin.ModelAdmin):
    list_display = ('district', 'name', 'trade')
    list_display_links = ('name', )

    list_filter = ('district', 'trade' )

    search_fields = ['name']


class MaintainCompany_Admin(admin.ModelAdmin):
    list_display = ('name',)
    pass


class ShutdownDate_Admin(admin.ModelAdmin):
    pass


admin.site.register(Station, Station_Admin)
admin.site.register(Company, Company_Admin)
admin.site.register(MaintainCompany, MaintainCompany_Admin)
admin.site.register(ShutdownDate, ShutdownDate_Admin)
