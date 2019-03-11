from django.contrib import admin
from api.core.models import Food, Diagnosis, Blacklist, Disease, Profile

# Register your models here.
admin.site.register(Food)
admin.site.register(Diagnosis)
admin.site.register(Blacklist)
admin.site.register(Profile)
