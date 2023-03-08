from django.contrib import admin

from .models import Task, Priority
# Register your models here.

admin.site.register(Task)
admin.site.register(Priority)