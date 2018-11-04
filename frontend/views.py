from django.shortcuts import render
from django.contrib import messages
from celery.schedules import crontab
from celery.task import periodic_task
from .tasks import printer


def home(request):
    messages.info(request, f'Alert: TITLE is due in X hours')
    # job = printer.delay(int(4))
    every_time()
    return render(request, 'task/home.html')


def task_details(request, id):
    return render(request, 'task/taskDetails.html')


def create_task(request, id=None):
    return render(request, 'task/newTask.html')


@periodic_task(run_every=crontab(hour=0, minute=1))
def every_time():
    print("This is run every Monday morning at 7:30")
