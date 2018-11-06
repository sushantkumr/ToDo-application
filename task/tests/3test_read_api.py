import requests
import json
from datetime import datetime, timedelta
import pytz


BASE_URL = "http://0.0.0.0:8000/"

tz = pytz.timezone('Asia/Kolkata')
UNIQUE_TITLE = 'TITLE ' + str(datetime.now(tz).time())

payload_task_1 = {
    'title': UNIQUE_TITLE,
    'description': 'Few words',
    'alert_time': '01:00'
}

payload_task_1['due_date'] = str(datetime.now(tz) + timedelta(days=7))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_1)


payload_task_2 = {
    'title': UNIQUE_TITLE + ' Task 2',
    'description': 'Few words',
    'alert_time': '01:00'
}

payload_task_2['due_date'] = str(datetime.now(tz) + timedelta(days=7))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_2)


def test_get_task_with_title():
    payload_another_task = {
        'title': UNIQUE_TITLE + ' Task 2',
        'description': 'Few words',
        'alert_time': '01:00'
    }

    payload_another_task['due_date'] = str(datetime.now(tz) + timedelta(days=7))
    response = requests.post(BASE_URL + "api/v1/task/", json=payload_another_task)

    payload = {
        'title': UNIQUE_TITLE
    }

    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    task_details = json.loads(response.text)
    title = task_details['objects'][0]['title']
    assert (title == UNIQUE_TITLE)


def test_get_task_containing_pattern_in_title():
    payload = {
        'title__contains': UNIQUE_TITLE
    }

    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    details = json.loads(response.text)
    count = details['meta']['total_count']

    assert (count == 2)


def test_get_particular_task():
    task = requests.get(BASE_URL + "api/v1/task/", params={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']

    response = requests.get(BASE_URL + "api/v1/task/" + str(task_id) + "/")
    task_details = (json.loads(response.text))
    title = task_details['title']
    assert (title == UNIQUE_TITLE)


def test_get_task_fail():
    response = requests.get(BASE_URL + "api/v1/task/abcdefghijklmnopqrstuvwxyz/")
    assert response.status_code == 404


def test_get_all_tasks():
    response = requests.get(BASE_URL + "api/v1/task/")
    assert response.status_code == 200
