from django.urls import path, include
from .api import v1_api

urlpatterns = [
    path('', include(v1_api.urls)),
]
