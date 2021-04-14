from django.contrib import admin
from webapp.models import Task, Type, Status, Project

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_at', 'updated_at', 'status', 'project']
    list_filter = ['type']
    search_fields = ['summary', 'description']
    fields = ['id', 'summary', 'description', 'status', 'created_at', 'updated_at', 'project']
    readonly_fields = ['created_at', 'updated_at', 'id', 'project']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'timestart', 'timefinish']
    list_filter = ['name']
    search_fields = ['name', 'description']
    fields = ['id', 'name', 'description', 'timestart', 'timefinish', 'user']
    readonly_fields = ['id']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)
# Register your models here.
