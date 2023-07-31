from django.db import models
from admin_user.models import *

# Create your models here.

class Student_Registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    email = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    dob = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    nationality = models.CharField(max_length=240, null=True)
    who = models.CharField(max_length=40, default='')
    school = models.CharField(max_length=40, null=True)
    qualification = models.CharField(max_length=40, null=True)
    study_abroad = models.CharField(max_length=40, null=True)
    intrest = models.CharField(max_length=60, null=True)
    others = models.CharField(max_length=60, null=True)
    #inschools
    address = models.CharField(max_length=240, null=True)
    school_ID = models.CharField(max_length=240, null=True)

    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    booking_ID = models.CharField(max_length=240, null=True)
    event_exp = models.DateField(max_length=240, null=True)
    QR = models.FileField(upload_to='qrcodes/', null=True, blank=True)
    register_DT = models.DateTimeField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True)
    

    def __str__(self):
        return self.fullname








