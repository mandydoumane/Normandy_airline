from django.contrib import admin
from airline.models import * 

# Register your models here.
admin.site.register(User)
admin.site.register(Plane)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Booking)
admin.site.register(Company)