from django.db import models

# Create your models here.

class AppStore(models.Model):
    appname = models.CharField(max_length=240, null=True)
    description = models.CharField(max_length=240, null=True)
    app_file = models.FileField(upload_to='AppStore/', null=True, blank=True)
    app_logo = models.FileField(upload_to='AppStore/', null=True, blank=True)
    download_count = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.appname


