import datetime

from django.shortcuts import render
from babel.dates import format_datetime
from datetime import datetime
from TODO_app.models import Task


def todo_home_page(request):
    """Функция-представление главной страницы проекта"""
    current_date = format_datetime(datetime.now(), 'EEE dd.MM.yy', locale='ru').capitalize()
    return render(request, 'home.html',
                  {
                      'title': 'Главная',
                      'date': current_date,
                      'tasks': Task.objects.all()
                  })
