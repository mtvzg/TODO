from django.db import models


class Task(models.Model):
    """Модель для хранения задач"""
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    importance = models.BooleanField(default=False)

    def __str__(self):
        return self.title
