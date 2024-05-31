from django.db import models
from babel.dates import format_datetime


class Task(models.Model):
    """Модель для хранения задач"""
    title = models.TextField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    importance = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def formatted_creation_date(self):
        """Функция для красивого отображения даты создания задачи"""
        return format_datetime(self.creation_date, 'EEE dd.MM.yy', locale='ru').upper()

    def formatted_deadline(self):
        """Функция для красивого отображения дедлайна"""
        if self.deadline:
            return format_datetime(self.deadline, 'EEE dd.MM.yy', locale='ru').upper()
        else:
            return 'Нет дедлайна...'

    def formatted_completed(self):
        """Функция для красивого отображения статуса выполнения задачи"""
        return 'Выполнено!' if self.is_completed else 'В работе.'

    def formatted_importance(self):
        """Функция для красивого отображения важности задачи"""
        return 'Важно!' if self.importance else '...'
