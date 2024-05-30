from django.db import models


class TaskCategory(models.Model):
    """Модель для хранения категорий задач"""
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):
    """Модель для хранения задач"""
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, related_name='tasks', null=True)

    def __str__(self):
        return self.title
