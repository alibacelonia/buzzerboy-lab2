from django.contrib import admin
from .models import Project, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Number of empty forms to display

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = ('name', 'start_date', 'end_date', 'budget', 'status')
    search_fields = ('name', 'description')
    list_filter = ('status', 'start_date', 'end_date')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'due_date', 'priority', 'completed')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'completed', 'due_date', 'project')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)