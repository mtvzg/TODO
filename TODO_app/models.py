from django.db import models
from babel.dates import format_datetime


class Task_Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):
    """Модель для хранения задач"""
    title = models.TextField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    importance = models.BooleanField(default=False)
    category = models.ForeignKey(Task_Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['is_completed', '-id']
        # это нужно для того, чтобы поля сортировались на уровне модели - по статусу выполнения и ID

    def __str__(self):
        return self.title

    def formatted_creation_date(self):
        """Функция для красивого отображения даты создания задачи"""
        return format_datetime(self.creation_date, 'EEE dd.MM.yy', locale='ru').title()

    def formatted_deadline(self):
        """Функция для красивого отображения дедлайна"""
        if self.deadline:
            deadline = format_datetime(self.deadline, 'EEE dd.MM.yy', locale='ru').title()
            return f'Завершить до {deadline}'
        else:
            return 'Нет дедлайна...'

    def formatted_importance(self):
        """Функция для красивого отображения важности задачи"""
        return 'Важно!' if self.importance else '...'

    def formatted_category(self):
        """Функция для красивого отображения категорий задач"""
        if self.category:
            return f'#{self.category}'
        else:
            return '...'
