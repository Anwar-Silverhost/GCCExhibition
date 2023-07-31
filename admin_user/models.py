from django.db import models

# Create your models here.

class Events(models.Model):
    event = models.CharField(max_length=240, null=True)
    from_date = models.DateField(max_length=240, null=True)
    to_date = models.DateField(max_length=240, null=True)
    from_time = models.TimeField(max_length=240, null=True)
    to_time = models.TimeField(max_length=240, null=True)
    location = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True)
    created_at = models.DateTimeField(max_length=240, null=True)

    def __str__(self):
        return self.event





