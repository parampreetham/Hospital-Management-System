from django.contrib import admin
from .models import admins,hostels,students,visitors,warden
# Register your models here.

admin.site.register(admins)
admin.site.register(hostels)
admin.site.register(students)
admin.site.register(visitors)
admin.site.register(warden)