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


def test_update_task_to_completed():
    task = requests.get(BASE_URL + "api/v1/task/", params={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']

    payload = {
        'completed': 'True'
    }
    response = requests.put(BASE_URL + 'api/v1/task/' + str(task_id) + '/', json=payload)
    assert response.status_code == 204


def test_update_task_to_pending():
    task = requests.get(BASE_URL + "api/v1/task/", params={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']

    payload = {
        'completed': 'False'
    }
    response = requests.put(BASE_URL + 'api/v1/task/' + str(task_id) + '/', json=payload)
    assert response.status_code == 204


def test_soft_delete_task():
    task = requests.get(BASE_URL + "api/v1/task/", params={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']
    print(task_details['objects'][0])

    payload = {
        'deleted': 'True'
    }
    response = requests.put(BASE_URL + 'api/v1/task/' + str(task_id) + '/', json=payload)
    assert response.status_code == 204
