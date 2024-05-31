from django.shortcuts import render

from TODO_app.models import Task


def todo_home_page(request):
    """Функция-представление главной страницы проекта"""
    return render(request, 'home.html',
                  {
                      'title': 'Главная',
                      'tasks': Task.objects.all()
                  })
