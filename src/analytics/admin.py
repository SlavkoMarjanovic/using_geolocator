from django.contrib import admin
from .models import Usersession, Oblast
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
class CountiesAdmin(LeafletGeoAdmin):
    list_display = ('name_0', 'varname_1')
admin.site.register(Usersession, IncidencesAdmin)
admin.site.register(Oblast, CountiesAdmin)