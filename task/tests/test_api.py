import requests
import json
from datetime import datetime


BASE_URL = "http://0.0.0.0:8000/"

UNIQUE_TITLE = str(datetime.now())


def test_create_task():
    payload = {
        'title': UNIQUE_TITLE,
        'description': 'Few words',
        'alert_time': '01:00'
    }

    payload['due_date'] = '2018-11-12 01:02:01'
    response = requests.post(BASE_URL + "api/v1/task/", json=payload)
    assert response.status_code == 201


def test_create_task_fail_no_title():
    payload = {
        'description': 'Few words',
        'alert_time': '01:00'
    }

    payload['due_date'] = '2018-11-12 01:02:01'
    response = requests.post(BASE_URL + "api/v1/task/", json=payload)
    assert response.status_code == 500


def test_get_task_with_title():
    payload = {
        'title': UNIQUE_TITLE
    }

    response = requests.get(BASE_URL + "api/v1/task/", json=payload)
    assert response.status_code == 200


def test_get_task_containing_pattern_in_title():
    payload = {
        'title__contains': UNIQUE_TITLE
    }

    response = requests.get(BASE_URL + "api/v1/task/", json=payload)
    assert response.status_code == 200


def test_get_particular_task():
    task = requests.get(BASE_URL + "api/v1/task/", json={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']

    response = requests.get(BASE_URL + "api/v1/task/" + str(task_id) + "/")
    assert response.status_code == 200


def test_get_task_fail():
    response = requests.get(BASE_URL + "api/v1/task/abcdefghijklmnopqrstuvwxyz/")
    assert response.status_code == 404


def test_get_all_tasks():
    response = requests.get(BASE_URL + "api/v1/task/")
    assert response.status_code == 200


def test_update_task_to_completed():
    task = requests.get(BASE_URL + "api/v1/task/", json={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']

    payload = {
        'completed': 'True'
    }
    response = requests.put(BASE_URL + 'api/v1/task/' + str(task_id) + '/', json=payload)
    assert response.status_code == 204


def test_update_task_to_pending():
    task = requests.get(BASE_URL + "api/v1/task/", json={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']

    payload = {
        'completed': 'False'
    }
    response = requests.put(BASE_URL + 'api/v1/task/' + str(task_id) + '/', json=payload)
    assert response.status_code == 204


def test_soft_delete_task():
    task = requests.get(BASE_URL + "api/v1/task/", json={'title': UNIQUE_TITLE})
    task_details = json.loads(task.text)
    task_id = task_details['objects'][0]['id']

    payload = {
        'deleted': 'True'
    }
    response = requests.put(BASE_URL + 'api/v1/task/' + str(task_id) + '/', json=payload)
    assert response.status_code == 204
