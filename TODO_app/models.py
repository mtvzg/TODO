from django.contrib.auth.models import User
from django.db import models
from babel.dates import format_datetime
from django import forms


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['is_completed', '-id']
        # это нужно для того, чтобы поля сортировались на уровне модели - по статусу выполнения и ID

    @property
    def form(self):
        return TaskForm(instance=self)

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


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'importance', 'category']
        labels = {
            'title': 'Задача',
            'deadline': 'Завершить до...',
            'importance': 'Важная задача?',
            'category': 'Категория задачи'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Что надо сделать?'
            }),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'importance': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
                'role': 'switch',
                'id': 'flexSwitchCheckDefault'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            })
        }


class LogInUserForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин'
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )
