from django.contrib import admin

from TODO_app.models import TaskCategory, Task

admin.site.register(TaskCategory)
admin.site.register(Task)

