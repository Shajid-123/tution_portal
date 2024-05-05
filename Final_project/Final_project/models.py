from django.db import models

class customer(models.Model):
    name = models.CharField(max_length = 500)
    dob = models.CharField(max_length = 500)
    Phone = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    password = models.CharField(max_length=100)




class Tutor(models.Model):
    name = models.CharField(max_length = 500)
    dob = models.CharField(max_length = 500)
    Phone = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    subject = models.CharField(max_length = 500)
    timings = models.CharField(max_length = 500)
    fee = models.CharField(max_length = 500)
    desc = models.TextField(max_length = 5000)
    grade = models.TextField(max_length = 5000)
    

