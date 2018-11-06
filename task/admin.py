from django.contrib import admin

# Register your models here.
from .models import TodoTask

admin.site.register(TodoTask)
