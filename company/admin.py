from django.contrib import admin
from company.models import *
from company.db_baise_models import *
# Register your models here.

class DatavalidationInline(admin.StackedInline):
    model = DataValidation
    max_num = 1


class Station_Admin(admin.ModelAdmin):
    list_display = ('name', 'type', 'in_or_out', 'mn')

    inlines = [
        DatavalidationInline,
    ]


class Company_Admin(admin.ModelAdmin):
    pass
class MaintainCompany_Admin(admin.ModelAdmin):
    pass
class ShutdownDate_Admin(admin.ModelAdmin):
    pass


admin.site.register(Station, Station_Admin)
admin.site.register(Company, Company_Admin)
admin.site.register(MaintainCompany, MaintainCompany_Admin)
admin.site.register(ShutdownDate, ShutdownDate_Admin)
