from django.urls import path
from TODO_app import views


urlpatterns = [
    path('', views.todo_home_page, name='todo_home'),
    path('task/<int:task_id>/', views.task_status, name='task_status'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')
]
