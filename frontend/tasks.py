from celery import shared_task, current_task


@shared_task
def printer(n):
    print("hello world 12345")
