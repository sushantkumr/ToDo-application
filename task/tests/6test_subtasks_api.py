import requests
import json
from datetime import datetime, timedelta
import pytz


BASE_URL = "http://0.0.0.0:8000/"

tz = pytz.timezone('Asia/Kolkata')
UNIQUE_TITLE = 'TITLE ' + str(datetime.now(tz).time())
