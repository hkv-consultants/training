from django.contrib import admin
from .models import Location, RecordValue, RecordValueList


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Location, LocationAdmin)


class RecordValueAdmin(admin.ModelAdmin):
    list_filter = ('value_list', 'value_list__location')

admin.site.register(RecordValue, RecordValueAdmin)


class RecordValueListAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('location',)

admin.site.register(RecordValueList, RecordValueListAdmin)