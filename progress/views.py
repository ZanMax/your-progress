from django.shortcuts import render
from django.views import View

from progress.models import Commit
from progress.utils import create_chart


class Progress(View):
    def get(self, request):
        commits = Commit.objects.filter(user=request.user).order_by("created").select_related("project").all()
        projects_chart = create_chart(commits)
        return render(request, "progress.html", {'projects': projects_chart})
