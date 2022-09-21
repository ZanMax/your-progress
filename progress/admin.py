from django.contrib import admin
from .models import Projects, Commit


# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'created')
    search_fields = ['name']
    readonly_fields = ['user']
    list_per_page = 25

    def get_queryset(self, request):
        qs = super(ProjectsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        Projects.user = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.user_id is None:
            obj.user_id = obj.user.id
        obj.save()


class CommitAdmin(admin.ModelAdmin):
    list_display = ('message', 'created', 'project')
    list_display_links = ('project', 'created', 'message')
    search_fields = ['project', 'created', 'message']
    readonly_fields = ['user']
    list_per_page = 25

    def get_queryset(self, request):
        qs = super(CommitAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        Commit.user = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.user_id is None:
            obj.user_id = obj.user.id
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "project":
            kwargs["queryset"] = Projects.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Commit, CommitAdmin)

admin.site.site_header = "Your-Progress Admin"
admin.site.site_title = "Your-Progress Admin"
admin.site.index_title = "Welcome to Your-Progress"
