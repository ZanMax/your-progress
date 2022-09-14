from django.db import connection
from django.utils import timezone
import plotly.express as px
import calendar


def date_range(start, end):
    delta = end - start
    dates = []
    for i in range(delta.days):
        dates.append(start + timezone.timedelta(days=i))
    dates.append(end)
    return dates


def create_chart(commits):
    now = timezone.now()
    start = now - timezone.timedelta(days=363)
    daterange = date_range(start, now)

    projects_list = []
    for c in commits:
        if c.project.name not in projects_list:
            projects_list.append(c.project.name)

    projects_chart = {}
    for project in projects_list:
        counts = [[] for _ in range(7)]
        dates = [[] for _ in range(7)]

        for dt in daterange:
            count = commits.filter(created__date=dt).filter(project__name=project).count()
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
                        width=1200,
                        labels=dict(x="Date", y="Day of the week", color="Commits"),
                        title=project,
                        )

        fig.update_traces({"xgap": 5, "ygap": 5})
        chart = fig.to_html(full_html=False, include_plotlyjs="cdn",
                            config={"displayModeBar": False})
        chart = chart.replace("\n", "")
        chart = chart.replace("'", "")
        projects_chart[project] = chart

    return projects_chart
