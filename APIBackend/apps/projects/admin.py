from django.contrib import admin
from .models import Project,Task
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','status']
admin.site.register(Project,ProjectAdmin)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name','assigned_to','created_at','due_date','status']
admin.site.register(Task,TaskAdmin)