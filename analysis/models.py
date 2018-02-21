from django.db import models

# Create your models here.

class AudioFile(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now=True)