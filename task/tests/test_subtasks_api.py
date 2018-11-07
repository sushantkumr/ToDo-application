import requests
import json
from datetime import datetime, timedelta
import pytz


BASE_URL = "http://0.0.0.0:8000/"

tz = pytz.timezone('Asia/Kolkata')
UNIQUE_TITLE = 'TITLE ' + str(datetime.now(tz).time())

payload_task_1 = {
    'title': UNIQUE_TITLE + ' parenttask',
    'description': 'Few words',
    'alert_time': '01:00'
}

payload_task_1['due_date'] = str(datetime.now(tz) + timedelta(hours=2))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_1)

parent_task = requests.get(BASE_URL + "api/v1/task/", params={'title': UNIQUE_TITLE + ' parenttask'})
task_details = json.loads(parent_task.text)
parent_task_id = task_details['objects'][0]['id']

payload_task_2 = {
    'title': UNIQUE_TITLE + ' subtask',
    'description': 'Few words',
    'alert_time': '01:00',
    'parent_task_id': parent_task_id
}

payload_task_2['due_date'] = str(datetime.now(tz) + timedelta(hours=2))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_2)

sub_task = requests.get(BASE_URL + "api/v1/task/", params={'title': UNIQUE_TITLE + ' subtask'})
sub_task_details = json.loads(sub_task.text)
sub_task_id = sub_task_details['objects'][0]['id']


def test_get_sub_tasks():
    payload = {
        'parent_task_id': parent_task_id
    }

    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    details = json.loads(response.text)
    count = details['meta']['total_count']
    assert (count == 1)


def test_get_sub_tasks_fail():
    payload = {
        'parent_task_id': sub_task_id
    }

    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    details = json.loads(response.text)
    count = details['meta']['total_count']
    assert (count == 0)
