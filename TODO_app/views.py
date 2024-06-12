from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from babel.dates import format_datetime
from datetime import datetime
from TODO_app.models import Task, Task_Category, TaskForm, LogInUserForm, RegisterUserForm


@login_required
def todo_home_page(request):
    """Функция-представление главной страницы проекта - здесь хранится текущая дата, для вывода в шапке приложения
    задачи из базы данных и категории задач"""
    current_date = format_datetime(datetime.now(), 'EEE dd.MM.yy', locale='ru').capitalize()
    tasks = Task.objects.filter(user_id=request.user.id)
    categories = Task_Category.objects.all()
    uncompleted_tasks = Task.objects.filter(user_id=request.user.id, is_completed=False).count()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            return redirect('todo_home')
    else:
        form = TaskForm()

    return render(request, 'todo_home.html',
                  {
                      'title': 'Главная',
                      'date': current_date,
                      'tasks': tasks,
                      'form': form,
                      'task_categories': categories,
                      'uncompleted_tasks': uncompleted_tasks
                  })


def task_status(request, task_id):
    """Функция для изменения статуса задачи (Выполнено/В работе и наоборот)"""
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('todo_home')


def delete_task(request, task_id):
    """Функция для удаления задачи из модели"""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo_home')


def update_task(request, task_id):
    """Функция для редактирования задачи в модели"""
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_home')
    else:

        form = TaskForm(instance=task)
        return render(request, 'todo_update_task.html', {
            'form': form
        })


def log_in(request):
    """Функция для авторизации пользователя"""
    if request.method == 'POST':
        form = LogInUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_home')
            else:
                messages.error(request, 'Кажется вы ввели неверное имя пользователя или пароль:(')
    else:
        form = LogInUserForm()
    return render(request, 'todo_login.html', {
        'title': 'Вход',
        'form': form
    })


def register_user(request):
    """Функция для регистрации пользователя"""
    if request.method == 'POST':
        new_user = User(
            username=request.POST.get('username'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name')
        )
        new_user.set_password(request.POST.get('password'))
        new_user.save()

        return HttpResponseRedirect('/login')

    form = RegisterUserForm

    return render(request, 'todo_register.html', {
        'title': 'Регистрация',
        'form': form
    })
