import datetime

from django.shortcuts import render, redirect, get_object_or_404
from babel.dates import format_datetime
from datetime import datetime

from TODO_app.forms import TaskForm
from TODO_app.models import Task


def todo_home_page(request):
    """Функция-представление главной страницы проекта"""
    current_date = format_datetime(datetime.now(), 'EEE dd.MM.yy', locale='ru').capitalize()
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_home')
    else:
        form = TaskForm()
    return render(request, 'todo_home.html',
                  {
                      'title': 'Главная',
                      'date': current_date,
                      'tasks': tasks,
                      'form': form
                  })


def task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('todo_home')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo_home')
