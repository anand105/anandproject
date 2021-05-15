from django.db import models

# Create your models here.
class student(models.Model):
    rollnum=models.IntegerField()
    name=models.CharField(max_length=30)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.IntegerField()
    address=models.TextField()
