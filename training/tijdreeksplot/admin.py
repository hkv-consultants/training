from django.contrib import admin
from .models import Location, RecordValue, RecordValueList


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Location, LocationAdmin)


class RecordValueAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecordValue, RecordValueAdmin)


class RecordValueListAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(RecordValueList, RecordValueListAdmin)