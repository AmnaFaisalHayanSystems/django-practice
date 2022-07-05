from __future__ import absolute_import , unicode_literals
from django.contrib.auth import get_user_model

from celery import shared_task
from hwproject import settings
from django.utils import timezone
from datetime import timedelta

@shared_task()
def hello_world():
    return "Hello World!"
