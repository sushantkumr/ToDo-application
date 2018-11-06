from django.shortcuts import render
from django.contrib import messages
from background_task import background
from background_task.models import Task
from task.models import TodoTask
from datetime import datetime, timedelta
import pytz


def home(request):
    alerts_for_tasks(request)
    hard_delete_records(repeat=Task.EVERY_4_WEEKS)
    return render(request, 'task/home.html')


def task_details(request, id):
    return render(request, 'task/taskDetails.html', {'id': id})


def create_task(request, id=None):
    return render(request, 'task/newTask.html', {'parent_task_id': id})


# 24*60*60*14 = 1209600 (14 days)
@background(schedule=1209600)
def hard_delete_records():
    print("Deleted records")
    queryset = TodoTask.objects.filter(deleted=True)
    queryset.delete()


def alerts_for_tasks(request):
    queryset = TodoTask.objects.filter(deleted=False).filter(completed=False)
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)

    for task in queryset:
        alert_period = task.due_date.astimezone(tz) - \
            timedelta(hours=task.alert_time.hour, minutes=task.alert_time.minute)
        if now > alert_period:
            messages.info(request, f'Alert: {task.title} is due at {task.due_date.astimezone(tz)}')
