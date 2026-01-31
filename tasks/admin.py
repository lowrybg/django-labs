from django.contrib import admin

from tasks.models import Task
from django.conf import settings
import os

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','is_done']
    search_fields = ['title']
    list_filter = ['is_done']
#    save_as = True



