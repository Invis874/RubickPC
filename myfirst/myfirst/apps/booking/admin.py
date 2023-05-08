from django.contrib import admin

from .models import Hall, Computer, Reservation

admin.site.register(Hall)
admin.site.register(Computer)
admin.site.register(Reservation)