from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User


# Create your models here.

class Projects(TimeStampedModel):
    name = models.CharField(max_length=100)
    goal = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"


class Commit(TimeStampedModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
