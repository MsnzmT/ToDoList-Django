from django.db import models
from accounts.models import CustomUser


class List(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)


class Task(models.Model):
    List = models.ForeignKey(List, on_delete=models.CASCADE, blank=True, null=True, related_name='tasks')
    text = models.TextField()

    def __str__(self):
        return '{}'.format(self.text)

