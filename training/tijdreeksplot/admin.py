from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)


class RecordValueAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecordValue, RecordValueAdmin)


class RecordValueListAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecordValueList, RecordValueListAdmin)