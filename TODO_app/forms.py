from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'creation_date', 'is_completed', 'deadline', 'importance']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'datetime-local'})
        }