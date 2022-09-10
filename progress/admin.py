from django.contrib import admin
from .models import Projects, Commit


# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'created')
    search_fields = ['name']
    list_per_page = 25


class CommitAdmin(admin.ModelAdmin):
    list_display = ('message', 'created', 'project')
    list_display_links = ('project', 'created', 'message')
    search_fields = ['project', 'created', 'message']
    list_per_page = 25


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Commit, CommitAdmin)

admin.site.site_header = "Your-Progress Admin"
admin.site.site_title = "Your-Progress Admin"
admin.site.index_title = "Welcome to Your-Progress"
