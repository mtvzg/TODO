from django.urls import path
from django.contrib.auth import views as auth_views
from TODO_app import views


urlpatterns = [
    path('', views.todo_home_page, name='todo_home'),
    path('task/<int:task_id>/', views.task_status, name='task_status'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('login/', views.log_in, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_user, name='register')
]
