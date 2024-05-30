from django.urls import path
from TODO_app import views


urlpatterns = [
    path('', views.todo_home_page, name='home')
]
