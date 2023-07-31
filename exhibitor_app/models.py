from django.db import models
from admin_user.models import *
from student_app.models import *

# Create your models here.
class Exhibitors(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    exhibitors = models.CharField(max_length=240, null=True)
    boothnumber = models.CharField(max_length=240, default='0')
    contactperson = models.CharField(max_length=240, null=True)
    contactemail = models.CharField(max_length=240, null=True)
    contactnumber = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, default='0')

    def __str__(self):
        return self.event.event


class BoothVisitors(models.Model):
    Booth = models.ForeignKey(Exhibitors, on_delete=models.CASCADE, null=True)
    visitor =  models.ForeignKey(Student_Registration, on_delete=models.CASCADE, null=True)
    booking_ID = models.CharField(max_length=240, null=True)
    visited_DT = models.DateTimeField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, default='0')
    def __str__(self):
        return self.event.event



