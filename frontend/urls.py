from django.urls import path
from .views import home, task_details, create_task

urlpatterns = [
    path('', home, name='home'),
    path('task_details/<int:id>', task_details, name='task_details'),
    path('new_task/', create_task, name='create_task'),
    path('new_task/<int:id>', create_task, name='create_task')
]
