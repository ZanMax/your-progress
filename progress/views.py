import calendar
from django.shortcuts import render
from django.utils import timezone

from django.views import View

from progress.models import Commit
from progress.utils import date_range
import plotly.express as px


class Progress(View):
    def get(self, request):
        commits = Commit.objects.filter(user=request.user).order_by("created")

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
        first_day = daterange[0].weekday()
        days = days[first_day:] + days[:first_day]

        fig = px.imshow(counts,
                        color_continuous_scale="greens",
                        x=dates[0],
                        y=days,
                        height=320,
                        width=1300
                        )
        fig.update_traces({"xgap": 5, "ygap": 5})
        chart = fig.to_html()
        return render(request, "progress.html", {"chart": chart})
