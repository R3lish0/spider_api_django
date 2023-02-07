from django.contrib import admin

from spiderapi.models import Owners,Farms,Fields,Crops,Inputs,Seeds,Tests,Harvests

# Register your models here.
admin.site.register(Owners)
admin.site.register(Farms)
admin.site.register(Fields)
admin.site.register(Crops)
admin.site.register(Inputs)
admin.site.register(Seeds)
admin.site.register(Tests)
admin.site.register(Harvests)

