from django.contrib import admin
from .models import Projects

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')

admin.site.register(Projects, ProjectsAdmin)