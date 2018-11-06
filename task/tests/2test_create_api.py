import requests
from datetime import datetime, timedelta
import pytz


BASE_URL = "http://0.0.0.0:8000/"

tz = pytz.timezone('Asia/Kolkata')
UNIQUE_TITLE = 'TITLE ' + str(datetime.now(tz).time())


def test_create_task():
    payload = {
        'title': UNIQUE_TITLE,
        'description': 'Few words',
        'alert_time': '01:00'
    }

    payload['due_date'] = str(datetime.now(tz) + timedelta(days=7))
    response = requests.post(BASE_URL + "api/v1/task/", json=payload)
    assert (response.status_code == 201)


def test_create_task_fail_repeat_title():
    payload = {
        'title': UNIQUE_TITLE,
        'description': 'Few words',
        'alert_time': '01:00'
    }

    payload['due_date'] = str(datetime.now(tz) + timedelta(days=7))
    response = requests.post(BASE_URL + "api/v1/task/", json=payload)
    assert (response.status_code == 500)


def test_create_task_fail_no_duedate():
    payload = {
        'title': UNIQUE_TITLE + '1',
        'description': 'Few words',
        'alert_time': '01:00'
    }

    response = requests.post(BASE_URL + "api/v1/task/", json=payload)
    assert (response.status_code == 500)
