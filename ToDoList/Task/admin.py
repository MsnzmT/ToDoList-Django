from django.contrib import admin
from .models import Task, List


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    pass
