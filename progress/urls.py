from django.urls import path
from . import views

urlpatterns = [
    path("", views.Progress.as_view(), name="tenses"),
]
