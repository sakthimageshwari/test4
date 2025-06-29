from django.db import models






class q_a(models.Model):
    subject=models.CharField(max_length=255)
    question=models.CharField(max_length=255)
    option_1=models.CharField(max_length=255)
    option_2=models.CharField(max_length=255)
    option_3=models.CharField(max_length=255)
    option_4=models.CharField(max_length=255)
    answer=models.CharField(max_length=255)

class regform(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    dob=models.DateField()
    phone=models.IntegerField()
    email=models.CharField(max_length=255)
    uname=models.CharField(max_length=255)
    passcode=models.CharField(max_length=255)





# Create your models here.
