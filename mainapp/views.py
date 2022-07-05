from django.shortcuts import render
from celery.schedules import crontab
from django.http.response import HttpResponse
from .tasks import test_func
from hello.tasks import hello_world
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def schedule_hw(request):
    hello_world.delay()
    return HttpResponse("Hello World!")

#def schedule_mail(request):
 #   schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
  #  task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
   # return HttpResponse("Done")




