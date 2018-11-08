import requests
import json
from datetime import datetime, timedelta
import pytz


BASE_URL = "http://0.0.0.0:8000/"

tz = pytz.timezone('Asia/Kolkata')
UNIQUE_TITLE = 'TITLE ' + str(datetime.now(tz).time())

days_till_sunday = 7 - datetime.today().weekday()

payload_task_1 = {
    'title': UNIQUE_TITLE + ' today',
    'description': 'Few words',
    'alert_time': '01:00'
}

payload_task_1['due_date'] = str(datetime.now(tz) + timedelta(hours=2))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_1)


payload_task_2 = {
    'title': UNIQUE_TITLE + ' thisweek',
    'description': 'Few words',
    'alert_time': '01:00'
}

payload_task_2['due_date'] = str(datetime.now(tz) + timedelta(days=days_till_sunday - 1))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_2)


payload_task_3 = {
    'title': UNIQUE_TITLE + ' nextweek',
    'description': 'Few words',
    'alert_time': '01:00'
}

payload_task_3['due_date'] = str(datetime.now(tz) + timedelta(days=days_till_sunday + 3))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_3)


payload_task_4 = {
    'title': UNIQUE_TITLE + ' overdue',
    'description': 'Few words',
    'alert_time': '01:00'
}

payload_task_4['due_date'] = str(datetime.now(tz) + timedelta(days=-2))
response = requests.post(BASE_URL + "api/v1/task/", json=payload_task_4)


def test_search_period_today():
    payload = {
        'period': 'today'
    }
    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    details = json.loads(response.text)
    tomorrow = datetime.combine(datetime.now().date() + timedelta(days=1), datetime.strptime('00:00', '%H:%M').time())
    date = datetime.strptime(details["objects"][0]['due_date'], '%Y-%m-%dT%H:%M:%S.%f')
    assert (date < tomorrow)


def test_search_period_thisweek():
    payload = {
        'period': 'thisweek',
        'title__contains': ' thisweek'
    }
    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    details = json.loads(response.text)
    end_of_week = datetime.combine(datetime.now().date() + timedelta(days=days_till_sunday), datetime.strptime('00:00', '%H:%M').time())
    date = datetime.strptime(details["objects"][0]['due_date'], '%Y-%m-%dT%H:%M:%S.%f')
    assert (date < end_of_week)


def test_search_period_nextweek():
    payload = {
        'period': 'nextweek'
    }
    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    details = json.loads(response.text)
    start_of_next_week = datetime.now().date() + timedelta(days=days_till_sunday)
    end_of_next_week = datetime.combine(start_of_next_week + timedelta(days=7), datetime.strptime('00:00', '%H:%M').time())
    date = datetime.strptime(details["objects"][0]['due_date'], '%Y-%m-%dT%H:%M:%S.%f')
    assert (date < end_of_next_week)


def test_search_period_overdue():
    payload = {
        'period': 'overdue'
    }
    response = requests.get(BASE_URL + "api/v1/task/", params=payload)
    details = json.loads(response.text)
    date = datetime.strptime(details["objects"][0]['due_date'], '%Y-%m-%dT%H:%M:%S.%f')
    assert (date < datetime.now())
