from django.db import models

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    file = models.FileField(upload_to='audio_player/')
