from django import forms
from .models import Task


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
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Что надо сделать?'}),
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
