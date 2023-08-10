from django.db import models

# Create your models here.

class LeaveRequest(models.Model):
    namelr=models.CharField(max_length=20)    
    date = models.DateField()
    leave_type = models.CharField(max_length=20)
    reason = models.TextField()
    supporting_docs = models.FileField(upload_to='supdocfolder',blank=True)

    def __str__(self):
        return str(self.namelr)
    
class Registration(models.Model):
    name=models.CharField( max_length=20)
    email=models.CharField( max_length=35, unique=True)
    password=models.CharField( max_length=20)

    def __str__(self):
        return str(self.name)