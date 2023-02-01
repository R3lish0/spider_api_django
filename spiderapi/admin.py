from django.contrib import admin

from spiderapi.models import Owners,Farms,Fields,Crops

# Register your models here.
admin.site.register(Owners)
admin.site.register(Farms)
admin.site.register(Fields)
admin.site.register(Crops)
