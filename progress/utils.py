from datetime import datetime


def convert_to_timestamp(date):
    timestamp = int(datetime.timestamp(date) * 1000)
    return timestamp


def create_chart(commits):
    projects_chart = {}

    for c in commits:
        if c.project.name not in projects_chart:
            projects_chart[c.project.name] = []
            projects_chart[c.project.name].append(convert_to_timestamp(c.created))
        else:
            projects_chart[c.project.name].append(convert_to_timestamp(c.created))

    return projects_chart
