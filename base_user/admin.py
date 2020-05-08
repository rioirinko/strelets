from django.contrib import admin
#
# from base_user.models import User
#
# admin.site.register(User)
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email',]
