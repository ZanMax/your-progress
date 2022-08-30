from django.contrib import admin
from .models import Projects, Commit

# Register your models here.

admin.site.register(Projects)
admin.site.register(Commit)
