from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DUserAdmin
from core.forms import RegisterForm
from core.models import *


class UserAdmin(DUserAdmin):
    form = RegisterForm
    model = User
    list_display = ['first_name', 'last_name', 'username',
                    'email', 'password', 'birth_date', 'height', 'weight', 'age']


admin.site.register(Food)
admin.site.register(Diagnosis)
admin.site.register(Blacklist)
admin.site.register(User, UserAdmin)
