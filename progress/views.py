import calendar
from django.shortcuts import render
from django.utils import timezone

from django.views import View

from progress.models import Commit
from progress.utils import date_range
import plotly.express as px
from progress.utils import create_chart


class Progress(View):
    def get(self, request):
        commits = Commit.objects.filter(user=request.user).order_by("created").select_related("project").all()

        project_commits = {}

        for c in commits:
            if c.project.name not in project_commits:
                project_commits[c.project.name] = []
            # project_commits[c.project.name].append(c)
            project_commits[c.project.name].append(c.created)

        projects_chart = {}
        for project, commits in project_commits.items():
            print(project)
            projects_chart[project] = create_chart(commits)
        """
        now = timezone.now()
        start = now - timezone.timedelta(days=364)
        daterange = date_range(start, now)
        counts = [[] for _ in range(7)]
        dates = [[] for _ in range(7)]
        for dt in daterange:
            count = commits.filter(created__date=dt).count()
            day_number = dt.weekday()
            counts[day_number].append(count)
            dates[day_number].append(dt)

        days = list(calendar.day_name)

        fig = px.imshow(counts,
                        color_continuous_scale="greens",
                        x=dates[0],
                        y=days,
                        height=280,
                        width=1200
                        )

        fig.update_traces({"xgap": 5, "ygap": 5})
        chart = fig.to_html()
        chart2 = fig.to_html()
        """

        return render(request, "progress.html", {'projects': projects_chart.items()})
