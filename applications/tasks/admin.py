from django.contrib import admin
from applications.tasks.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_done', 'priority']