from django.contrib import admin
from .models import SubProject, MainProject

# Register your models here.
admin.site.register(SubProject)
admin.site.register(MainProject)