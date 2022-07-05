from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.schedule_hw, name="shcedule_hw"),
    #path('sendmail/', views.send_mail_to_all, name="sendmail"),
    #path('schedulemail/', views.schedule_mail, name="schedulemail"),
]