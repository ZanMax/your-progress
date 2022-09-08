from django.utils import timezone
import plotly.express as px
import calendar


def date_range(start, end):
    delta = end - start
    dates = []
    for i in range(delta.days):
        dates.append(start + timezone.timedelta(days=i))
    return dates


def create_chart(commits):
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
    return chart
