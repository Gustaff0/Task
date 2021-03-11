from django.contrib import admin
from webapp.models import Task, Type, Status

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_at', 'updated_at', 'status']
    list_filter = ['type']
    search_fields = ['summary', 'description']
    fields = ['id', 'summary', 'description', 'type', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'id']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
# Register your models here.
