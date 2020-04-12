from django.contrib import admin
from .models import *


class MyAdmin(admin.ModelAdmin):
    readonly_fields = ["price", ]


admin.site.register(Room)
admin.site.register(Employee)
admin.site.register(Booking, MyAdmin)
admin.site.register(Services)
admin.site.register(Review)