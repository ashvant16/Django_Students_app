from django.db import models

# Create your models here.
class Reminder(models.Model):
    rname=models.CharField(max_length=500)    
    rdate = models.DateField()

    def __str__(self):
        return str(self.rname)
    
class Tregistration(models.Model):
    name=models.CharField( max_length=20)
    email=models.CharField( max_length=35, unique=True)
    password=models.CharField( max_length=20)

    def __str__(self):
        return str(self.name)
    
class Timetable(models.Model):
    hnum = models.IntegerField(unique=True)
    hname = models.CharField(max_length=30)
    tname = models.CharField(max_length=30)

    def __str__(self):
        return str(self.hnum)
