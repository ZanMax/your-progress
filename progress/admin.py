from django.contrib import admin
from .models import Projects, Commit

# Register your models here.

admin.site.register(Projects)
admin.site.register(Commit)

admin.site.site_header = "Your-Progress Admin"
admin.site.site_title = "Your-Progress Admin"
admin.site.index_title = "Welcome to Your-Progress"
