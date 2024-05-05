from django.db import models

# Create your models here.

class Tutor(models.Model):
    img = models.ImageField(upload_to="images/")
    name = models.CharField(max_length = 500)
    dob = models.CharField(max_length = 500)
    Phone = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    subject = models.CharField(max_length = 500)
    timings = models.CharField(max_length = 500)
    fee = models.CharField(max_length = 500)
    desc = models.TextField(max_length = 5000)
    grade = models.TextField(max_length = 5000)
    v_c = models.TextField(max_length = 5000)
    v_status = models.TextField(max_length = 5000)