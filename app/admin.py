from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(section)
admin.site.register(resource)
admin.site.register(student)
admin.site.register(lab)
admin.site.register(booking)
admin.site.register(resource_booking)
