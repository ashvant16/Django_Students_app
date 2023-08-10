from django.db import models
from . models import *

class Registration(models.Model):
    name=models.CharField( max_length=20)
    email=models.CharField( max_length=20)
    password=models.CharField( max_length=20)
    confirmPassword=models.CharField( max_length=20)
    insta=models.CharField(max_length=20)
    def __str__(self):
        return self.email

class MusicFiles(models.Model):
    title=models.CharField( max_length=50)
    artist=models.CharField( max_length=50)
    song=models.FileField(upload_to="audiotracks/")
    def __str__(self):
        return self.title
    class Meta:
        db_table='MusicFiles'

class Songs(models.Model):
    s_title=models.CharField( max_length=50)
    s_artist=models.CharField( max_length=50)
    songs=models.FileField(upload_to="songs/")
    def __str__(self):
        return self.s_title
    class Meta:
        db_table='Songs'