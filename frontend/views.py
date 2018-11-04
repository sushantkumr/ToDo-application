from django.shortcuts import render
from django.contrib import messages
from background_task import background
from background_task.models import Task


def home(request):
    messages.info(request, f'Alert: TITLE is due in X hours')
    hard_delete_records(repeat=Task.EVERY_2_WEEKS)
    return render(request, 'task/home.html')


def task_details(request, id):
    return render(request, 'task/taskDetails.html')


def create_task(request, id=None):
    return render(request, 'task/newTask.html')


@background(schedule=1)  # Delete subsequent every day
def hard_delete_records():
    print("hello world")
