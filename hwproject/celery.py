from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hwproject.settings')

app = Celery('hwproject')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

#settings
app.config_from_object('django.conf:settings')

# Celery Beat Settings
app.conf.beat_schedule = {
    'every-60-seconds': {
        'task': 'hello.tasks.hello_world',
        'schedule': crontab(hour=0, minute=1),
        #'args': (2,)
    }
    
}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')