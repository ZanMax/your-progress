from django.utils import timezone


def date_range(start, end):
    delta = end - start
    dates = []
    for i in range(delta.days):
        dates.append(start + timezone.timedelta(days=i))
    return dates
