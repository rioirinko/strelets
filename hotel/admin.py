from django.contrib import admin
from .models import *


class MyAdmin(admin.ModelAdmin):
    readonly_fields = ["total_sum", ]


admin.site.register(Customer, MyAdmin)
admin.site.register(Room)
admin.site.register(Employee)
admin.site.register(Cleaning)
admin.site.register(Booking)
